
# Create your views here.


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from noball.settings import VIEW_ENCODE
from service.const import LEAGUES, POSITION_BATTER, POSITION_PITCHER
from mlb.form import SearchForm, PytagorasForm
from mlb.service.stats import Stats as StatsService
from mlb.models import Teams, Salaries
from mlb.models import Master as Player
from mlb.models import Battingtotal
from mlb.models import Pitchingtotal


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
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
        if Player.objects.filter(nameFirst=first).filter(nameLast=last).count() == 1:
            # 全画面共通のContext(PlayerModelの中身)
            context['player'] = self._get_player(first, last)
            # 成績情報(PlayerStatsModelの中身)
            context['stats'], context['pos'], context['Salaries'] = self._get_player_stats(context['player'].playerID)
        else:
            context['MENU_ENABLE'] = False
        return context

    def get_response_value(self, context):
        '''
        戻り値の編集
        野手or投手で呼び出し先を変える
        '''

        _content = {}
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
            return Player.objects.filter(nameFirst=first).filter(nameLast=last).get()

    def _get_player_stats(self, playerID):
        # batting, pitching両方のスタッツを取って多い方を出す。
        count_atbat = Battingtotal.objects.filter(playerID=playerID).count()
        count_pitch = Pitchingtotal.objects.filter(playerID=playerID).count()

        # 検索対象のモデルと戻り値
        if count_atbat > count_pitch:
            # Batter
            model = self._get_model_filter_player_order_by_year_desc(Battingtotal, playerID)
            pos = POSITION_BATTER
        else:
            # Pitcher
            model = self._get_model_filter_player_order_by_year_desc(Pitchingtotal, playerID)
            pos = POSITION_PITCHER
        salary = self._get_model_filter_player_order_by_year_desc(Salaries, playerID)

        return model, pos, salary

    def _get_model_filter_player_order_by_year_desc(self, model, player_id, before=3):
        """
        search model
        """
        # 年度の降順で最新のレコードを取得、年度ごとにDictに詰めて降順で返す
        rows = {}
        if model.objects.filter(playerID=player_id).order_by('-yearID').count() > 0:
            # 一番最後のシーズンの成績を取得(一行だけ)
            row = model.objects.filter(playerID=player_id).order_by('-yearID').all()[:1]
            # 最後のシーズンから過去3年分を取得、年度が一緒のモノはchunkする
            for m in model.objects.filter(playerID=player_id)\
                .filter(yearID__range=(row[0].yearID - before, row[0].yearID)).order_by('-yearID').all():
                if m.yearID not in rows:
                    rows[m.yearID] = []
                rows[m.yearID].append(m)
        # 年度の降順でsortし直す
        return sorted(rows.items(), key=lambda x: x[0], reverse=True)


class MlbBaseballException(Exception):
    pass


class TopView(BaseView):
    template_name = "%s/top.html" % (StatsService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        # TODO 多分何も出さない
        return context


class HomeView(PlayerView):
    template_name = "%s/home.html" % (StatsService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if 'player' in context:
            context['values'] = self.get_response_value(context)
        return context

    def _get_batter_content(self, player, player_stats, Salaries):
        # Serviceを呼び出す
        return self.service.get_home_value_batter(player, player_stats, Salaries)

    def _get_pitcher_content(self, player, player_stats, Salaries):
        # Serviceを呼び出す
        return self.service.get_home_value_pitcher(player, player_stats, Salaries)


class SabrView(PlayerView):
    template_name = "%s/sabr.html" % (StatsService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(SabrView, self).get_context_data(**kwargs)
        if 'player' in context:
            context['data'] = self.get_response_value(context)
        return context

    def _get_batter_content(self, player, player_stats, Salaries):
        # Serviceを呼び出す
        return self.service.get_sabr_value_batter(player, player_stats, Salaries)

    def _get_pitcher_content(self, player, player_stats, Salaries):
        # Serviceを呼び出す
        return self.service.get_sabr_value_pitcher(player, player_stats, Salaries)


class PythagorasView(BaseView):
    template_name = "%s/pythagoras.html" % (StatsService.SUB_DOMAIN)

    def get_context_data(self, **kwargs):
        context = super(PythagorasView, self).get_context_data(**kwargs)
        # TODO MAX_YEARを差し替え context['year'], context['league'], context['leagues'] = MAX_YEAR, LEAGUE_AL, LEAGUES
        teams = Teams.objects.filter(yearID=context['year']).filter(lgID=context['league']).order_by('divID', 'Rank')
        context['dataset'] = self.service.get_pythagoras_dataset(teams)
        return context


def _search(request, action):
    service = StatsService(VIEW_ENCODE)
    form = SearchForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data[StatsService.QUERY_KEY]
        names = name.lower().split()
        if len(names) == 2:
            # 件数チェック
            players = Player.objects.filter(nameFirst=names[0].capitalize()).filter(nameLast=names[1].capitalize())
        elif len(names) == 1:
            players = Player.objects.filter(nameFirst=names[0])
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
    if request.method == 'POST':
        return _search(request, 'player')


def stats_search(request):
    if request.method == 'POST':
        return _search(request, 'stats')


def sabr_search(request):
    if request.method == 'POST':
        return _search(request, 'sabr')


def pythagoras_search(request):
    """
    ピタゴラス勝率(Form検索)
    :param request: request object
    :return: html
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
            teams = Teams.objects.filter(yearID=context['year']).filter(lgID=context['league']).order_by('divID', 'Rank')
            context['dataset'] = service.get_pythagoras_dataset(teams)
            context['search_action'] = 'pythagoras_search'
        return render_to_response(
            template_html, context, context_instance=RequestContext(request)
        )
