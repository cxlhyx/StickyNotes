from imports import *

plugin_path = os.path.join(
    os.path.dirname(sys.executable), "Lib", "site-packages", "PyQt5", "Qt", "plugins"
)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path
# 设置为exe即将存储的目录路径或克隆下来的项目路径
directory = "D:\college\Project\StickyNotes"
Startup.create_bat_file(directory)


class Main(QMainWindow):  # type: ignore
    def __init__(self):
        super().__init__()

        # 使用生成的界面类创建界面对象
        self.ui = Ui()
        self.ui.setupUi(self)  # 设置界面

        # 可以在这里连接信号和槽，设置界面初始化逻辑、初始化变量等
        self.setWindowTitle("Sticky Notes")
        self.is_on_top = False  # 是否置顶
        self.is_startup = Startup.is_in_startup(
            directory + "\StickyNotes.bat"
        )  # 是否开机启动
        self.colored_dates = []  # 选中item的日期
        self.item = None  # 选中的item

        # event栏
        self.model = QStandardItemModel()  # 创建一个 QStandardItemModel
        self.ui.listView.setModel(self.model)  # 设置为QListView的模型
        self.delegate = LineDelegate()  # 设置自定义委托
        self.ui.listView.setItemDelegate(self.delegate)
        self.delegate.rightClicked.connect(self.showListViewMenu)  # 设置右键点击事件
        self.delegate.leftClicked.connect(self.colorSelectedDate)  # 设置左键点击事件
        self.db = Database()  # 连接数据库
        for i in self.db.SelectALL():
            self.model.appendRow(i)  # 添加项目

        # 时钟
        self.ui.lcdNumber.setDigitCount(19)  # 设置显示的位数，包括日期和时间
        self.timer = QTimer(self)  # 创建一个定时器，每秒更新一次时间显示
        self.timer.timeout.connect(self.updateTime)  # 设置时钟更新
        self.timer.start(1000)  # 每隔1000毫秒（1秒）更新一次

    def updateTime(self):
        # 获取当前日期和时间
        currentDateTime = QDateTime.currentDateTime()
        # 将日期和时间格式化为字符串
        displayText = currentDateTime.toString("yyyy-MM-dd hh:mm:ss")
        # 在 QLCDNumber 上显示时间
        self.ui.lcdNumber.display(displayText)

    def clearPreviousFormats(self):
        if self.item != None:
            self.item = None
        if len(self.colored_dates) != 0:
            for date in self.colored_dates:
                self.ui.calendarWidget.setDateTextFormat(date, QTextCharFormat())
            self.colored_dates = []

    def colorSelectedDate(self, index):
        # Clear previous formats
        self.clearPreviousFormats()

        self.item = self.model.item(index)

        # 给对应的日期上色
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("yellow")))

        date_format = "yyyy-MM-dd hh:mm:ss"
        start_time = self.item.start_time
        end_time = self.item.end_time
        start_time = QDateTime.fromString(start_time, date_format)
        end_time = QDateTime.fromString(end_time, date_format)
        start_date = start_time.date()
        end_date = end_time.date()
        if not start_date.isNull():
            current_date = start_date
            while True:
                self.ui.calendarWidget.setDateTextFormat(current_date, fmt)
                self.colored_dates.append(current_date)
                current_date = current_date.addDays(1)
                if current_date > end_date:
                    break

    def showListViewMenu(self, index):
        self.colorSelectedDate(index)

        self.item = self.model.item(index)

        # 在右键点击时显示上下文菜单
        menu = QMenu(self)
        action1 = menu.addAction("detail")
        action2 = menu.addAction("file")
        action3 = menu.addAction("delete")

        # 显示菜单并获取所选的操作
        action = menu.exec_(self.cursor().pos())

        # 根据所选的操作执行相应的逻辑
        if action == action1:
            DetailBox(self.db, self.item).exec_()  # type: ignore
            self.model.clear()
            for i in self.db.SelectALL():
                self.model.appendRow(i)  # 添加项目
        elif action == action2:
            files = self.item.file
            files = files.split("; ")
            for file in files:
                if file == "":
                    QMessageBox.warning(self, "文件打开出错", "文件为空")
                    return
                try:
                    os.startfile(file)  # 在 Windows 上打开文件
                except:
                    QMessageBox.warning(self, "文件打开出错", "暂不支持这种类型的文件")
        elif action == action3:
            self.db.Delete(self.item.id)
            self.model.clear()
            for i in self.db.SelectALL():
                self.model.appendRow(i)  # 添加项目

    def eventFilter(self, source, event):
        if (
            event.type() == event.MouseButtonPress
            and source is self.ui.listView.viewport()
        ):
            index = self.ui.listView.indexAt(event.pos())
            if not index.isValid():
                self.clearPreviousFormats()
                if event.button() == Qt.LeftButton:
                    self.handle_left_click(event)
                elif event.button() == Qt.RightButton:
                    self.handle_right_click(event)
                return True
        return super().eventFilter(source, event)

    def handle_left_click(self, event):
        pass

    def handle_right_click(self, event):
        # 在右键点击时显示上下文菜单
        menu = QMenu(self)
        action1 = menu.addAction("insert")
        action2 = menu.addAction("topping √" if self.is_on_top else "topping")
        action3 = menu.addAction("startup √" if self.is_startup else "startup")
        action4 = menu.addAction("about")
        action5 = menu.addAction("exit")

        # 显示菜单并获取所选的操作
        action = menu.exec_(self.cursor().pos())

        # 根据所选的操作执行相应的逻辑
        if action == action1:
            formDialog = FormDialog(None)  # type: ignore
            if formDialog.exec_() == QDialog.Accepted:
                form_data = formDialog.get_form_data()
                if not isinstance(form_data["id"], int):
                    return
                elif form_data["important"] != "null" and not isinstance(
                    form_data["important"], int
                ):
                    return
                new_item = Entity(
                    id=form_data["id"],
                    title=form_data["title"],
                    describe=form_data["describe"],
                    important=form_data["important"],
                    start_time=form_data["start_time"],
                    end_time=form_data["end_time"],
                    file=form_data["file"],
                )
                if self.db.Insert(new_item):
                    self.model.clear()
                    for i in self.db.SelectALL():
                        self.model.appendRow(i)  # 添加项目
                else:
                    QMessageBox.warning(
                        self, "Insert new event error", "Id was repeat!!!"
                    )
        elif action == action2:
            if self.is_on_top:
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()  # Update the window
            self.is_on_top = not self.is_on_top  # Toggle the state
        elif action == action3:
            if self.is_startup:
                Startup.remove_from_startup(directory + "\StickyNotes.bat")
            else:
                Startup.add_to_startup(directory + "\StickyNotes.bat")
            self.is_startup = not self.is_startup  # Toggle the state
        elif action == action4:
            self.msg_window = QWidget()
            self.msg_window.setWindowTitle("About")
            self.msg_window.setWindowFlags(Qt.Drawer)
            self.layout = QVBoxLayout()
            self.label = QLabel("版本: 1.0.2\n作者: cxlhyx")
            self.layout.addWidget(self.label)
            self.msg_window.setLayout(self.layout)
            self.msg_window.show()
        elif action == action5:
            QCoreApplication.quit()  # 退出应用


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.ui.listView.viewport().installEventFilter(window)
    window.show()
    sys.exit(app.exec_())
