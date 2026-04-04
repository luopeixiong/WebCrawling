import time
import requests
import json
from urllib.parse import urlparse
import execjs
import hashlib
from hashlib import md5



headers = {
    # "x-s": "",
    # "x-s-common": "",
    # "x-t": "",
}
cookies = {
    # 不给你看
}
url = "aHR0cHM6Ly9lZGl0aC54aWFvaG9uZ3NodS5jb20vYXBpL3Nucy93ZWIvdjEvaG9tZWZlZWQ="
data = {
    "cursor_score": "",
    "num": 43,
    "refresh_type": 1,
    "note_index": 41,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed.fashion_v3",
    "search_key": "",
    "need_num": 18,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": False
}
data = json.dumps(data, separators=(',', ':'))

with open('x-s_4.3.3.js', 'r', encoding='utf-8') as fp:
    jscode = fp.read()
    ctx = execjs.compile(jscode)
    path = urlparse(url).path
    arg1 = path + data
    arg2 = md5(arg1.encode("utf-8")).hexdigest()
    arg3 = md5(path.encode("utf-8")).hexdigest()
    t = int(time.time() * 1000)
    a1 = cookies['a1']

    X_S = ctx.call('get_XS', arg1, arg2, arg3, t, a1)
    X_S_Common = ctx.call('get_XS_Common', t, a1)
    print(X_S)
    print(X_S_Common)

    headers["x-t"] = str(t)
    headers["x-s"] = X_S
    headers["x-s-common"] = X_S_Common

    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.text)
    print(response)