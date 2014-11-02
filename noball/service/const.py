#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
serviceの定数クラス
"""
__author__ = 'Shinichi Nakagawa'

PLAYERS_NAME_DELI = " "
PLAYERS_PAGE_URL = 'http://www.baseball-reference.com/players/%(letter)s/'
PLAYERS_PAGE_URL_SUFIX_BATTER = "-bat.shtml"
PLAYERS_PAGE_URL_SUFIX_PITCHER = "-pitch.shtml"
PLAYERS_PAGE_URL_SUFIX_REPLACE = ".shtml"

LEAGUE_AL = 'AL'
LEAGUE_NL = 'NL'
LEAGUES = (LEAGUE_AL, LEAGUE_NL)
LEAGUE_TUPLES = (
    (LEAGUE_AL, LEAGUE_AL),
    (LEAGUE_NL, LEAGUE_NL)
)

# Position FLG
POSITION_PITCHER = "p"
POSITION_BATTER = "b"

# ポジション辞書(Key:BRFの名称 Value:略称)
POSITION_DICT = {
    'Pitcher': 'P',  # 投手
    'SP': 'SP',  # 先発
    'RP': 'RP',  # リリーフ
    'CL': 'CL',  # 抑え
    'Catcher': 'C',  # 捕手
    'First Baseman': '1B',  # 一塁
    'Second Baseman': '2B',  # 二塁
    'Third Baseman': '3B',  # 三塁
    'Shortstop': 'SS',  # 遊撃手
    'Leftfielder': 'LF',  # 左翼
    'Centerfielder': 'CF',  # 中堅
    'Rightfielder': 'RF',  # 右翼
    'Outfielder': 'OF',  # 外野手全般
    'Designated Hitter': 'DH',  # 指名打者
    'Pinch Hitter': 'PH',  # 代打専門
}

# 右/左/両
HANDS_RIGHT = 'Right'
HANDS_LEFT = 'Left'
BATTING_SWITCH = 'Both'
