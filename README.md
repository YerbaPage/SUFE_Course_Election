# Course_selection_for_SUFE
上海财经大学自动选课脚本 支持二轮三轮及开学选课

## Requirements

- Chrome 

- Selenium (Python)

  ```
  pip install -r requirements.txt
  ```

- Selenium Chrome WebDriver (已附带对应最新版本的 WebDriver for Windows)

  > 可以在此下载与你的 Chrome 相应的版本 https://chromedriver.chromium.org/ 移动到 `codes/`目录下即可)

## Procedure

以第三轮选课为例: 

1. 修改 Third_Run.py 文件 line 11: 

   > https://github.com/YerbaPage/Course_selection_for_SUFE/blob/master/codes/Third_Run.py#L10-L11

   ```Python
   browser.get('http://eams.sufe.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=5385')
   ```

   中为你的选课地址 (不同年级貌似不一样)

2. 在 Terminal 中运行

   ```bash
   python Third_Run.py
   ```

3. 根据命令行提示在弹出的浏览器完成登录, 完成后回车

4. 输入课程代码, 回车, 开始蹲点

## Update 

#### 2021/1/4

- Allow input from terminal 
- more detailed README 

#### 2020/9/1

- 新增第三轮选课脚本 还是一样修改选课网址和课程序号即可 (开学选课可用)

ps : 祝大家蹲到想要的课程~

