# import requests
from curl_cffi import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.jd.com/",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Microsoft Edge\";v=\"145\", \"Chromium\";v=\"145\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
cookies = {
    "jcap_dvzw_fp": "EB4YR6U0I2F8Mv8ggQ0y4pKb_jn-Y5aBnKvagQl8udi9nr_7HFYnWo0BsXFEgrva6rx_tPHWnz_7qqTF5giq3g==",
    "shshshfpa": "3e3a3d2c-f2df-3936-f615-09e8cdcc6105-1749387579",
    "shshshfpx": "3e3a3d2c-f2df-3936-f615-09e8cdcc6105-1749387579",
    "__jdu": "1772111101436759769482",
    "areaId": "19",
    "TrackID": "19bPlthQo3YaVLYaj2EVNsDeSSgKamuTLgKAswbpWJn7Mc4QjczUWVpEXRzq3WiJi6ABbTzpO9kjJPr2WIUTkLRdm7gkUgzQwMpSmVaKPHd61zkjcM9oNK1Ou2vtnuUH1",
    "light_key": "AASBKE7rOxgWQziEhC_QY6yafIpJ9ljAJsoIIcp2ddpiy8sL_BvX_QKxS15I9wTWOsCvIM7x",
    "pinId": "vRoE5IXBssareUFhCsM7yQ",
    "pin": "jd_ZKWQHSSvWXPj",
    "unick": "g6mjxzutq5zw50",
    "ceshi3.com": "000",
    "_tp": "y9jSsp13CoQiiDdK9A0fcg%3D%3D",
    "_pst": "jd_ZKWQHSSvWXPj",
    "ipLoc-djd": "19-1601-50258-129167",
    "jsavif": "1",
    "mt_xid": "V2_52007VwMUVF5YUlofSBlZB2AFFlpbX1pfFkopD1A1UxBSCVhOXBpAGUAAZgIRTlRfUAkDS0pdVWABQFRYUFsIL0oYXwJ7AhFOXl5DWR5CHV0OYgEiUG1YYl0ZSh1UB24FG1BZaFFcHUo%3D",
    "3AB9D23F7A4B3CSS": "jdd03BZVE6BDBQMIRQWOFO24NBCB5NCPSFEZQI2LWATBCLZLCUWWX23CFYHLJ35CPKHSC62NLZB4NKJIH3YKUOZCBTFALB4AAAAM4T4YRHRAAAAAADQDUHAZ4XKLRTEX",
    "_gia_d": "1",
    "wlfstk_smdl": "cyhxa2lpswkin3lx1euqk9pf2o5jnig0",
    "unpl": "JF8EALJnNSttX0lVAxhSG0cVT18BW1kPHB8CazABA1paGAAAHwtMERd7XlVdWhRKFB9sYRRXXVNKVg4YASsSEXteU11bD00VB2xXXAQDGhUQR09SWEBJJVpWX1kLSR4KbmMHZG1bS2QFGjIbFBZIXVReXQlLEgFoYQFcW19DUQwYMhoiF3ttZFddAEoUBl9mNVVtGh8IDBsDGhoQBl1SWF4ISxcDbmcAVlpeT1wDHAoeGxN7XGRd",
    "__jdv": "232945309|haosou-search|t_262767352_haosousearch|cpc|63052388053_0_63072a1d453d456f905f5f63be458f26|1772197397657",
    "3AB9D23F7A4B3C9B": "BZVE6BDBQMIRQWOFO24NBCB5NCPSFEZQI2LWATBCLZLCUWWX23CFYHLJ35CPKHSC62NLZB4NKJIH3YKUOZCBTFALB4",
    "__jda": "76161171.1772111101436759769482.1772111101.1772196567.1772197398.4",
    "__jdc": "76161171",
    "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu17S7myJs3tR5l7H7UWKDIxOhvFqh01eBEN-0v1wh6sXv2_H3jjaBFCCAxR2rM1B_YWb0s4xioskoC4kG8ZX1MB52z77vvVe17OoBfcNtMCDm4T8lo8Nw-8EEYLiX3LXr7b_841wZ-DcPy9AUwp-S9PdDdqE9-D7qDnVuj09A",
    "shshshfpb": "BApXWsPs6nPlAzJM8AJjXgkTcYJ92CtDfBgt5clZ69xJ1Mv-yWI628XS7jn_8YNYqdrdd5_LVhrOYjmU",
    "__jdb": "76161171.6.1772111101436759769482|4.1772197398"
}
url = "https://api.m.jd.com/api"
params = {
    "h5st": "20260227210336659;a6zmzg3wi6060dt0;b5216;tk03w65fb1a7c18nOs51bWCqEMW2ASR1U7Rdib9C4YjVM55uOVhTt6abgs5shCHP9vVeIM8O75U0k_JD8CXTh99ZkCQe;059e9c238d7441c846cfdb1dd7b60d17c4ae605c5f9e80bb33f784b0b85e50c3;5.2;1772197413659;gt6f-heE9g_UxJOHqUuIns7Drd7ZB5_ZxI7ZBh-f1ZOVB5_ZzUrJ-hfZXx-ZqZ_UtROIxh_V-QOT9I_V_U7UuFeTAY_VsFOUxRLUuJ_ZB5_ZxIdG6YLIqYfZB5hW-FOU_g_VvFeTvdLU8IeV_IeTwdbU8QOIodOTAAOIuBeT-h-T-VKJroLJ_YfZB5hW-dOW-h-T-ROE-YfZB5hW-9_WvpPUrkMI187ICMeH-h-T-J6ZBh-f1ZfUHAeMZo7NMY8V7AdO-h-T-trG9oLJvYfZB5hW-ZuVz8rM-h-T-JbF-hfZXxPCBh-f-h6Q-h-T-VOVsY7ZBhfZB5hWvh-T-dOVsY7ZBhfZB5hWtdeZnZfVwN6J-hfZBh-f1BOWB5_ZvdOE-YfZBhfZXx-ZvJ6JvVMEUYuG8M6ZB5_Z0kbIzc7F-hfZBh-f1heZnZfTsY7ZBhfZB5hWxh-T-FOE-YfZBhfZXx-Vvh-T-JOE-YfZBhfZXxfVB5_ZsN6J-hfZBh-f1heZnZfUsY7ZBhfZB5hWrVeZnZvVsY7ZBhfZB5hW-R_WwpfV-h-T-dOE-YfZBhfZXxfVB5_Z2E6ZBhfZB5hWsh-T-VaG-hfZBh-f1heZnZfG-hfZBh-f1heZnZfIqYfZBhfZX1aZnZfIzMbEpM7ZBh-f1taZB5BZ3gcLKIqNOANNK09LCQ7H-h-T-ZeF-hfZBh-fmg-T-haF-hfZXx-ZtJeDB1eUrpLHKgvTxpfVwhfMTgvFqkbIz8rM-h-T-dLEuYfZB5xD;338ca7ab835e7a433690d11683deafee1f58b1ec9148ad638991b5a217d03ee3;fZhIYorG4QqJzM6I1R6G88bG_wPD9k7J1RLHxgKJ",
    "uuid": "1772111101436759769482",
    "body": "{\"qryParam\":[{\"type\":\"advertGroup\",\"mapTo\":\"advertInfos\",\"id\":\"04752737\"}],\"sourceCode\":\"pcDt\",\"pageId\":\"\",\"activityId\":\"\",\"reqSrc\":\"mainActivity\",\"platform\":0,\"siteClientVersion\":\"\",\"applyKey\":\"jd_mall_pc_home\"}",
    "functionId": "qryCompositeMaterials",
    "appid": "www-jd-com",
    "x-api-eid-token": "jdd03BZVE6BDBQMIRQWOFO24NBCB5NCPSFEZQI2LWATBCLZLCUWWX23CFYHLJ35CPKHSC62NLZB4NKJIH3YKUOZCBTFALB4AAAAM4T4YRHRAAAAAADQDUHAZ4XKLRTEX",
    "client": "wh5",
    "callback": "jsonpSchoolFloor",
    "_": "1772197413673"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)