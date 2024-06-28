# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StickyNotes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from imports import *


class Ui(object):
    def setupUi(self, Frame):
        # 设置窗口透明度
        Frame.setWindowOpacity(0.5)

        # 设置窗口为无边框
        Frame.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore

        # 设置窗口位置
        self.fixed_position = QPoint(1160, 0)  # type: ignore # 固定位置
        Frame.move(self.fixed_position)

        Frame.setObjectName("Frame")
        Frame.resize(761, 574)
        self.calendarWidget = QCalendarWidget(Frame)  # type: ignore
        self.calendarWidget.setGeometry(QRect(250, 0, 511, 371))  # type: ignore
        self.calendarWidget.setStyleSheet(
            "/* 设置日历工具按钮（如上一个月、下一个月按钮）的样式 */\n"
            "                    QCalendarWidget QToolButton {\n"
            "                    height: ; /* 按钮高度 */\n"
            "                    width: ; /* 按钮宽度 */\n"
            "                    color: ; /* 按钮文字颜色 */\n"
            "                    font-size: ; /* 按钮文字大小 */\n"
            "                    icon-size: , ; /* 按钮图标大小 */\n"
            "                    background-color: ; /* 按钮背景颜色 */\n"
            "                    border: ; /* 按钮无边框 */\n"
            "                    margin: ; /* 按钮外边距 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置工具按钮悬停时的背景颜色 */\n"
            "                    QCalendarWidget QToolButton:hover {\n"
            "                    background-color: #87CEEB; /* 悬停时的背景颜色 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置工具按钮菜单指示器的位置 */\n"
            "                    QCalendarWidget QToolButton::menu-indicator {\n"
            "                    subcontrol-position: bottom center; /* 菜单指示器的位置 */\n"
            "                    subcontrol-origin: padding; /* 菜单指示器的原点 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置年份选择框（QSpinBox）的样式 */\n"
            "                    QCalendarWidget QSpinBox {\n"
            "                    width: 100px; /* 选择框宽度 */\n"
            "                    font-size: 18px; /* 字体大小 */\n"
            "                    color: white; /* 字体颜色 */\n"
            "                    background: transparent; /* 背景透明 */\n"
            "                    selection-background-color: #1E90FF; /* 选中时的背景颜色 */\n"
            "                    selection-color: white; /* 选中时的字体颜色 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置年份选择框的上按钮样式 */\n"
            "                    QCalendarWidget QSpinBox::up-button {\n"
            "                    subcontrol-origin: border; /* 上按钮的原点 */\n"
            "                    subcontrol-position: top right; /* 上按钮的位置 */\n"
            "                    width: 35px; /* 上按钮宽度 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置年份选择框的下按钮样式 */\n"
            "                    QCalendarWidget QSpinBox::down-button {\n"
            "                    subcontrol-origin: border; /* 下按钮的原点 */\n"
            "                    subcontrol-position: bottom right; /* 下按钮的位置 */\n"
            "                    width: 35px; /* 下按钮宽度 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置年份选择框的上箭头大小 */\n"
            "                    QCalendarWidget QSpinBox::up-arrow {\n"
            "                    width: 20px; /* 上箭头宽度 */\n"
            "                    height: 20px; /* 上箭头高度 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置年份选择框的下箭头大小 */\n"
            "                    QCalendarWidget QSpinBox::down-arrow {\n"
            "                    width: 20px; /* 下箭头宽度 */\n"
            "                    height: 20px; /* 下箭头高度 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置日历小部件的交替背景颜色 */\n"
            "                    QCalendarWidget QWidget {\n"
            "                    alternate-background-color: ; /* 交替背景颜色 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置日历视图中启用项的样式 */\n"
            "                    QCalendarWidget QAbstractItemView:enabled {\n"
            "                    font-size: 18px; /* 字体大小 */\n"
            "                    color: ; /* 字体颜色 */\n"
            "                    background-color: ; /* 背景颜色 */\n"
            "                    selection-background-color: ; /* 选中时的背景颜色 */\n"
            "                    selection-color: ; /* 选中时的字体颜色 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置日历视图中禁用项的样式 */\n"
            "                    QCalendarWidget QAbstractItemView:disabled {\n"
            "                    color: ; /* 禁用项的字体颜色 */\n"
            "                    }\n"
            "\n"
            "                    /* 设置日历导航栏的背景颜色 */\n"
            "                    QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
            "                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0\n"
            "                    rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); /* 导航栏背景颜色 */\n"
            "                    }\n"
            "                "
        )
        self.calendarWidget.setFirstDayOfWeek(Qt.Sunday)  # type: ignore
        self.calendarWidget.setObjectName("calendarWidget")
        self.lcdNumber = QLCDNumber(Frame)  # type: ignore
        self.lcdNumber.setGeometry(QRect(240, 370, 521, 211))  # type: ignore
        self.lcdNumber.setObjectName("lcdNumber")
        self.listView = QListView(Frame)  # type: ignore
        self.listView.setGeometry(QRect(0, 0, 251, 581))  # type: ignore
        self.listView.setObjectName("listView")

        self.retranslateUi(Frame)
        QMetaObject.connectSlotsByName(Frame)  # type: ignore

    def retranslateUi(self, Frame):
        _translate = QCoreApplication.translate  # type: ignore
        Frame.setWindowTitle(_translate("Frame", "Frame"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # type: ignore
    Frame = QFrame()  # type: ignore
    ui = Ui()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
