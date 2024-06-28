from imports import *


class LineDelegate(QStyledItemDelegate):  # type: ignore
    # 自定义信号，传递项目索引
    rightClicked = pyqtSignal(int)  # type: ignore
    leftClicked = pyqtSignal(int)  # type: ignore

    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        painter.save()

        # 设置字体大小
        self.font = QFont()  # type: ignore
        self.font.setPointSize(14)  # 设置字体大小为14
        painter.setFont(self.font)

        # 设置文本颜色
        painter.setPen(option.palette.color(QPalette.Text))  # type: ignore

        super().paint(painter, option, index)

        painter.restore()

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setHeight(size.height() + 10)  # 增加高度以适应分隔线
        return size

    def createEditor(self, parent, option, index):
        # 返回None，表示不允许编辑
        return None

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:  # type: ignore
            self.rightClicked.emit(index.row())  # 发出右键点击信号
            return True
        elif (
            event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton  # type: ignore
        ):
            self.leftClicked.emit(index.row())  # 发出左键点击信号
            return True
        return super().editorEvent(event, model, option, index)
