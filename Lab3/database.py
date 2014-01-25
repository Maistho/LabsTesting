import sqlite3
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.nusers = int(self.conn.cursor().execute("select * from users").rowcount)

    def __del__(self):
        self.conn.close()

    def create_user(self, name, surname, email, country, city, friend=False, google=False, facebook=False, twitter=False, search_engine=False, othertext=None):
        cmd = "insert into users values (?,?,?,?,?,?,?)"
        curs = self.conn.cursor()

        try:
            curs.execute(cmd, (name, surname, email, country, city, 1, othertext))
        except sqlite3.IntegrityError:
            # Return error
            pass

        self.conn.commit()
        #self.nusers += 1

if __name__ == '__main__':
    db = Database()
    db.create_user("Gustav", "Bylund", "maistho2@gmail.com", "Sweden", "Linkoping", google=True, twitter=True)
    print(db.nusers)
