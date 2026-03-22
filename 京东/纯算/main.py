import time
import execjs
from curl_cffi import requests
import json
import re
import hashlib


def get_tk(fp, expandParams):
    headers = {
        # 不给你看
    }
    url = "aHR0cHM6Ly9jYWN0dXMuamQuY29tL3JlcXVlc3RfYWxnbw"
    data = {
        "version": "5.3",
        "fp": fp,
        "appId": "b5216",
        "timestamp": int(time.time() * 1000),
        "platform": "web",
        "expandParams": expandParams,
        "fv": "h5_file_v5.3.0",
        "localTk": localTk
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    json_data = json.loads(response.text)
    tk = json_data['data']['result']['tk']
    algo = json_data['data']['result']['algo']
    rd = re.search(r"rd='(.*?)'", algo).group(1)
    return tk, rd


def get_info(fp, tk, rd, ctx):
    headers = {
        # 不给你看
    }
    cookies = {
        # 不给你看
    }
    url = "https://api.m.jd.com/"
    params = {
        # 不给你看
    }

    timestamp = int(time.time() * 1000)
    body_sha256 = hashlib.sha256(params["body"].encode('utf-8')).hexdigest()
    params_str = f"appid:www-jd-com&body:{body_sha256}&client:pc&clientVersion:1.0.0&functionId:pc_home_feed&t:{timestamp}"
    h5st = ctx.call('get_h5st', fp, tk, params_str, rd)

    params["h5st"] = h5st
    params["t"] = str(timestamp)
    params["uuid"] = cookies["__jda"]

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.text)
    print(response)





if __name__ == '__main__':
    with open('get_h5st.js', 'r', encoding='utf-8') as doc:
        jscode = doc.read()
        ctx = execjs.compile(jscode)
        fp = ctx.call('get_fingerprint')
        localTk = ctx.call('get_LocalTK', fp)
        expandParams = ctx.call('get_expandParams', fp)
        tk, rd = get_tk(fp, expandParams)

        get_info(fp, tk, rd, ctx)




