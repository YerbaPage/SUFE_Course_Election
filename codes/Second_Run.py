from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# Opening browser
browser = webdriver.Chrome()
# 此处换成自己选课页面的链接 每一轮选课 每一学期都似乎不同
browser.get(
    'http://eams.sufe.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=5926')
# 需要手动完成登录
void = input("请完成登录后回车")
number = input("请输入课程序号(四位):")
while len(list(number)) != 4:
    number = input("请输入正确的课程序号(四位):")
void = input("初始化完成, 回车后开始选课")

fin = '开始捡漏'
while "成" not in list(fin):
    try:
        # Searching
        textbox = browser.find_element_by_xpath(
            '//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input')
        textbox.clear()
        # 此处"0028"换成需要蹲的课程序号
        textbox.send_keys(number)
        # textbox.submit()
        textbox.send_keys(Keys.ENTER)
        try:
            # Submitting
            button = browser.find_element_by_xpath(
                '/html/body/div[10]/div[2]/form/div/table/tbody/tr/td[11]/a')
            button.send_keys(Keys.ENTER)
            # Results
            result = browser.find_element_by_xpath(
                '//*[@id="cboxLoadedContent"]/table/tbody/tr[1]/td/div')
            fin = result.text
            if "功" in list(result.text):
                # end
                button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
                button.click()
                break
            # end
            button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
            button.click()
        except:
            fin = fin
        time.sleep(2.5)
    except:
        input('Some problem occurs, press ENTER if you have fixed it')
print(fin)
