# Line Notify 使用簡介

## 關於唯客學院

* [唯客學院網址](https://www.vcdemy.com)
* [唯客學院粉絲專頁](https://www.facebook.com/vcdemy/)
* [唯客學院線上教學](https://vcdemy.teachable.com)

## 教學影片

* [Line Notify 使用簡介](https://www.youtube.com/playlist?list=PLj4JWjo5dOC4ipFy5ODaMXsMYcBpZOp45)

## 課程內容

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/victorgau/khpy_linenotify_intro/)

* Line Notify簡介
* 如何取得Token？
* 如何使用 Line Notify 傳送訊息？
* 如何使用 Line Notify 傳送貼紙？
* 如何使用 Line Notify 傳送圖片？
* 如何定期發送訊息？

## 下載`linenotify.py`

我們寫好了一個`linenotify.py`模組，方便大家使用。

在 colab 或 jupyter lab/notebook 中，可以使用底下的指令下載`linenotify.py`模組。

如果可以執行 wget 指令，請執行：
```bash
!wget https://raw.githubusercontent.com/vcdemy/linenotify/main/py/linenotify.py
```

如果可以執行 curl 指令，請執行：
```bash
!curl -o linenotify.py https://raw.githubusercontent.com/vcdemy/linenotify/main/py/linenotify.py
```

## 相關連結

* [Line Notify Help](https://help2.line.me/line_notify/web/pc?lang=zh-Hant)
* [取得 Line Notify Token](https://notify-bot.line.me/en/)
* [Line Notify API Document](https://notify-bot.line.me/doc/en/)
* [標準 Sticker List](misc/sticker_list.pdf)
* [Line Notify 官方文件上的貼紙連結](https://developers.line.biz/en/docs/messaging-api/sticker-list/#send-sticker)
* [schedule](https://pypi.org/project/schedule/)