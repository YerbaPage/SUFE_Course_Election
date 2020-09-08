#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
#Openning browser
browser = webdriver.Chrome()
# 不同年级选课网址不同 请注意调整
browser.get('http://eams.sufe.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=5385')


# In[ ]:


final = '开始捡漏'
course_id = input('请完成登录, 并输入课程序号:')
wait_time = int(input('请设置每次查询间隔时间___s'))

while "成" not in list(final):
    xuanke = browser.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]')
    xuanke.click()
    #Searching
    textbox = browser.find_element_by_xpath(
        '//*[@id="electableLessonList"]/thead/tr[1]/th[2]/div/input')
    textbox.clear()
    # 输入目标课程序号
    textbox.send_keys(course_id)
    #textbox.submit()
    textbox.send_keys(Keys.ENTER)
    try:
        #Submitting
        button = browser.find_element_by_xpath(
            '/html/body/div[10]/div[3]/form/div/table/tbody/tr/td[11]/a')
        button.send_keys(Keys.ENTER)
        #Results
        result = browser.find_element_by_xpath(
            '//*[@id="cboxLoadedContent"]/table/tbody/tr[1]/td/div')
        final = result.text
        if "功" in list(final):
            #end
            button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
            button.click()
            sys.exit(0)
        #end
        button = browser.find_element_by_xpath('//*[@id="cboxClose"]')
        button.click()
    except:
        final = final
    time.sleep(1)
print(final)

