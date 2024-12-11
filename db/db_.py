import sqlalchemy as db
import os


class Database_admin:
    def __init__(self):
        self.meta = db.MetaData()
        self.engine = db.create_engine('sqlite:///admin_database.db')
        self.product = db.Table('Admin_database', self.meta,
                           db.Column('id', db.Integer, primary_key=True),
                           db.Column('name', db.Text),
                           db.Column('password', db.Text))
        if os.path.exists("git_project/admin_database.db"):
            self.__create_database()

    def __create_database(self):
        try:
            engine = db.create_engine('sqlite:///admin_database.db')
            connection = engine.connect()
            meta = db.MetaData()
            meta.create_all(engine)
            connection.commit()

        except BaseException as e:
            return e.__class__

        finally:
            connection.close()

    def add_registration_admin(self, name, password):
        try:
            engine = db.create_engine('sqlite:///admin_database.db')
            connection = engine.connect()
            insert = self.product.insert().values([
                {'name': name,
                 'password': password}])
            connection.execute(insert)
            connection.commit()
        finally:
            connection.close()

    def is_registration_admin(self, name, password):
        select_query = db.select(self.product)
        with self.engine.connect() as connection:
            result = connection.execute(select_query)
            for admin in result:
                if admin[1] == name and admin[2] == password:
                    return True
                else:
                    return False


a = Database_admin()
a.add_registration_admin()
a1 = a.is_registration_admin("Roma", "kele1245")
print(a1)