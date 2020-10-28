from selenium import webdriver


# 自定义代理IP 及 请求头。
chromeOptions = webdriver.ChromeOptions()
# 加载配置数据
configPath = r'--user-data-dir=/Users/FionaYang/Library/Application Support/Google/Chrome'
chromeOptions.add_argument(configPath)
# chromeOptions.add_argument("--proxy-server=http://218.93.119.165:9002")
# chromeOptions.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 \
#                             like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like \
#                             Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

browser = webdriver.Chrome(r'/Users/FionaYang/chromedriver', options=chromeOptions)

# browser.get("http://httpbin.org/ip")  # 查看IP是否切换。
# print(browser.page_source)

# 获取请求头信息
agent = browser.execute_script("return navigator.userAgent")
print(agent)  # 查看请求头是否更改。

browser.close()
