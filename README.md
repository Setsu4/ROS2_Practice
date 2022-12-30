# mypkg

[![test](https://github.com/Setsu4/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Setsu4/mypkg/actions/workflows/test.yml)

ロボットシステム学講義内ROS2練習リポジトリ

* このリポジトリはROS2のパッケージです。
* このリポジトリではtalker,listenerと、talker_listener.launchという二つのノードを使用することができます。
* ROS2を未インストールの方は先にROS2のインストールをお願いします。
* ROS2をインストールしたら以下のURLをクローンして下さい。
```
$git clone https://github.com/Setsu4/mypkg.git
$cd mypkg
```

# talker,listener

このノードを使用するにはターミナルが２つ必要です。
talker側がcountupというトピックを通じて、16ビットの符号付整数型のメッセージを送り、listener側がそのメッセージを受信した順番通りにエディタに出力します。
終了する際は、無限ループする仕様になっているため強制的に終了してください。

## 実行例
以下ターミナル1をtalker側、ターミナル2をlistener側としています。

* talker側
```
$ ros2 run mypkg talker
```

* listener側
```
$ ros2 run mypkg listener
[INFO] [1672430132.605043900] [listener]: Listen: 1
[INFO] [1672430133.096196500] [listener]: Listen: 2
[INFO] [1672430133.596569000] [listener]: Listen: 3
[INFO] [1672430134.096543600] [listener]: Listen: 4
[INFO] [1672430134.596493700] [listener]: Listen: 5
[INFO] [1672430135.096559700] [listener]: Listen: 6
[INFO] [1672430135.596383300] [listener]: Listen: 7
[INFO] [1672430136.096230800] [listener]: Listen: 8
[INFO] [1672430136.596362200] [listener]: Listen: 9
[INFO] [1672430137.096485100] [listener]: Listen: 10
[INFO] [1672430137.596389500] [listener]: Listen: 11
...(以下省略)
```

# talker_listener.launch

talkerとlistenerの2つのノードを同時に立ち上げることができます。

## 実行例

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/setsu/.ros/log/2022-12-31-05-45-41-064938-SETSU-LAPTOP01-1546
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [1547]
[INFO] [listener-2]: process started with pid [1549]
[listener-2] [INFO] [1672433141.892012100] [listener]: Listen: 0
[listener-2] [INFO] [1672433142.383552500] [listener]: Listen: 1
[listener-2] [INFO] [1672433142.883232900] [listener]: Listen: 2
[listener-2] [INFO] [1672433143.383520500] [listener]: Listen: 3
[listener-2] [INFO] [1672433143.883274900] [listener]: Listen: 4
[listener-2] [INFO] [1672433144.383270000] [listener]: Listen: 5
[listener-2] [INFO] [1672433144.883252400] [listener]: Listen: 6
[listener-2] [INFO] [1672433145.383307300] [listener]: Listen: 7
[listener-2] [INFO] [1672433145.883410900] [listener]: Listen: 8
[listener-2] [INFO] [1672433146.383192500] [listener]: Listen: 9
[listener-2] [INFO] [1672433146.883256500] [listener]: Listen: 10
[listener-2] [INFO] [1672433147.383231400] [listener]: Listen: 11
...(以下省略)
```

# 動作確認済み環境

 * Ubuntu 22.04

# ライセンス

 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
 * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
 	* [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* © 2022 Setsu Ito
