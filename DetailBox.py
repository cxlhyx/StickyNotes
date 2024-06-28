from imports import *


class FormDialog(QDialog):  # type: ignore
    # 插入或修改数据的表单
    def __init__(self, item, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail")
        self.setWindowFlags(Qt.Drawer)

        # Remove the '?' button by setting the window flags
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowContextHelpButtonHint
            | Qt.WindowCloseButtonHint
        )
        self.item = item

        # 文字和输入框
        self.id_Label = QLabel("Id:", self)  # type: ignore
        self.id_LineEdit = QLineEdit(self)  # type: ignore
        self.id_Layout = QHBoxLayout()
        self.id_Layout.addWidget(self.id_Label, alignment=Qt.AlignLeft)
        self.id_Layout.addWidget(self.id_LineEdit, alignment=Qt.AlignRight)

        self.title_Label = QLabel("Title:", self)
        self.title_LineEdit = QLineEdit(self)
        self.title_Layout = QHBoxLayout()
        self.title_Layout.addWidget(self.title_Label, alignment=Qt.AlignLeft)
        self.title_Layout.addWidget(self.title_LineEdit, alignment=Qt.AlignRight)

        self.describe_Label = QLabel("Describe:", self)
        self.describe_LineEdit = QLineEdit(self)
        self.describe_Layout = QHBoxLayout()
        self.describe_Layout.addWidget(self.describe_Label, alignment=Qt.AlignLeft)
        self.describe_Layout.addWidget(self.describe_LineEdit, alignment=Qt.AlignRight)

        self.important_Label = QLabel("Important:", self)
        self.important_LineEdit = QLineEdit(self)
        self.important_Layout = QHBoxLayout()
        self.important_Layout.addWidget(self.important_Label, alignment=Qt.AlignLeft)
        self.important_Layout.addWidget(
            self.important_LineEdit, alignment=Qt.AlignRight
        )

        self.start_time_Label = QLabel("Start_time:", self)
        self.start_time_LineEdit = QLineEdit(self)
        self.start_time_Layout = QHBoxLayout()
        self.start_time_Layout.addWidget(self.start_time_Label, alignment=Qt.AlignLeft)
        self.start_time_Layout.addWidget(
            self.start_time_LineEdit, alignment=Qt.AlignRight
        )

        self.end_time_Label = QLabel("End_time:", self)
        self.end_time_LineEdit = QLineEdit(self)
        self.end_time_Layout = QHBoxLayout()
        self.end_time_Layout.addWidget(self.end_time_Label, alignment=Qt.AlignLeft)
        self.end_time_Layout.addWidget(self.end_time_LineEdit, alignment=Qt.AlignRight)

        self.file_Label = QLabel("File:", self)
        self.file_LineEdit = QLineEdit(self)
        self.file_Layout = QHBoxLayout()
        self.file_Layout.addWidget(self.file_Label, alignment=Qt.AlignLeft)
        self.file_Layout.addWidget(self.file_LineEdit, alignment=Qt.AlignRight)

        self.submitButton = QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.submit_form)

        # 修改时显示原先数据
        if self.item != None:
            self.id_LineEdit.setText(str(self.item.id))
            self.title_LineEdit.setText(self.item.title)
            self.describe_LineEdit.setText(self.item.describe)
            self.important_LineEdit.setText(str(self.item.important))
            self.start_time_LineEdit.setText(self.item.start_time)
            self.end_time_LineEdit.setText(self.item.end_time)
            self.file_LineEdit.setText(self.item.file)

        layout = QVBoxLayout()
        layout.addLayout(self.id_Layout)
        layout.addLayout(self.title_Layout)
        layout.addLayout(self.describe_Layout)
        layout.addLayout(self.important_Layout)
        layout.addLayout(self.start_time_Layout)
        layout.addLayout(self.end_time_Layout)
        layout.addLayout(self.file_Layout)
        layout.addWidget(self.submitButton)
        self.setLayout(layout)

    def submit_form(self):
        self.form_data = {
            "id": self.id_LineEdit.text(),
            "title": self.title_LineEdit.text(),
            "describe": self.describe_LineEdit.text(),
            "important": self.important_LineEdit.text(),
            "start_time": self.start_time_LineEdit.text(),
            "end_time": self.end_time_LineEdit.text(),
            "file": self.file_LineEdit.text(),
        }
        # 类型检查、空值判断
        try:
            self.form_data["id"] = eval(self.form_data["id"])
            # 同时做了空值判断和类型检查
        except:
            QMessageBox.warning(self, "Event error", "Id must be integer!!!")
        if self.form_data["important"] == "":
            self.form_data["important"] = "null"  # 空值判断
        else:
            try:
                self.form_data["important"] = eval(
                    self.form_data["important"]
                )  # 类型检查
            except:
                QMessageBox.warning(self, "Event error", "Important must be integer!!!")
        # 空值判断
        if self.form_data["title"] == "":
            self.form_data["title"] = "null"
        if self.form_data["describe"] == "":
            self.form_data["describe"] = "null"
        if self.form_data["start_time"] == "":
            self.form_data["start_time"] = "null"
        if self.form_data["end_time"] == "":
            self.form_data["end_time"] = "null"
        if self.form_data["file"] == "":
            self.form_data["file"] = "null"

        self.accept()

    def get_form_data(self):
        return self.form_data


class DetailBox(QDialog):
    # 一个event对应一个detailbox
    def __init__(self, db, item, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sticky Notes Event Detail")
        self.setWindowFlags(Qt.Drawer)
        self.db = db
        self.item = item

        # Remove the '?' button by setting the window flags
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowContextHelpButtonHint
            | Qt.WindowCloseButtonHint
        )

        self.label = QLabel(str(self.item))
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        self.updateButton = QPushButton("Update")
        self.updateButton.clicked.connect(self.detailUpdate)

        # Horizontal layout for the buttons
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.updateButton)
        buttonLayout.addWidget(self.okButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def detailUpdate(self):
        formDialog = FormDialog(self.item)
        if formDialog.exec_() == QDialog.Accepted:
            form_data = formDialog.get_form_data()
            self.db.Update(
                self.item.id,
                id=form_data["id"],
                title=form_data["title"],
                describe=form_data["describe"],
                important=form_data["important"],
                start_time=form_data["start_time"],
                end_time=form_data["end_time"],
                file=form_data["file"],
            )
            self.item = self.db.Select(form_data["id"])
            self.label.setText(str(self.item))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    def show_silent_message():
        db = Database()
        msg = DetailBox(db, db.Select(1))
        msg.exec_()

    show_silent_message()
    sys.exit(app.exec_())
