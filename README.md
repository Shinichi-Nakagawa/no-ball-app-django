no-ball-app-django ~ のぼーる（野球）Djangoアプリケーション
=================

Lahman’s Baseball Database( http://www.seanlahman.com/baseball-archive/statistics/ )をMySQLで使うプロジェクトです。

## Description

Lahman’s Baseball Database Server、「no-ball-db-server」を用いたアプリケーションのサンプルです。

アプリケーションはDjangoで開発しました。	

このプロジェクトには、

 * 選手のプロフィールを表示
 * 選手のセイバーメトリクス指標を表示	
 * ピタゴラス勝率の算出と表示

上記の役割を果たすコードが含まれています。

メジャーリーグの選手やチームを分析・可視化する際に活用してもらえると幸いです。

## Demo

このプロジェクトを用いてできる事は以下のスライドおよび動画を参照ください。

なお、データベースは別のプロジェクトとして公開しています。

### スライド
<iframe src="//www.slideshare.net/slideshow/embed_code/39061157" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/shinyorke/python-39061157" title="Pythonではじめる野球プログラミング PyCon JP 2014 9/14 Talk Session" target="_blank">Pythonではじめる野球プログラミング PyCon JP 2014 9/14 Talk Session</a> </strong> from <strong><a href="//www.slideshare.net/shinyorke" target="_blank">Shinichi Nakagawa</a></strong> </div>

### 動画
http://youtu.be/7NS1CwzlFS8?list=UUxNoKygeZIE1AwZ_NdUCkhQ

## Requirement

このプロジェクトを適用する際は以下のアプリケーション・ライブラリが必要となります。

プロジェクトをCloneする前にご準備願います。

 * Python 3.x ※3.4を推奨 
 * pip https://pypi.python.org/pypi/pip

 Pythonおよびpipをインストール後、同梱されているrequirements.txtを使いライブラリのインストールを行ってください。

> pip install -r requirements.txt

## Usage

手っ取り早く動かしたい方は、Djangoのrunserverを用いると良いでしょう。

> python manage.py runserver

アプリケーションが起動したら、以下のURLを叩いてください

> http://localhost:8000/mlb

Top画面が開き、選手およびピタゴラス勝率の検索フォームが表示されます。

後はお好きな様に遊んでみてください。

## install

インストール手順です。利用環境(OS)は以下の要件を想定しています。

 * Mac OS X 10.9(Mavericks)またはMac OS X 10.10(Yosemite)

ここから先の説明は仮置きで、Project Root(=クローンする先)を以下のディレクトリとします。

 * /Users/Billy_Beane/Documents/no-ball-db-server

__"Billy_Beane"の部分をご自身の環境と置き換えて読んでください。__

#### no-ball-db-serverを設定

別プロジェクトとして公開しているDB Serverを設定します。

sourceは以下から入手してください。

https://github.com/Shinichi-Nakagawa/no-ball-db-server

上記リポジトリのREADME.mdを参考に、DB Serverを構築しましょう。

構築が完了したら、

> vagrant up

でサーバーを起動することを忘れずに！

#### クローンする先のディレクトリに移動

> cd /Users/Billy_Beane/Documents

#### プロジェクトをcloneする

> git clone git@github.com:Shinichi-Nakagawa/no-ball-app-django.git

#### setting.pyの内容を変更

setting.py内にあるDB(MySQL)ユーザーのパスワードを、DB Serverに合わせて書きなおしてください。

##### 対象のコード

https://github.com/Shinichi-Nakagawa/no-ball-app-django/blob/master/noball/noball/settings.py

##### 設定内容

「DATABASES」で検索、mlb データベースのパスワードを、appユーザーのパスワードに書き換えてください

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'noball.db'),                      # Or path to database file if using sqlite3.
    },
    'mlb': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sean_lahman',                      # Or path to database file if using sqlite3.
        'USER': 'app',
        __'PASSWORD': 'adam_dunn',__　←ココを書き換える
        'HOST': '192.168.33.10',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
```

これで、

> python manage.py runserver

上記コマンドで無事起動したらアプリケーションが使えるはずです！

## License

MIT License http://opensource.org/licenses/MIT

## Message

日本プロ野球、サッカー、etc...同じくスポーツデータをHackしたい方の参考になれば幸いです。

__好きな言語で好きなデータをHackしましょう！__