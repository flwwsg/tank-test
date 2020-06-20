import requests


def regist():
    for i in range(10):
        a = requests.get("https://github.com")
        phone = 18000000001
        data = {"account": "TEST0000%s" % i, "phone": str(phone + i), "captcha": "1111", "password": "a1111111",
                "repeat_password": "a1111111"}
        result = requests.post("https://admin.tepleton.info/account/api/v1/register", data)
        print(result.json())


g_tokenDict = {}


def getToken(phone):
    # phone = str(18000000000 + i)
    date = {"phone": str(phone), "password": "a1111111", "smsCode": "11"}
    result = requests.post("https://admin.tepleton.info/api/v1/login", json=date)
    result = dict(result.json())
    # print(result)
    if not result["success"]:
        return
    token = result["data"]["token"]
    # print(token)
    g_tokenDict[phone] = token
    return token


if __name__ == '__main__':
    while 1:
        phont = input("输入手机号：")
        token = getToken(phont)
        print(token)
