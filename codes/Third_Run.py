from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys



chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/usr/bin/chromium-browser"
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless') # 算了 懒得写自动登陆了 
browser = webdriver.Chrome(chrome_options=chrome_options)



# 不同年级选课网址不同 请注意调整
browser.get('http://eams.sufe.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=5385')

void = input("请完成登录后回车")
course_id = input("请输入课程序号(四位):")
while len(list(course_id)) != 4:
    course_id = input("请输入正确的课程序号(四位吧?):")
void = input("初始化完成, 回车后开始选课")

final = '开始捡漏'

while "成" not in list(final):
    try:
        xuanke = browser.find_element_by_xpath(
            '/html/body/div[10]/div[1]/div[2]')
        xuanke.click()
        # Searching
        textbox = browser.find_element_by_xpath(
            '//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input')
        textbox.clear()
        # 输入目标课程序号
        textbox.send_keys(course_id)
        # textbox.submit()
        textbox.send_keys(Keys.ENTER)
        try:
            # Submitting
            button = browser.find_element_by_xpath(
                '/html/body/div[10]/div[3]/form/div/table/tbody/tr/td[11]/a')
            button.send_keys(Keys.ENTER)
            # Results
            result = browser.find_element_by_xpath(
                '//*[@id="cboxLoadedContent"]/table/tbody/tr[1]/td/div')
            final = result.text
            if "功" in list(final):
                # end
                button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
                button.click()
                sys.exit(0)
            # end
            button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
            button.click()
        except:
            final = final
        time.sleep(2)
    except:
        input('Some problem occurs, press ENTER if you have fixed it')
print(final)
