from imports import *


class Entity(QStandardItem):  # type: ignore
    def __init__(
        self,
        id,
        title=None,
        describe=None,
        important=-1,
        start_time=None,
        end_time=None,
        create_time=None,
        file=None,
    ):
        super().__init__(str(id) + " " + str(title))
        assert id != None, "Id was needed!!!"
        if create_time == None:
            # 获取当前日期和时间
            currentDateTime = QDateTime.currentDateTime()  # type: ignore
            # 将日期和时间格式化为字符串
            create_time = currentDateTime.toString("yyyy-MM-dd hh:mm:ss")
        self.id = id
        self.title = title
        self.describe = describe
        self.important = important
        self.start_time = start_time
        self.end_time = end_time
        self.create_time = create_time
        self.file = file

    def __str__(self):
        return (
            "{"
            + "\n    id: "
            + str(self.id)
            + ",\n    title: "
            + self.title
            + ",\n    describe: "
            + self.describe
            + ",\n    important: "
            + str(self.important)
            + ",\n    start_time: "
            + self.start_time
            + ",\n    end_time: "
            + self.end_time
            + ",\n    creat_time: "
            + self.create_time
            + ",\n    file: "
            + self.file
            + "\n}"
        )


class Database:
    def __init__(self) -> None:
        # 初始化数据库连接
        self.initDatabase()

    def initDatabase(self):
        # 添加 SQLite 驱动
        db = QSqlDatabase.addDatabase("QSQLITE")  # type: ignore
        db.setDatabaseName("Database.db")  # 使用文件路径，也可以是内存中的数据库

        if not db.open():
            print("无法建立数据库连接！")
            return False

        # 创建表格
        query = QSqlQuery()  # type: ignore
        query.exec_(
            """
            CREATE TABLE IF NOT EXISTS event 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            describe TEXT,
            important INTEGER,
            start_time TEXT,
            end_time TEXT,
            create_time TEXT,
            file TEXT)
            """
        )

        """
        # 插入测试数据
        self.Insert(
            StickyNotesEntity(
                1,
                "测试",
                "用于测试的事件",
                1,
                "2024-06-25 23:00:32",
                "2024-06-25 23:00:32",
                None,
                "D:\college\Project\新建文件夹\StickyNotes.ui",
            )
        )
        """
        return True

    def Select(self, id):
        query = QSqlQuery()  # type: ignore
        query.exec_(
            f"""
            SELECT *
            FROM event
            WHERE id={id}
            """
        )
        if query.next():
            return Entity(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
            )
        else:
            return None

    def SelectALL(self):
        # 查询数据库中的数据并输出
        query = QSqlQuery()  # type: ignore
        query.exec_("SELECT * FROM event")
        stickyNotesEntities = []
        while query.next():
            stickyNotesEntity = Entity(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
            )
            stickyNotesEntities.append(stickyNotesEntity)
        return stickyNotesEntities

    def Insert(self, stickyNotesEntity):
        tmp = f"{stickyNotesEntity.id}"
        if stickyNotesEntity.title != "null":
            tmp += f", '{stickyNotesEntity.title}'"
        else:
            tmp += f", {stickyNotesEntity.title}"
        if stickyNotesEntity.describe != "null":
            tmp += f", '{stickyNotesEntity.describe}'"
        else:
            tmp += f", {stickyNotesEntity.describe}"
        tmp += f", {stickyNotesEntity.important}"
        if stickyNotesEntity.start_time != "null":
            tmp += f", '{stickyNotesEntity.start_time}'"
        else:
            tmp += f", {stickyNotesEntity.start_time}"
        if stickyNotesEntity.end_time != "null":
            tmp += f", '{stickyNotesEntity.end_time}'"
        else:
            tmp += f", {stickyNotesEntity.end_time}"
        tmp += f", '{stickyNotesEntity.create_time}'"
        if stickyNotesEntity.file != "null":
            tmp += f", '{stickyNotesEntity.file}'"
        else:
            tmp += f", {stickyNotesEntity.file}"
        query = QSqlQuery()  # type: ignore
        return query.exec_(
            f"""
            INSERT INTO event (id, title, describe, important, start_time, end_time, create_time, file) 
            VALUES ({tmp})
            """
        )

    def Delete(self, id):
        query = QSqlQuery()  # type: ignore
        return query.exec_(
            f"""
            DELETE
            FROM event
            WHERE id={id}
            """
        )

    def Update(self, ID, **kwargs):
        tmp = ""
        for key, value in kwargs.items():
            if key == "id" or key == "important" or value == "null":
                tmp += f"{key}={value},"
            else:
                tmp += f"{key}='{value}',"
        query = QSqlQuery()  # type: ignore
        return query.exec_(
            f"""
            UPDATE event
            SET {tmp[:-1]}
            WHERE id={ID}
            """
        )


if __name__ == "__main__":
    sql = Database()
    sql.Select(231)
