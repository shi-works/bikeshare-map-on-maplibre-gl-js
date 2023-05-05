# bikeshare-map
## Public Website
- https://shi-works.github.io/bikeshare-map/
## データの取得
### gbfs_station_dl.py
- pythonで下記の公共交通オープンデータセンターよりGBFS形式のデータ（以下、station_information.json）を取得します。  
[ドコモ・バイクシェア](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-d-bikeshare/resource/f114f7d1-11c8-4f03-98e1-2a6d2fd53e2e)  
URL: `https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_information.json`  
[HELLOCYCLING](https://ckan.odpt.org/dataset/c_bikeshare_gbfs-openstreet/resource/d45e9650-b243-4f5a-bda6-c2b0cb61e8a3)  
URL: `https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json`
### 取得結果
#### ドコモ・バイクシェア
`https://github.com/shi-works/bikeshare-map/blob/main/data/docomo-cycle-tokyo_station.csv`
#### HELLOCYCLING
`https://github.com/shi-works/bikeshare-map/blob/main/data/hellocycling_station.csv`  
※CSVからGeoJSONへの変換にはQGISを使用します。
