import requests
import json
import os

# 抓取九巴到站資料 (以 89C 為例)
def get_bus_eta(route, stop_seq):
    try:
        url = f"https://data.etabus.gov.hk/v1/transport/kmb/route-eta/{route}/{stop_seq}"
        res = requests.get(url).json()
        return res.get('data', [])
    except:
        return []

# 抓取天文台農曆 (直接簡化為邏輯)
# 注意：為求穩定，GitHub Actions 內可直接用計算程式

data = {
    "bus_89c": get_bus_eta("89C", "1"),
    "timestamp": os.popen("date").read().strip()
}

with open("data.json", "w") as f:
    json.dump(data, f)
