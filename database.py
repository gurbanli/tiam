import pymysql
from hashlib import sha1
class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "admin"
        password = "KsV79n#tiam"
        db = "tiam"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def add_student(self,name,gender,email,phone,field,uni,spec):
        data = (name,gender,email,phone,field,uni,spec,)
        try:
            self.cur.execute("insert into Students (name,gender,email,phone,field,uni,spec) values (%s,%s,%s,%s,%s,%s,%s)",(data))
            self.con.commit()
        except Exception as e:
            print(e)
    def check_admin(self,username,password):
        try:
            password = password.encode('utf-8')
            password = sha1(password).hexdigest()
            if self.cur.execute("select * from users where username=%s and password=%s",(username,password,)):
                return True
            else:
                return False
        except Exception as e:
            print(e)
    def get_students(self):
        try:
            self.cur.execute("Select * from Students")
            records = self.cur.fetchall()
            return records
        except Exception as e:
            print(e)
db = Database()
for student in db.get_students():
    print(student)


