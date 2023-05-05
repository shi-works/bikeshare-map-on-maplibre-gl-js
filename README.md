# bikeshare-map
## Public Website
- https://shi-works.github.io/bikeshare-map/

## データの取得
### gbfs_station_dl.py
- pythonで下記の公共交通オープンデータセンターよりGBFS形式のデータ（station_information.json）を取得します。  
[ドコモ・バイクシェア](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/f114f7d1-11c8-4f03-98e1-2a6d2fd53e2e)  
URL: `https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json`  
[HELLOCYCLING](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-openstreet/resource/d45e9650-b243-4f5a-bda6-c2b0cb61e8a3)  
URL: `https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json`
### 取得結果
#### ドコモ・バイクシェア（東京のみ）
`https://github.com/shi-works/bikeshare-map/blob/main/data/docomo-cycle-tokyo_station.csv`
#### HELLOCYCLING
`https://github.com/shi-works/bikeshare-map/blob/main/data/hellocycling_station.csv`  

### ※CSVからGeoJSONへの変換にはQGISを使用します。
#### ドコモ・バイクシェア（東京のみ）
`https://github.com/shi-works/bikeshare-map/blob/main/data/docomo-cycle-tokyo_station.geojson`
#### ドコモ・バイクシェア（東京以外）
- ドコモ・バイクシェア（東京以外）は[ドコモ・バイクシェア](https://docomo-cycle.jp/)の公式サイトよりkmlを取得し、GeoJSONに変換後、マージしたデータになります。  
`https://github.com/shi-works/bikeshare-map/blob/main/data/docomo-cycle_station.geojson`
#### HELLOCYCLING
`https://github.com/shi-works/bikeshare-map/blob/main/data/hellocycling_station.geojson`  

## ライセンス
本データセットはCC-BY-4.0で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは公共交通オープンデータのドコモ・バイクシェア及びHELLOCYCLINGのシェアサイクルデータ（GBFS形式）を加工して作成したものです。本データセットの使用・加工にあたっては、[公共交通オープンデータセンター利用規約](https://developer.odpt.org/terms/center_use_rules.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
