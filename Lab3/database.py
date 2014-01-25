import sqlite3
import my_forms

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.create_table()
        self.nusers = (self.conn.execute("select max(rowid) from users").fetchone()[0] or 0)

    def create_table(self):
        self.conn.execute("""
    CREATE TABLE if not exists USERS
    (
        name TEXT,
        surname TEXT,
        email TEXT PRIMARY KEY NOT NULL,
        country TEXT,
        city TEXT,
        referrer int,
        othertext TEXT
        );
        """)

    def reset(self):
        self.conn.execute("drop table if exists users")
        self.create_table()

    def users(self):
        return self.nusers

    def __del__(self):
        self.conn.close()

    def create_user(self, form_data):
        cmd = "insert into users values (?,?,?,?,?,?,?)"
        curs = self.conn.cursor()

        referrer = 0
        for i, value in enumerate(my_forms.RegistrationForm.refList):
            referrer += (2**i if form_data[value] else 0)
        try:
            curs.execute(cmd, (form_data['name'], form_data['surname'], form_data['email'], form_data['country'], form_data['city'], referrer, form_data['refOtherText']))
        except sqlite3.IntegrityError:
            return False

        self.conn.commit()
        self.nusers += 1

if __name__ == '__main__':
    db = Database()
    db.create_user({'name': "Gustav", "surname": "Bylund", "email": "mai2123tho2@gmail.com", "country": "Sweden", "referrer": 1, "city": "Linkoping", "refOtherText": "kitten"})
    print(db.nusers)
