#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

"""
選手の情報に関する振る舞いを提供するService
"""

import locale
from datetime import datetime

from service.const import POSITION_PITCHER, POSITION_BATTER
from service.stats import Stats as BaseballStats
from noball.settings import APPLICATION_NAME
from mlb.service.sean_lahman import SeanLahmanDB as MlbDB


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

    # 戻り値の件数(固定)
    STATS_LIMIT = 4

    def __init__(self, encode):
        pass
        # locale.setlocale(locale.LC_NUMERIC, encode)

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
                'team': t.teamid,
                'name': t.name,
                'div': t.divid,
                'rank': t.rank,
                'g': t.g,
                'w': t.w,
                'l': t.l,
                'r': t.r,
                'er': t.er,
                'win_p': Stats.calc_winning_percentage(t.w, t.g),
                'pyt_p': Stats.calc_pythagorean_expectation(t.r, t.ra)
            }
            d['pyt_p_w'] = round(t.g * d['pyt_p'], 0)
            d['pyt_p_l'] = t.g - d['pyt_p_w']
            datasets.append(d)
        return datasets

    def get_sabr_value_batter(self, player, stats, salary, html=True):
        """
        SABR Stats for batter
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :param html: HTMLで表示(default:True)
        :return: (dict)sabar stats data
        """
        # SABR Data(batter)
        _datasets = {
            'rc_list': [],
            'babip_list': [],
            'dunn_list': []
        }

        for batting in stats:
            year = batting.yearid
            pa = BaseballStats.pa(batting.ab, batting.bb, batting.hbp, batting.sf, batting.sh)
            single = BaseballStats.single(batting.h, batting.hr, batting.number_2b, batting.number_3b)
            rc = BaseballStats.rc(
                batting.h,
                batting.bb,
                batting.hbp,
                batting.cs,
                batting.gidp,
                batting.sf,
                batting.sh,
                batting.sb,
                batting.so,
                batting.ab,
                batting.ibb,
                single,
                batting.number_2b,
                batting.number_3b,
                batting.hr
            )

            _datasets['rc_list'].append(
                {
                    'year': year,
                    'rc': BaseballStats.rc27(rc, batting.ab, batting.h, batting.sh, batting.sf, batting.cs, batting.gidp)
                }
            )

            _datasets['dunn_list'].append(
                {
                    'year': year,
                    'dunn': BaseballStats.adam_dunn_batter(batting.hr, batting.bb, batting.so, pa)
                }
            )
            _datasets['babip_list'].append(
                {
                    'year': year,
                    'avg': BaseballStats.avg(batting.h, batting.ab),
                    'babip': BaseballStats.babip(batting.h, batting.hr, batting.ab, batting.so, batting.sf)
                }
            )
        # HTML表示の場合かつ戻り値件数未満の場合は空行を追加
        if html:
            cnt_row = self.STATS_LIMIT - len(stats)
            while cnt_row > 0:
                year -= 1
                _datasets['rc_list'].append(
                    {
                        'year': year,
                        'rc': 0.0
                    }
                )
                _datasets['dunn_list'].append(
                    {
                        'year': year,
                        'dunn': 0.0
                    }
                )
                _datasets['babip_list'].append(
                    {
                        'year': year,
                        'avg': 0.0,
                        'babip': 0.0,
                    }
                )
                cnt_row -= 1
                if cnt_row == 0:
                    break
        return _datasets

    def get_sabr_value_pitcher(self, player, stats, salary, html=True):
        """
        SABR Stats for batter
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :param html: HTMLで表示(default:True)
        :return: (dict)sabar stats data
        """
        # SABR Data(pitcher)
        _datasets = {
            'whip_list': [],
            'hr9_list': [],
            'dunn_list': []
        }

        year = None
        for pitching in stats:
            year = pitching.yearid

            ip = BaseballStats.ip(pitching.ipouts)

            _datasets['whip_list'].append(
                {
                    'year': year,
                    'whip': BaseballStats.whip(pitching.bb, pitching.h, ip)
                }
            )
            _datasets['hr9_list'].append(
                {
                    'year': year,
                    'hr9': BaseballStats.hr9(pitching.hr, ip),
                    'bb9': BaseballStats.bb9(pitching.bb, ip),
                    'so9': BaseballStats.so9(pitching.so, ip)
                }
            )
            _datasets['dunn_list'].append(
                {
                    'year': year,
                    'dunn': BaseballStats.adam_dunn_pitcher(pitching.hr, pitching.bb, pitching.hbp, pitching.so, pitching.bfp)
                }
            )
        # HTML表示の場合かつ戻り値件数未満の場合は空行を追加
        if html:
            cnt_row = self.STATS_LIMIT - len(stats)
            while cnt_row > 0:
                year -= 1
                _datasets['whip_list'].append(
                    {
                        'year': year,
                        'whip': 0.0
                    }
                )
                _datasets['hr9_list'].append(
                    {
                        'year': year,
                        'hr9': 0.0,
                        'bb9': 0.0,
                        'so9': 0.0
                    }
                )
                _datasets['dunn_list'].append(
                    {
                        'year': year,
                        'dunn': 0.0
                    }
                )
                cnt_row -= 1
                if cnt_row == 0:
                    break
        return _datasets

    def get_home_value_pitcher(self, player, stats, salary):
        """
        Pitcher profile
        :param player: Player master model
        :param stats: Player stats model
        :param salary: Player salary model
        :return: pitcher profile(dict)
        """
        # statsから必要な値を修得
        w, l, so, er, ipo, year, teams = 0, 0, 0, 0, 0, 0, []
        if len(stats) > 0:
            pitching = stats[0]
            year = pitching.yearid
            w = pitching.w
            l = pitching.l
            so = pitching.so
            er = pitching.er
            ipo = pitching.ipouts
            teams.append(MlbDB.get_last_team(MlbDB.get_pitching(), year, pitching.playerid))

        # ipを計算
        ip = BaseballStats.ip(ipo)

        _prof = self._get_base_profile(player, year, teams, salary)
        _prof['position'] = POSITION_PITCHER.upper()
        _prof['win'] = w
        _prof['lose'] = l
        _prof['era'] = BaseballStats.era(er, ip)
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
        # statsから必要な値を修得
        hr, rbi, h, ab, year, teams = 0, 0, 0, 0, 0, []
        if len(stats) > 0:
            batter = stats[0]
            year = batter.yearid
            h = batter.h
            ab = batter.ab
            hr = batter.hr
            rbi = rbi + batter.rbi
            teams.append(MlbDB.get_last_team(MlbDB.get_batting(), year, batter.playerid))

        _prof = self._get_base_profile(player, year, teams, salary)
        _prof['position'] = POSITION_BATTER.upper()
        _prof['avg'] = BaseballStats.avg(h, ab)
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
            'age': Stats.calc_age(player.birthyear),
            'birthday': '%d/%d/%d' % (player.birthyear, player.birthmonth, player.birthday),
            'salary': Stats._calc_salary(salary),
            'country': player.birthcountry,
            'city': player.birthcity,
            'bats': player.bats,
            'throws': player.throws,
            'display_name': ' '.join([player.namefirst, player.namelast])

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
            sal = salary[0].salary
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

    @classmethod
    def exists_player(cls, firstname, lastname):
        """
        選手がいるかいないか
        :param firstname: Player's First name
        :param lastname: Player's Last name
        :return: True(exists) or False(not exists)
        """
        if MlbDB.player().filter(namefirst=firstname).filter(namelast=lastname).count() == 1:
            return True
        else:
            return False