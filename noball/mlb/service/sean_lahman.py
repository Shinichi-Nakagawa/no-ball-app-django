#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

from mlb.models import Master as Player
from mlb.models import Battingtotal, Pitchingtotal, Salariestotal, Teams


class SeanLahmanDB(object):

    # データベースを指定
    DATABASE_READ_FOR = 'mlb'
    DATABASE_WRITE_FOR = 'mlb'

    @classmethod
    def _read_model(cls, model, database):
        """
        DB検索
        :param model: Django Model
        :param database: using database
        :return: model
        """
        return model.objects.using(database)

    @classmethod
    def teams(cls, database=DATABASE_READ_FOR):
        """
        球団モデル
        :param database: using database(default: DATABASE_READ_FOR)
        :return: model
        """
        return SeanLahmanDB._read_model(Teams, database)

    @classmethod
    def salaries_total(cls, database=DATABASE_READ_FOR):
        """
        年俸モデル
        :param database: using database(default: DATABASE_READ_FOR)
        :return: model
        """
        return SeanLahmanDB._read_model(Salariestotal, database)

    @classmethod
    def pitching_total(cls, database=DATABASE_READ_FOR):
        """
        投手成績モデル
        :param database: using database(default: DATABASE_READ_FOR)
        :return: model
        """
        return SeanLahmanDB._read_model(Pitchingtotal, database)

    @classmethod
    def batting_total(cls, database=DATABASE_READ_FOR):
        """
        打撃成績モデル
        :param database: using database(default: DATABASE_READ_FOR)
        :return: model
        """
        return SeanLahmanDB._read_model(Battingtotal, database)

    @classmethod
    def player(cls, database=DATABASE_READ_FOR):
        """
        選手モデル
        :param database: using database(default: DATABASE_READ_FOR)
        :return: model
        """
        return SeanLahmanDB._read_model(Player, database)

    @classmethod
    def get_teams_by_yearid_lgid(cls, yearid, lgid):
        """
        年度とLEAGUEを指定して球団リストを取得
        :param yearid: 年度
        :param lgid: LEAGUE ID
        :return: Team List
        """
        return SeanLahmanDB.teams().filter(yearid=yearid).filter(lgid=lgid).order_by('divid', 'rank')

    @classmethod
    def get_model_filter_player_order_by_year_desc(cls, model, playerid, limit=1):
        """
        選手に紐づくモデルを年度の降順で取得
        :param model: 対象モデル(Batting, Pitching, Salary, etc...)
        :param playerid: 選手ID(PlayerのUNIQUE KEY)
        :param limit: 取得件数
        :return: model list
        """
        return model.filter(playerid=playerid).order_by('-yearid').all()[:limit]

    @classmethod
    def count_by_player_id(cls, model, playerid):
        """
        選手IDでの検索件数
        :param model: 対象モデル(Batting, Pitching, Salary, etc...)
        :param playerid: 選手ID(PlayerのUNIQUE KEY)
        :return: count
        """
        return model.filter(playerid=playerid).count()

    @classmethod
    def get_player_by_first_name_last_name(cls, first_name, last_name):
        """
        選手検索(姓名指定)
        :param first_name: Player's First name
        :param last_name: Player's Last name
        :return: Player's List
        """
        return SeanLahmanDB.player().filter(namefirst=first_name).filter(namelast=last_name)

    @classmethod
    def get_player_by_first_name(cls, first_name):
        """
        選手検索(First Nameのみ)
        :param first_name: Player's First name
        :return: Player's List
        """
        return SeanLahmanDB.player().filter(namefirst=first_name)
