import sqlite3

class StaffRepository:
    def __init__ (self):
        self.staffConnect = sqlite3.connect('staff.db')
        self.staffCursor = self.staffConnect.cursor()
    def onClose(self):
        self.staffConnect.close()
    def creatTable(self):
        createRequest = """
            CREATE TABLE staff (
                id integer,
                code text,
                name text,
                shop text,
                createTime timeStamp,
                updateTime timeStamp
            )
        """
        self.staffCursor.execute(createRequest)
        self.staffConnect.commit()
    def insertTable(self):
        insertRequest = """
            INSERT INTO staff VALUES (
                'tuan anh',
                'hust',
                2020
            )
        """

staffRepository = StaffRepository()
checkEmpty = staffRepository.staffCursor.fetchone()

if checkEmpty is None:
    staffRepository.creatTable()
else:
    staffRepository