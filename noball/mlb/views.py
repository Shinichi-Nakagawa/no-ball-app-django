
# Create your views here.


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from noball.settings import VIEW_ENCODE
from service.const import CURRENT_SEASON_YEAR, LEAGUES, POSITION_BATTER, POSITION_PITCHER, LEAGUE_AL
from mlb.form import SearchForm, PytagorasForm
from mlb.service.stats import Stats as StatsService


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
        '''
        ページ情報を返す
        :param kwargs:
        :return:
        '''
        # Serviceのインスタンス
        self.service = StatsService(VIEW_ENCODE)
        # 共通処理（野手・投手共通の処理、DB検索など）
        context = super(TemplateView, self).get_context_data(**kwargs)
        # 固定値を取得
        context.update(self.service.get_base_context())
        return context


class PlayerView(BaseView):

    # 戻り値のキー
    KEY_STATS = 'stats'

    def get_context_data(self, **kwargs):
        # パラメータを取得
        first, last = "", ""
        if StatsService.QUERY_KEY in self.request.GET:
            name = self.request.GET[StatsService.QUERY_KEY]
            names = name.lower().split()
            first, last = names[0].capitalize(), names[1].capitalize()
        else:
            pass
        # 共通処理（野手・投手共通の処理、DB検索など）
        context = super(PlayerView, self).get_context_data(**kwargs)
        # 固定値を取得
        context.update(self.service.get_base_context())
        # 検索QUERYを保存
        context['query_name'] = name
        if StatsService.exists_player(first, last):
            # 全画面共通のContext(PlayerModelの中身)
            context['player'] = self._get_player(first, last)
            # 成績情報(PlayerStatsModelの中身)
            context['stats'], context['pos'], context['Salaries'] = self._get_player_stats(context['player'].playerid)
        else:
            context['MENU_ENABLE'] = False
        return context

    def get_response_value(self, context):
        """
        戻り値の編集
        野手or投手で呼び出し先を変える
        """

        if POSITION_BATTER == context['pos']:
            return self._get_batter_content(context['player'], context['stats'], context['Salaries'])
        elif POSITION_PITCHER == context['pos']:
            return self._get_pitcher_content(context['player'], context['stats'], context['Salaries'])
        else:
            raise MlbBaseballException()

    def _get_player(self, first, last):
        cache = {}  # TODO Memcache的なやつを入れる
        if "_".join([first, last]) in cache:
            # TODO キャッシュから返す
            pass
        else:
            # キャッシュに無かったらDBを検索
            return StatsService.get_player_by_first_name_last_name(first, last).get()

    def _get_player_stats(self, playerID):
        # batting, pitching両方のスタッツを取って多い方を出す。
        cnt_atbat = StatsService.count_by_player_id(StatsService.batting_total(), playerID)
        cnt_pitch = StatsService.count_by_player_id(StatsService.pitching_total(), playerID)

        # 検索対象のモデルと戻り値
        if cnt_atbat > cnt_pitch:
            # Batter
            model = StatsService.get_model_filter_player_order_by_year_desc(
                StatsService.batting_total(),
                playerID
            )
            pos = POSITION_BATTER
        else:
            # Pitcher
            model = StatsService.get_model_filter_player_order_by_year_desc(
                StatsService.pitching_total(),
                playerID
            )
            pos = POSITION_PITCHER
        salary = StatsService.get_model_filter_player_order_by_year_desc(
            StatsService.salaries_total(),
            playerID
        )

        return model, pos, salary


class MlbBaseballException(Exception):
    pass


