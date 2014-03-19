#! usr/bin/env python
#! -*-coding: utf-8-*-
#author@Shoichi Otomo

import urllib2

url = 'https://joa.epi.bz/api/prcavg?token=aaa&date=2012-08-01&lat=30.2&lon=130.5'

response = urllib2.urlopen(url)
the_page = response.read()

print the_page

//TODO 入力した値を当日の値として、前日と前々日の値も取得する。
//TODO 取得するデータと紐付く座標値点の値の入力方法は、要考する。
//TODO 取得した座標値点の値を。時間区間で合算する。
