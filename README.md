- 👋 Hi, I’m @货又星
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞 I’m looking to collaborate on ...
- 📫 How to reach me ...
  - [README 目录（持续更新中） 各种错误处理、爬虫实战及模板、百度智能云人脸识别、计算机视觉深度学习CNN图像识别与分类、PaddlePaddle自然语言处理知识图谱、GitHub、运维...](https://blog.csdn.net/muaamua/article/details/134426428?spm=1001.2014.3001.5502)
  - WeChat：1297767084
  - Email：cxlhyx1297767084@gmail.com
  - GitHub：[https://github.com/cxlhyx](https://github.com/cxlhyx)
    ![在这里插入图片描述](/qrcode.jpg)
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
cxlhyx/cxlhyx is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

## 项目结构

```
D:.
│  Main.py                                 # 主函数，实现按键点击等功能
│  Ui.ui                                   # 使用Qt Designer设计的界面ui
│  Ui.py                                   # 根据界面ui生成的python代码
│  LineDelegate.py                         # 左侧event栏的自定义委托
│  Sql.py                                  # 数据：数据库增删改查、event实体
│  DetailBox.py                            # event详情盒：查看event、更新event
│  Startup.py                              # 开机自启动
│  imports.py                              # 导入需要的库
│  requirements.txt                        # 项目依赖
│  README.md							   
│  Database.db                             # sqlite数据库
│  StickyNotes.exe                         # 打包成的exe
│  StickyNotes.exe - 快捷方式.lnk           # exe的快捷方式，用户可能需要自己更改
│  qrcode.jpg                              # 作者wx
│
└─__pycache__                              # 运行缓存
        DetailBox.cpython-39.pyc
        imports.cpython-39.pyc
        LineDelegate.cpython-39.pyc
        Sql.cpython-39.pyc
        Startup.cpython-39.pyc
        Ui.cpython-39.pyc
```

## 使用

### 抓取

```
git clone git@github.com:cxlhyx/StickyNotes.git
```

### 安装依赖

```
pip install -r requirements.txt
```

### 运行

```
python Main.py
```

## 注意

- event的日期格式必须为"**yyyy-MM-dd hh:mm:ss**"，否则右侧日历表将无法对选中的event日期进行涂色。

- event的file为**绝对路径**。

  对于每个文件可以用**双引号**也可以不用，对于多个文件中间需要用"; "隔开（**英文分号和空格**），最后一个文件时不能再用"; "。

- 建议不要直接使用项目的exe，以免bug。先修改Main.py中第8行的directory = "D:\college\Project\StickyNotes"，改为exe即将存储的路径或直接改为项目克隆的路径，接着在克隆下来的目录下使用以下命令即可编译生成exe文件。StickyNotes.exe 将被生成在 dist 目录中。PyInstaller 还会创建 build 目录和 MyApp.spec 文件。build 目录包含构建过程中使用的中间文件，而 .spec 文件是构建过程的配置文件。如果不希望保留 build 目录和 .spec 文件，可以手动删除它们。
```
pip install pyinstaller
pyinstaller -F -w --name StickyNotes Main.py
```

## release

v1.0.0：2024-06-29 基础功能

v1.0.1：2024-06-29 新增打开多个文件的功能

v1.0.2: 2024-07-05 修复了开机自动启动event列表数据不显示的问题

## 欢迎微信、邮箱、GitHub提出建议或问题
