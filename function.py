import requests
import ddddocr
from chaojiying import Chaojiying_Client

# location格式为“ 是（崇山校区）”“ 是（蒲河校区）”“否”

def function(username, password, provinces, area, jd, community, room, temperature, location, ipLocation):
    # 登录界面抓取
    login_url = 'http://tjxx.lnu.edu.cn/login.asp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
    }
    session = requests.session()
    login_page = session.get(url=login_url, headers=headers)

    # 验证码图片抓取
    img_url = 'http://tjxx.lnu.edu.cn/inc/checkcode.asp'
    img_data = session.get(url=img_url, headers=headers)
    with open('./code.jpg', 'wb')as fp:
        fp.write(img_data.content)

    # 识别验证码区域，识别的结果返回给code，
    code = 

    # 登录操作页面抓取
    login_do_url = 'http://tjxx.lnu.edu.cn/login_do.asp'
    data = {
        'userid': username,
        'userpwd': password,
        'checkcode': code
    }

    login_do_page = session.post(url=login_do_url, data=data, headers=headers)

    # 填报页面抓取
    inputExt_url = 'http://tjxx.lnu.edu.cn/inputExt.asp'
    inputExt_page = session.get(url=inputExt_url, headers=headers)

    # 填报完毕页面抓取
    inputExt_do_url = 'http://tjxx.lnu.edu.cn/inputExt_do.asp'
    inputExt_data = {
        "xszd": provinces,  # 省市
        "xszq": area,  # 区
        "xszjd": jd,  # 街道
        "xszsq": community,  # 社区
        "jtdz": room,  # 寝室
        "csld": "无",
        'csldxx': '',
        'hbjc': '无',
        'hbjcxx': '',
        'drtw': temperature,
        'fyzz': '健康',
        'fyzzxx': '',
        'glzt': '否',
        'zxzg': location,  # 崇山 / 蒲河 / 不在校
        'xcgj': '无',
        'xcgjxx': '',
        'gdipszd': '',
        'bdipszd': '',
        'txipszd': ipLocation,
    }
    inputExt_do_page = session.post(url=inputExt_do_url, data=inputExt_data, headers=headers)

