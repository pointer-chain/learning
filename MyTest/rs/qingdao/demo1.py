import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
    "JSESSIONID": "2501F61C02DB26456C5BFCCC64894AD4",
    "tpass_aec7eia2ab294w26aw2899f9ded277e5": "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjJkY2JiNTY4NjViMzRlODk4ODkyNzczOTdkMWY1NGFiIn0.k3quXJjup22ykR6Nky7NZgXffYwZnZpYqR32elm_goI0_IYzrdAC7fF9_2e0HhvzsnIQogtlQcmM4bRB3MvV7w",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22195657ffb3a493-02c39df4575ebea-2c7f0c5f-2073600-195657ffb3bda5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1NjU3ZmZiM2E0OTMtMDJjMzlkZjQ1NzVlYmVhLTJjN2YwYzVmLTIwNzM2MDAtMTk1NjU3ZmZiM2JkYTUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22195657ffb3a493-02c39df4575ebea-2c7f0c5f-2073600-195657ffb3bda5%22%7D",
    "sajssdk_2015_cross_new_user": "1",
    "oauth2_referer": "etax.guizhou.chinatax.gov.cn",
    "znhd-ssotoken": "609f026ba26f4dd09e9afa9fa29f5374",
    "ZNHD_SECURITY_CHECK_TOKEN": "35af91550af24c239726477d18a8d1c8",
    "DZSWJ_TGC": "9A81D4868FE3CDB2A837DD540D91F39A",
    "SYS_CHANNEL_ID": "J4",
    "route": "b1ef52395b346adc0864ef06439806d3",
    "1zIlXIQYC8aAO": "60BklYm0.J5c3iqeHuu_sfdbRuYNQ0CpRQYps1HBTmNMoDA45iGXGfp_PK3KemCAWNZFHoB6AizXp0v5MvPpSFhA",
    "1zIlXIQYC8aAP": "0gjc9PNn5LY7d1lk5bmf_knOV213TExZ99YrNGuko0qa69nnYnenYmUKsOnv4r2jvGmWhMS5bpoBdUnncLs1zjrJFGGu5uGTkcTQtF_0Eigmfv1tDHhKVq2q_rhuGBDzOpnUfzIWotck4KQrL8GKjPNnBA9VThBAT39BA2Zgv8uUlxS4xl2s9eRIbxTFwZ430w.N7P9oqLbpxALydRCy6qD.jQjxDC71YcoVXk9p_RVSF.k_nSE0pEivpmWqeWcEdNMWTVrT30SOK9XxLlZtiAV1NCrkb80fw9PcouuIB24NrZ_mH0RP2lpcbeDxxSazkt9cEuHeXU0cwrU.HZR_IrwfpirG8CxNWjYlYfwbuSqvQ.pRKrEqV7lb5J5v5Msnb01FwTyjpKAD3UgoBqLQcBF.xDMocSh4R7Yy913242.aJj09HHDhAlsAwh8PQaEGk"
}
url = "https://etax.guizhou.chinatax.gov.cn/shbxf-cjpt-web/view/sbjs/sbfjkcxjdy/jkcxjdy.jsp"
params = {
    "gdslxDm": "1",
    "channelId": "J4"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)