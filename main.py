from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 324)
Config.set("graphics", "height", 491)

from kivy.lang import Builder
from kivymd.app import MDApp
import os.path
import mysql.connector
from kivymd.uix.list import OneLineListItem
import My


class MyApp(MDApp):
    user_sex = None

    def on_start(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()
        c.execute("USE app_db")

        c.execute("SELECT name FROM food ORDER BY name")
        records = c.fetchall()

        c.execute("SELECT GI FROM food ORDER BY name")
        GIS = c.fetchall()

        c.execute("SELECT XE FROM food ORDER BY name")
        XES = c.fetchall()

        word = ''
        word1 = ''
        word2 = ''

        for record, Gi, Xe in zip(records, GIS, XES):
            word = f'{word}\n{record[0]}'
            word1 = f'{word1}\n{Gi[0]}'
            word2 = f'{word2}\n{Xe[0]}'
            self.root.get_screen("ten").ids.container.add_widget(
                OneLineListItem(text=f'{word}, ГИ = {word1}, ХЕ = {word2}')
            )
            word = ''
            word1 = ''
            word2 = ''

        mydb.commit()
        mydb.close()

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()

        c.execute("CREATE DATABASE IF NOT EXISTS app_db")
        c.execute("USE app_db")

        c.execute("""CREATE TABLE if not exists food (name VARCHAR(50), GI INTEGER, XE INTEGER)""")

        mydb.commit()

        mydb.close()

        kv = Builder.load_file('My.kv')
        kv1 = Builder.load_file('My1.kv')
        kv2 = Builder.load_file('My2.kv')

        if os.path.exists('1.txt'):
            return kv2
        else:
            myfile = open("1.txt", 'w')
            myfile.write('1')
            myfile.close()
        return kv

    def submit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()

        c.execute("USE app_db")

        sql_command = "INSERT INTO food (name, GI, XE) VALUES (%s, %s, %s)"
        values = (self.root.get_screen("eleven").ids.dbname.text, self.root.get_screen("eleven").ids.dbgi.text,
                  self.root.get_screen("eleven").ids.dbxe.text,)

        c.execute(sql_command, values)

        # self.root.get_screen("ten").ids.word_input.text = ""

        mydb.commit()
        mydb.close()

    def show(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()
        c.execute("USE app_db")

        c.execute("SELECT * FROM food")
        records = c.fetchall()

        word = ''

        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.get_screen("ten").ids.word_input.text = f'{word}'

        mydb.commit()
        mydb.close()

    def logger(self):
        self.fname = self.root.get_screen('five').ids.firstname.text
        self.sname = self.root.get_screen('five').ids.secondname.text
        print(My.FiveWindow)
        print(self.fname)
        print(self.sname)
        print(self.user_sex)
        self.root.get_screen(
            'six').ids.welcome1_label.text = f'Hey, {self.root.get_screen("five").ids.firstname.text}, I need a little more information about you'

    def logger1(self):
        self.age = self.root.get_screen('six').ids.age.text
        self.height = self.root.get_screen('six').ids.height.text
        self.weight = self.root.get_screen('six').ids.weight.text
        print(self.age)
        print(self.height)
        print(self.weight)

    def clear(self):
        self.root.get_screen('five').ids.firstname.text = ""
        self.root.get_screen('five').ids.secondname.text = ""
        self.root.get_screen('five').ids.check.active = False
        self.root.get_screen('five').ids.check2.active = False

    def clear1(self):
        self.root.get_screen('six').ids.age.text = ""
        self.root.get_screen('six').ids.height.text = ""
        self.root.get_screen('six').ids.weight.text = ""

    def clear2(self):
        self.root.get_screen('eleven').ids.dbname.text = ""
        self.root.get_screen('eleven').ids.dbgi.text = ""
        self.root.get_screen('eleven').ids.dbxe.text = ""

    def checkbox_click(self, instance, value, sex):

        if value:
            self.user_sex = sex
        else:
            self.user_sex = None


if __name__ == "__main__":
    MyApp().run()
