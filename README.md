# Course_selection_for_SUFE
上海财经大学选课脚本 自动连续点击选课操作以捡漏

## Requirements

- Chrome Version 87.0.4280.88 (Official Build) (64-bit) 

- ```
  pip install -r requirements.txt
  ```

- Selenium Chrome WebDriver (已附带对应最新版本的WebDriver)

  > 可以在此下载相应版本 https://chromedriver.chromium.org/

## Procedure

以第三轮选课为例: 

1. 修改 Third_Run.py 文件 line 11: browser.get('http://eams.sufe.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=5385')`中为你的选课地址 (不同年级貌似不一样)
2. 运行
3. 根据命令行提示完成登录并输入课程代码即可开始蹲点

## Update 

#### 2021/1/4

- Allow input from terminal 
- more detailed README 

#### 2020/9/1

- 新增第三轮选课脚本 还是一样修改选课网址和课程序号即可 (开学选课可用)

ps : 祝大家蹲到想要的课程~

