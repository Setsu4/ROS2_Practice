# mypkg

[![test](https://github.com/Setsu4/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Setsu4/mypkg/actions/workflows/test.yml)

ロボットシステム学講義内ROS2練習リポジトリ

* このリポジトリはROS2のパッケージです。
* このリポジトリではtalker,listener(mypkgファイル内)と、talker_listener.launch(launchファイル内)という二つのノードを使用することができます。
* ROS2を未インストールの方は先にROS2のインストールをお願いします。
* ROS2をインストールしたら以下のURLをクローンして下さい。
```
$git clone https://github.com/Setsu4/mypkg.git
$cd mypkg
```

# talker,listener

このノードを使用するにはターミナルが２つ必要です。
talker側がcountupというトピックを通じて、16ビットの符号付整数型のメッセージを送り、listener側がそのメッセージを受信した順番通りにエディタに出力します。
修了する際は、無限ループする仕様になっているため強制的に終了してください。

## 実行例
以下ターミナル1をtalker側、ターミナル2をlistener側としています。

* talker側
```
$ ros2 run mypkg talker
```

* listener側
```
$ ros2 run mypkg listener
```
