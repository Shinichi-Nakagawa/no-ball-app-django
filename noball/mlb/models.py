# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Allstarfull(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    gamenum = models.IntegerField(db_column='gameNum')  # Field name made lowercase.
    gameid = models.CharField(db_column='gameID', max_length=12, blank=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    gp = models.IntegerField(db_column='GP', blank=True, null=True)  # Field name made lowercase.
    startingpos = models.IntegerField(db_column='startingPos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllstarFull'


class Appearances(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    g_all = models.IntegerField(db_column='G_all', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.IntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    g_defense = models.IntegerField(db_column='G_defense', blank=True, null=True)  # Field name made lowercase.
    g_p = models.IntegerField(db_column='G_p', blank=True, null=True)  # Field name made lowercase.
    g_c = models.IntegerField(db_column='G_c', blank=True, null=True)  # Field name made lowercase.
    g_1b = models.IntegerField(db_column='G_1b', blank=True, null=True)  # Field name made lowercase.
    g_2b = models.IntegerField(db_column='G_2b', blank=True, null=True)  # Field name made lowercase.
    g_3b = models.IntegerField(db_column='G_3b', blank=True, null=True)  # Field name made lowercase.
    g_ss = models.IntegerField(db_column='G_ss', blank=True, null=True)  # Field name made lowercase.
    g_lf = models.IntegerField(db_column='G_lf', blank=True, null=True)  # Field name made lowercase.
    g_cf = models.IntegerField(db_column='G_cf', blank=True, null=True)  # Field name made lowercase.
    g_rf = models.IntegerField(db_column='G_rf', blank=True, null=True)  # Field name made lowercase.
    g_of = models.IntegerField(db_column='G_of', blank=True, null=True)  # Field name made lowercase.
    g_dh = models.IntegerField(db_column='G_dh', blank=True, null=True)  # Field name made lowercase.
    g_ph = models.IntegerField(db_column='G_ph', blank=True, null=True)  # Field name made lowercase.
    g_pr = models.IntegerField(db_column='G_pr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appearances'


class Awardsmanagers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=25)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    tie = models.CharField(max_length=1, blank=True)
    notes = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'AwardsManagers'


class Awardsplayers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    tie = models.CharField(max_length=1, blank=True)
    notes = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'AwardsPlayers'


class Awardssharemanagers(models.Model):
    awardid = models.CharField(db_column='awardID', max_length=25)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    pointswon = models.IntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.IntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.IntegerField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwardsShareManagers'


class Awardsshareplayers(models.Model):
    awardid = models.CharField(db_column='awardID', max_length=25)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    pointswon = models.FloatField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.IntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.FloatField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AwardsSharePlayers'


class Batting(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.IntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    g_old = models.IntegerField(db_column='G_old', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Batting'


class Battingpost(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=10)
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BattingPost'


class Battingtotal(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.IntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.
    g_old = models.IntegerField(db_column='G_old', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BattingTotal'


class Fielding(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=2)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.FloatField(db_column='ZR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fielding'


class Fieldingof(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    glf = models.IntegerField(db_column='Glf', blank=True, null=True)  # Field name made lowercase.
    gcf = models.IntegerField(db_column='Gcf', blank=True, null=True)  # Field name made lowercase.
    grf = models.IntegerField(db_column='Grf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingOF'


class Fieldingpost(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    round = models.CharField(max_length=10)
    pos = models.CharField(db_column='POS', max_length=2)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.IntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingPost'


class Halloffame(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField()
    votedby = models.CharField(db_column='votedBy', max_length=64)  # Field name made lowercase.
    ballots = models.IntegerField(blank=True, null=True)
    needed = models.IntegerField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    inducted = models.CharField(max_length=1, blank=True)
    category = models.CharField(max_length=20, blank=True)
    needed_note = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'HallOfFame'


class Managers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9, blank=True)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    inseason = models.IntegerField()
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(blank=True, null=True)
    plyrmgr = models.CharField(db_column='plyrMgr', max_length=1, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Managers'


class Managershalf(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    inseason = models.IntegerField(blank=True, null=True)
    half = models.IntegerField()
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ManagersHalf'


class Master(models.Model):
    playerid = models.CharField(db_column='playerID', primary_key=True, max_length=9)  # Field name made lowercase.
    hofid = models.CharField(db_column='hofID', max_length=10, blank=True)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.IntegerField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.CharField(db_column='birthCountry', max_length=50, blank=True)  # Field name made lowercase.
    birthstate = models.CharField(db_column='birthState', max_length=2, blank=True)  # Field name made lowercase.
    birthcity = models.CharField(db_column='birthCity', max_length=50, blank=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.IntegerField(db_column='deathMonth', blank=True, null=True)  # Field name made lowercase.
    deathday = models.IntegerField(db_column='deathDay', blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.CharField(db_column='deathCountry', max_length=50, blank=True)  # Field name made lowercase.
    deathstate = models.CharField(db_column='deathState', max_length=2, blank=True)  # Field name made lowercase.
    deathcity = models.CharField(db_column='deathCity', max_length=50, blank=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=50, blank=True)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=50, blank=True)  # Field name made lowercase.
    namenote = models.CharField(db_column='nameNote', max_length=255, blank=True)  # Field name made lowercase.
    namegiven = models.CharField(db_column='nameGiven', max_length=255, blank=True)  # Field name made lowercase.
    namenick = models.CharField(db_column='nameNick', max_length=255, blank=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bats = models.CharField(max_length=1, blank=True)
    throws = models.CharField(max_length=1, blank=True)
    debut = models.CharField(max_length=10, blank=True)
    finalgame = models.CharField(db_column='finalGame', max_length=10, blank=True)  # Field name made lowercase.
    college = models.CharField(max_length=50, blank=True)
    lahman40id = models.CharField(db_column='lahman40ID', max_length=9, blank=True)  # Field name made lowercase.
    lahman45id = models.CharField(db_column='lahman45ID', max_length=9, blank=True)  # Field name made lowercase.
    retroid = models.CharField(db_column='retroID', max_length=9, blank=True)  # Field name made lowercase.
    holtzid = models.CharField(db_column='holtzID', max_length=9, blank=True)  # Field name made lowercase.
    bbrefid = models.CharField(db_column='bbrefID', max_length=9, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Master'


class Pitching(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.IntegerField()
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pitching'


class Pitchingpost(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=10)
    teamid = models.CharField(db_column='teamID', max_length=3, blank=True)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2, blank=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.FloatField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PitchingPost'


class Pitchingtotal(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.IntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.IntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.IntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.IntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PitchingTotal'


class Salaries(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Salaries'


class Salariestotal(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SalariesTotal'


class Schools(models.Model):
    schoolid = models.CharField(db_column='schoolID', primary_key=True, max_length=15)  # Field name made lowercase.
    schoolname = models.CharField(db_column='schoolName', max_length=255, blank=True)  # Field name made lowercase.
    schoolcity = models.CharField(db_column='schoolCity', max_length=55, blank=True)  # Field name made lowercase.
    schoolstate = models.CharField(db_column='schoolState', max_length=55, blank=True)  # Field name made lowercase.
    schoolnick = models.CharField(db_column='schoolNick', max_length=55, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schools'


class Schoolsplayers(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=9)  # Field name made lowercase.
    schoolid = models.CharField(db_column='schoolID', max_length=15)  # Field name made lowercase.
    yearmin = models.IntegerField(db_column='yearMin', blank=True, null=True)  # Field name made lowercase.
    yearmax = models.IntegerField(db_column='yearMax', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchoolsPlayers'


class Seriespost(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=5)
    teamidwinner = models.CharField(db_column='teamIDwinner', max_length=3, blank=True)  # Field name made lowercase.
    lgidwinner = models.CharField(db_column='lgIDwinner', max_length=2, blank=True)  # Field name made lowercase.
    teamidloser = models.CharField(db_column='teamIDloser', max_length=3, blank=True)  # Field name made lowercase.
    lgidloser = models.CharField(db_column='lgIDloser', max_length=2, blank=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SeriesPost'


class Teams(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    franchid = models.CharField(db_column='franchID', max_length=3, blank=True)  # Field name made lowercase.
    divid = models.CharField(db_column='divID', max_length=1, blank=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ghome = models.IntegerField(db_column='Ghome', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', max_length=1, blank=True)  # Field name made lowercase.
    wcwin = models.CharField(db_column='WCWin', max_length=1, blank=True)  # Field name made lowercase.
    lgwin = models.CharField(db_column='LgWin', max_length=1, blank=True)  # Field name made lowercase.
    wswin = models.CharField(db_column='WSWin', max_length=1, blank=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    ha = models.IntegerField(db_column='HA', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    bba = models.IntegerField(db_column='BBA', blank=True, null=True)  # Field name made lowercase.
    soa = models.IntegerField(db_column='SOA', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    fp = models.FloatField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True)
    park = models.CharField(max_length=255, blank=True)
    attendance = models.IntegerField(blank=True, null=True)
    bpf = models.IntegerField(db_column='BPF', blank=True, null=True)  # Field name made lowercase.
    ppf = models.IntegerField(db_column='PPF', blank=True, null=True)  # Field name made lowercase.
    teamidbr = models.CharField(db_column='teamIDBR', max_length=3, blank=True)  # Field name made lowercase.
    teamidlahman45 = models.CharField(db_column='teamIDlahman45', max_length=3, blank=True)  # Field name made lowercase.
    teamidretro = models.CharField(db_column='teamIDretro', max_length=3, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teams'


class Teamsfranchises(models.Model):
    franchid = models.CharField(db_column='franchID', primary_key=True, max_length=3)  # Field name made lowercase.
    franchname = models.CharField(db_column='franchName', max_length=50, blank=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True)
    naassoc = models.CharField(db_column='NAassoc', max_length=3, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamsFranchises'


class Teamshalf(models.Model):
    yearid = models.IntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.CharField(db_column='lgID', max_length=2)  # Field name made lowercase.
    teamid = models.CharField(db_column='teamID', max_length=3)  # Field name made lowercase.
    half = models.CharField(db_column='Half', max_length=1)  # Field name made lowercase.
    divid = models.CharField(db_column='divID', max_length=1, blank=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', max_length=1, blank=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamsHalf'