class TopView(BaseView):
    template_name = "%s/top.html" % (StatsService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        # TODO 何も出さない
        return context


class HomeView(PlayerView):
    template_name = "%s/home.html" % (StatsService.SUB_DOMAIN, )

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if 'player' in context:
            context['values'] = self.get_response_value(context)
        return context

    def _get_batter_content(self, player, player_stats, salaries):
        """
        Batter情報取得
        :param player:
        :param player_stats:
        :param salaries:
        :return:
        """
        return self.service.get_home_value_batter(player, player_stats, salaries)

    def _get_pitcher_content(self, player, player_stats, salaries):
        """
        Pitcher情報取得
        :param player:
        :param player_stats:
        :param salaries:
        :return:
        """
        return self.service.get_home_value_pitcher(player, player_stats, salaries)


class SabrView(PlayerView):
    template_name = "%s/sabr.html" % (StatsService.SUB_DOMAIN, )

    def get_context_data(self, **kwargs):
        context = super(SabrView, self).get_context_data(**kwargs)
        if 'player' in context:
            context['data'] = self.get_response_value(context)
        return context

    def _get_batter_content(self, player, player_stats, salaries):
        # Serviceを呼び出す
        return self.service.get_sabr_value_batter(player, player_stats, salaries)

    def _get_pitcher_content(self, player, player_stats, salaries):
        # Serviceを呼び出す
        return self.service.get_sabr_value_pitcher(player, player_stats, salaries)


class PythagorasView(BaseView):
    template_name = "%s/pythagoras.html" % (StatsService.SUB_DOMAIN, )

    def get_context_data(self, **kwargs):
        context = super(PythagorasView, self).get_context_data(**kwargs)
        context['year'], context['league'], context['leagues'] = CURRENT_SEASON_YEAR, LEAGUE_AL, LEAGUES
        teams = StatsService.get_teams_by_yearid_lgid(context['year'], context['league'])
        context['dataset'] = self.service.get_pythagoras_dataset(teams)
        return context


def _search(request, action):
    '''
    検索
    :param request: Http Request objects
    :param action: 遷移先ページ
    :return: response
    '''
    service = StatsService(VIEW_ENCODE)
    form = SearchForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data[StatsService.QUERY_KEY]
        names = name.lower().split()
        if len(names) == 2:
            # 件数チェック
            players = StatsService.get_player_by_first_name_last_name(names[0].capitalize(), names[1].capitalize())
        elif len(names) == 1:
            players = StatsService.get_player_by_first_name(names[0].capitalize())
        else:
            raise MlbBaseballException()

        if players.count() == 1:
            # リダイレクト先設定
            url = '/%s/%s/?%s=%s' % (StatsService.SUB_DOMAIN, action, StatsService.QUERY_KEY, name)
            return HttpResponseRedirect(url)

        # 0件又は複数件
        context = service.get_base_context()
        context['MENU_ENABLE'] = False
        context[StatsService.QUERY_KEY] = name
        context['count'] = players.count()
        context['values'] = []
        context['title'] = ''
        context['action'] = action
        if action == 'player':
            context['search_action'] = 'search'
        else:
            context['search_action'] = '%s_search' % action


        template_html = '%s/%s.html' % (StatsService.SUB_DOMAIN, 'search_result')
        if players.count() > 1:
            # 候補選手を出してあげる
            for player in players:
                context['values'].append(player)

        if len(context['values']):
            context['result'] = True
        else:
            context['result'] = False

        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )
    else:
        # validateエラー
        # リダイレクト先設定
        template_html = '%s/%s.html' % (StatsService.SUB_DOMAIN, action)
        context = service.get_base_context()
        # 検索QUERYを保存
        context['query_name'] = ''
        context['error_message'] = u"検索ワード不正。"
        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )


def search(request):
    """
    検索(選手)
    :param request: http request
    :return: response
    """
    if request.method == 'POST':
        return _search(request, 'player')


def stats_search(request):
    """
    検索(Stats)
    :param request: http request
    :return: response
    """
    if request.method == 'POST':
        return _search(request, 'stats')


def sabr_search(request):
    """
    検索(SABR Metrics)
    :param request: http request
    :return: response
    """
    if request.method == 'POST':
        return _search(request, 'sabr')


def pythagoras_search(request):
    """
    ピタゴラス勝率(Form検索)
    :param request: http request
    :return: response
    """
    service = StatsService(VIEW_ENCODE)
    context = service.get_base_context()
    template_html = "%s/pythagoras.html" % (StatsService.SUB_DOMAIN)

    if request.method == 'POST':
        form = PytagorasForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            league = form.cleaned_data['league']
            context['year'], context['league'], context['leagues'] = year, league, LEAGUES
            teams = StatsService.get_teams_by_yearid_lgid(context['year'], context['league'])
            context['dataset'] = service.get_pythagoras_dataset(teams)
            context['search_action'] = 'pythagoras_search'
        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )
