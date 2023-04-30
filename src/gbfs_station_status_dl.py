import requests
import pandas as pd
from io import StringIO
import datetime
import time


def fetch_data_and_save_csv():

    # 現在の日時を取得し、指定の形式に変換
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M")

    # hellocycling
    # URLへアクセスしてデータを取得
    url_h = requests.get(
        "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_status.json")

    text = url_h.text

    # 変換したいJSONファイルを読み込む
    df_h = pd.read_json(StringIO(text))
    # print(df_h.head())

    # ネスト（入れ子）構造になっている"data"という項目を展開する
    df_h_json = pd.json_normalize(df_h['data'][0])

    # JSONをCSVへ変換して文字コードをutf8で出力
    output_h_filename = f"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\hellocycling\hellocycling_station_status_{current_datetime}.csv"

    df_h_json.to_csv(output_h_filename, encoding='utf8', index=False)

    # docomo-cycle-tokyo
    # URLへアクセスしてデータを取得
    url_d = requests.get(
        "https://api-public.odpt.org/api/v4/gbfs/docomo-cycle-tokyo/station_status.json")

    text = url_d.text

    # 変換したいJSONファイルを読み込む
    df_d = pd.read_json(StringIO(text))
    # print(df_d.head())

    # ネスト（入れ子）構造になっている"data"という項目を展開する
    df_d_json = pd.json_normalize(df_d['data'][0])

    # JSONをCSVへ変換して文字コードをutf8で出力
    output_d_filename = f"D:\交通データ\公共交通オープンデータセンター\シェアサイクルデータ\csv\docomo-cycle-tokyo\docomo-cycle-tokyo_station_status_{current_datetime}.csv"

    df_d_json.to_csv(output_d_filename, encoding='utf8', index=False)

    print(current_datetime + ':処理終了')


# 処理開始日時
start_datetime = datetime.datetime(2023, 4, 30, 19, 20)

# 処理終了日時
end_datetime = datetime.datetime(2023, 4, 30, 20, 20)

# 現在時刻が開始日時になるまで待機
while datetime.datetime.now() < start_datetime:
    time.sleep(1)

while datetime.datetime.now() <= end_datetime:
    fetch_data_and_save_csv()
    time.sleep(300)  # 30分（1800秒）ごとにデータを取得
