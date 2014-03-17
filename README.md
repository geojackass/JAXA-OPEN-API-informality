JAXA-OPEN-API-informality
=========================

俺がJAXA-OPEN-APIのデータを使う練習するためのリポジトリ。堂々と公開している非公式なページ

</br>
<div align="right">20140317大友翔一</div>

####最重要確認事項　「ウェブブラウザで表示できること」


- githubに公開されているリポジトリをクローンした。

```
git clone git://github.com/JAXA-OPEN-API/example_api
```
- 作業後にディレクトリ内容を確認した。
	- example_api/client/sample03.htmlに実行権限がないことが確認された。

<img src=sc2014-03-17d.png>

- 実行権限を付与した。


```
chmod +x sample003.html
```

<img src=sc2014-03-17e.png>

- firefoxで表示した。

	- sample001.html<img src=sc2014-03-17a.png>
	</br>
	- sample002.html<img src=sc2014-03-17b.png>
	</br>
	- sample003.html<img src=sc2014-03-17c.png>

### 通常のweb APIのリクエストを行う

#### 指定地点の物理量を取得する

- request format xml

```
https://joa.epi.bz/api/prcavg?token=KOISURU-WAKUSEI_ver2&date=2012-08-01&lat=30.2&lon=130.5
```

<img src=open-api_get001a.png>

- request format JSON


```
https://joa.epi.bz/api/prcavg?token=KOISURU-WAKUSEI_ver2&date=2012-08-01&lat=30.2&lon=130.5&format=JSON
```

<img src=open-api_get002a.png>


#### 指定範囲の物理量をすべて取得する 

- request format xml

```
https://joa.epi.bz/api/prcall?token=KOISURU-WAKUSEI_ver2&date=2012-08-01&lat=30.2&lon=130.5
```

<img src=open-api_get003a.png>

- request format JSON


```
https://joa.epi.bz/api/prcall?token=KOISURU-WAKUSEI_ver2&date=2012-08-01&lat=30.2&lon=130.5&format=JSON
```
<img src=open-api_get004a.png>
