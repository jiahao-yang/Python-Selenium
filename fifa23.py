# This is for FIFA23
# coding:utf-8

from selenium import webdriver
import time
from datetime import datetime
import json
from pathlib import Path


# def find_element(condition):
#     retry_limit = 3
#     for i in range(retry_limit):
#         try:
#             print(f"Click the {condition} for the {i+1} time")
#             club = wd.find_element_by_css_selector('button[class*="ut-tab-bar-item icon-club"]')
#             break
#         except:
#             print(f"Sleep and then retry clicking {condition} for the {i + 1} time")
#             time.sleep(5)
#             continue


def go_to_page(element):
    retry_limit = 10
    for i in range(retry_limit):
        try:
            print(f"Click the {element.text} for the {i + 1} time")
            element.click()
            print(f"Successfully clicked the button")
            break
        except:
            print(f"Sleep and then retry clicking {element.text} for the {i + 1} time")
            time.sleep(10)
            continue


def save_player_info(wd):
    # Get Player Stats and store into map
    print(f"Loading player info ...")
    player_list = wd.find_elements_by_xpath('//*[contains(@class,"listFUTItem")]')
    player_list_str = [str(player.get_attribute("outerHTML")) for player in player_list]
    player_names = [player.find_element_by_css_selector('.name') for player in player_list]
    player_names_str = [str(player_name.get_attribute("textContent")) for player_name in player_names]

    player_info_dict = dict(zip(player_names_str, player_list_str))

    # Save player info into file
    # file name:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    print(f"Saving player info ...")
    with open(f"FUT20 players full info {datetime.now().strftime('%Y-%m-%d')}.html", mode="a+", encoding="UTF-8") as f:
        f.write("\n".join(player_list_str))
        f.close()

    # with open(f"FUT20 player names {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.html", mode="w") as f:
    #     f.write("\n".join(player_names_str))
    #     f.close()

    with open(f"FUT20 player json {datetime.now().strftime('%Y-%m-%d')}.html", mode="a+", encoding="UTF-8") as f:
        json_str = json.dumps(player_info_dict, indent=0, ensure_ascii=False)
        f.write(json_str)
        f.close()

    print(f"Successfully saved player info")


def main():
    # 配置文件路径
    configPath = r'--user-data-dir=/Users/FionaYang/Library/Application Support/Google/Chrome'
    # 加载配置数据
    chromeConfig = webdriver.ChromeOptions()
    chromeConfig.add_argument(configPath)

    # 启动浏览器配置
    # wd = webdriver.Chrome(r'/Users/FionaYang/chromedriver', chrome_options=chromeConfig)
    wd = webdriver.Chrome(r'/Users/FionaYang/chromedriver', options=chromeConfig)

    wd.implicitly_wait(60)

    # print(wd.get_cookies())

    url = "https://www.easports.com/fifa/ultimate-team/web-app/"
    wd.get(url)

    # for handle in wd.window_handles:
    #     # 先切换到该窗口
    #     wd.switch_to.window(handle)
    #     # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    #     if 'EA SPORT' in wd.title:
    #         # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
    #         break
    #
    # # mainWindow变量保存当前窗口的句柄
    # mainWindow = wd.current_window_handle

    loading_time = 30
    print(f"Wait {loading_time} secs for loading the website")
    time.sleep(loading_time)

    print("Find Club")
    club = wd.find_element_by_css_selector('button[class*="ut-tab-bar-item icon-club"]')
    go_to_page(club)

    # Go to players page
    print("Go to Players page")
    players = wd.find_element_by_css_selector('[class*="players-tile"] .tileHeader')
    go_to_page(players)
    # players = wd.find_elements_by_css_selector('[class*="players-tile"]>*')
    # for player in players:
    #     print(f'Players elements: {player.get_attribute("outerHTML")}')
    #     go_to_page(player)

    # Browse through the players pages and save the player info into files
    player_page_count = 0
    while True:
        time.sleep(10)
        player_page_count += 1
        print(f"Save player info at page : {player_page_count}")
        save_player_info(wd)
        next_button = wd.find_element_by_css_selector('[class *="flat pagination next"]')
        if not next_button.is_displayed():
            print("This is the last page of Players")
            break;
        print("Next button exists. Click next button")
        next_button.click()

    time.sleep(0)

    wd.quit()


#########################
main()
