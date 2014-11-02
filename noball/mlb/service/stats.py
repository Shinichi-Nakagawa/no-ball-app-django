#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
選手の情報に関する振る舞いを提供するService
"""

import locale
from datetime import datetime

from service.const import POSITION_PITCHER, POSITION_BATTER
from service.stats import Stats
from noball.settings import APPLICATION_NAME


__author__ = 'Shinichi Nakagawa'


class Stats(object):

    # サブドメイン名
    SUB_DOMAIN = 'mlb'
    # Queryのキー名
    QUERY_KEY = 'query_word'

    # 右/左/両の略称
    SHORT_NAME_RIGHT = 'R'
    SHORT_NAME_LEFT = 'L'
    SHORT_NAME_SWITCH = 'S'

    # 通貨記号（アメリカなので＄）
    CURRENCY = '$'
    # SALARYの分母(million)
    BASE_SALARY = 1000000

    # ピタゴラス勝率のべき乗
    PYTHAGORIAN_POWER = 1.8

    def __init__(self, encode):
        locale.setlocale(locale.LC_NUMERIC, encode)

    def get_base_context(self):
        """
        戻り値定数セット
        :return: 戻り値(固定)
        """
        return {
            'APPLICATION_NAME': APPLICATION_NAME,
            'QUERY_KEY': Stats.QUERY_KEY,
            'SUB_DOMAIN': Stats.SUB_DOMAIN,
            'PLAYER_BATTER': POSITION_BATTER,
            'PLAYER_PITCHER': POSITION_PITCHER,
            'MENU_ENABLE': True,
        }

    def get_pythagoras_dataset(self, teams):
        """
        ピタゴラス勝率を含んだデータセットを返す
        :param teams: Team Model List
        :return: pythagoras % list
        """
        datasets = []
        for t in teams:
            d = {
                'team': t.teamID,
                'name': t.name,
                'div': t.divID,
                'rank': t.Rank,
                'g': t.G,
                'w': t.W,
                'l': t.L,
                'r': t.R,
                'er': t.ER,
                'win_p': Stats.calc_winning_percentage(t.W, t.G),
                'pyt_p': Stats.calc_pythagorean_expectation(t.R, t.RA)
            }
            d['pyt_p_w'] = round(t.G * d['pyt_p'], 0)
            d['pyt_p_l'] = t.G - d['pyt_p_w']
            datasets.append(d)
        return datasets

    def get_sabr_value_batter(self, player, stats, salary):
        """
        SABR Stats for batter
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :return: (dict)sabar stats data
        """
        # TODO 書き直す
        # SABR Data(batter)
        _datasets = {
            'rc_list': [],
            'babip_list': [],
            'dunn_list': []
        }

        for items in stats:
            # 複数Recordあり得るので足し込む
            year = items[0]
            hr, bb, so, pa = 0, 0, 0, 0
            h, ab, sf, rc = 0, 0, 0, 0
            hbp, cs, gidp, sh, sb, ibb = 0, 0, 0, 0, 0, 0
            single, _2b, _3b = 0, 0, 0
            for batting in items[1]:
                hr = hr + batting.HR
                bb = bb + batting.BB
                so = so + batting.SO
                h = h + batting.H
                ab = ab + batting.AB
                sf = sf + batting.SF
                hbp = hbp + batting.HBP
                cs = cs + batting.CS
                gidp = gidp + batting.GIDP
                sh = sh + batting.SH
                sb = sb + batting.SB
                ibb = ibb + batting.IBB
                _2b = _2b + batting._2B
                _3b = _3b + batting._3B

            pa = Stats.pa(ab, bb, hbp, sf, sh)
            single = Stats.single(h, hr, _2b, _3b)
            rc = Stats.rc(h, bb, hbp, cs, gidp, sf, sh, sb, so, ab, ibb, single, _2b, _3b, hr)

            _datasets['rc_list'].append(
                {
                    'year': year,
                    'rc': Stats.rc27(rc, ab, h, sh, sf, cs, gidp)
                }
            )

            _datasets['dunn_list'].append(
                {
                    'year': year,
                    'dunn': Stats.adam_dunn_batter(hr, bb, so, pa)
                }
            )
            _datasets['babip_list'].append(
                {
                    'year': year,
                    'avg': Stats.avg(h, ab),
                    'babip': Stats.babip(h, hr, ab, so, sf)
                }
            )
        return _datasets

    def get_sabr_value_pitcher(self, player, stats, salary):
        """
        SABR Stats for batter
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :return: (dict)sabar stats data
        """
        # TODO 書き直す
        # SABR Data(pitcher)
        _datasets = {
            'whip_list': [],
            'hr9_list': [],
            'dunn_list': []
        }

        for items in stats:
            # 複数Recordあり得るので足し込む
            year = items[0]
            bb, h, hr, so, hbp, bfp = 0, 0, 0, 0, 0, 0
            ip_outs = 0
            for pitching in items[1]:
                ip_outs = ip_outs + pitching.IPouts
                bb = bb + pitching.BB
                h = h + pitching.H
                hr = hr + pitching.HR
                so = so + pitching.SO
                hbp = hbp + pitching.HBP
                bfp = bfp + pitching.BFP

            ip = Stats.ip(ip_outs)

            _datasets['whip_list'].append(
                {
                    'year': year,
                    'whip': Stats.whip(bb, h, ip)
                }
            )
            _datasets['hr9_list'].append(
                {
                    'year': year,
                    'hr9': Stats.hr9(hr, ip),
                    'bb9': Stats.bb9(bb, ip),
                    'so9': Stats.so9(so, ip)
                }
            )
            _datasets['dunn_list'].append(
                {
                    'year': year,
                    'dunn': Stats.adam_dunn_pitcher(hr, bb, hbp, so, bfp)
                }
            )
        return _datasets

    def get_home_value_pitcher(self, player, stats, salary):
        """
        Pitcher profile
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :return: pitcher profile(dict)
        """
        # TODO 書き直す
        # statsから必要な値を修得
        w, l, so, er, ipo, year, teams = 0, 0, 0, 0, 0, 0, []
        if len(stats) > 0:
            year = stats[0][0]
            for s in stats[0][1]:
                w = w + s.W
                l = l + s.L
                so = so + s.SO
                er = er + s.ER
                ipo = ipo + s.IPouts
                teams.append(s.teamID)

        # ipを計算
        ip = Stats.ip(ipo)

        _prof = self._get_base_profile(player, year, teams, salary)
        _prof['position'] = POSITION_PITCHER.upper()
        _prof['win'] = w
        _prof['lose'] = l
        _prof['era'] = Stats.era(er, ip)
        _prof['so'] = so
        return _prof

    def get_home_value_batter(self, player, stats, salary):
        """
        Batter profile
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :return: batter profile(dict)
        """
        # TODO 書き直す
        # statsから必要な値を修得
        hr, rbi, h, ab, year, teams = 0, 0, 0, 0, 0, []
        if len(stats) > 0:
            year = stats[0][0]
            for s in stats[0][1]:
                h = h + s.H
                ab = ab + s.AB
                hr = hr + s.HR
                rbi = rbi + s.RBI
                teams.append(s.teamID)

        _prof = self._get_base_profile(player, year, teams, salary)
        _prof['position'] = POSITION_BATTER.upper()
        _prof['avg'] = Stats.avg(h, ab)
        _prof['hr'] = hr
        _prof['rbi'] = rbi
        return _prof

    def _get_base_profile(self, player, year, teams, salary):
        """
        Profile(Base)
        :param player: Player master model
        :param year: Last play year
        :param teams: teams
        :param salary: Player salary model
        :return: profile(dict)
        """
        return {
            'year': year,
            'team': ','.join(teams),
            'age': Stats.calc_age(player.birthYear),
            'birthday': '%d/%d/%d' % (player.birthYear, player.birthMonth, player.birthDay),
            'salary': Stats._calc_salary(salary),
            'country': player.birthCountry,
            'city': player.birthCity,
            'bats': player.bats,
            'throws': player.throws,
            'display_name': ' '.join([player.nameFirst, player.nameLast])

        }

    @classmethod
    def _calc_salary(cls, salary):
        """
        年俸計算
        :param salary: salary model list
        :return:
        """
        sal = 0
        if len(salary) > 0:
            for s in salary[0][1]:
                sal = sal + s.salary
        return Stats._get_salary(sal)

    @classmethod
    def _get_salary(cls, money):
        """
        表示用のsalary
        :param money: salary
        :return: (str) salary
        """
        # SALARY編集
        if money == None or money == '':
            return '?'
        _money = int(money)
        if _money >= Stats.BASE_SALARY:
            return '%s%sM' % (Stats.CURRENCY, "{:n}".format(_money / Stats.BASE_SALARY))
        else:
            return '%s%s' % (Stats.CURRENCY, "{:n}".format(_money))

    @classmethod
    def calc_age(cls, year):
        """
        calculate age
        :param year: (int)birth year
        :return: (int) age
        """
        now = datetime.now()
        return now.year - year

    @classmethod
    def calc_winning_percentage(cls, w, g):
        """
        勝率
        :param w: win
        :param g: games
        :return: winning percentage
        """
        return round(w / g, 3)

    @classmethod
    def calc_pythagorean_expectation(cls, r, ra):
        """
        ピタゴラス勝率
        :param r: Runs Scored
        :param ra: Runs Allowed
        :return: pythagorean expectation
        """
        r_power = r ** Stats.PYTHAGORIAN_POWER
        ra_power = ra ** Stats.PYTHAGORIAN_POWER
        return round(r_power / (r_power + ra_power), 3)

