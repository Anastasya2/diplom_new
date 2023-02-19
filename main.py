from ctypes import windll
import plyer as plyer

windll.user32.SetProcessDpiAwarenessContext(-4)

from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib

matplotlib.use('TkAgg', force=True)

from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 394)
Config.set("graphics", "height", 598)

import os.path
import mysql.connector
from kivymd.uix.list import OneLineListItem
import Other_classes
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from datetime import datetime
from threading import Timer
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MyApp(MDApp):
    user_sex = None
    noti = False

    food_data = {
        'График': 'chart-line',
        'Отчет за сутки': 'database-clock-outline',
        'Добавить': 'plus',
    }
    blood_pressure_data = {
        'График за неделю': 'chart-line',
        'График за месяц': 'chart-bell-curve',
        'График за все время': 'chart-bell-curve-cumulative',
    }
    glukosa_data = {
        'График за неделю': 'chart-line',
        'График за месяц': 'chart-bell-curve',
        'График за все время': 'chart-bell-curve-cumulative',
    }
    physics_data = {
        'График минут': 'chart-line',
        'График калорий': 'chart-bell-curve',
    }

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="111222333",
    )
    c = mydb.cursor()
    c.execute("USE app_db")
    c.execute("""CREATE TABLE if not exists food_days1 (days1 VARCHAR(50), GIs1 INT, XEs1 INT)""")
    mydb.commit()
    mydb.close()
    def food_buttons(self, instance):
        if instance.icon == 'chart-line':
            self.food_day_diagramm()
        elif instance.icon == 'database-clock-outline':
            self.consumed_food()
        elif instance.icon == 'plus':
            self.add_food_at_base()
    def food_day_diagramm(self):
        MDApp.get_running_app().root.current = "Piechart"
    def consumed_food(self):
        MDApp.get_running_app().root.current = "ten"
    def add_food_at_base(self):
        MDApp.get_running_app().root.current = "eleven"


    def blood_pressure_buttons(self, instance):
        if instance.icon == 'chart-line':
            self.blood_pressure_week_chart()
        elif instance.icon == 'chart-bell-curve':
            self.blood_pressure_month_chart()
        elif instance.icon == 'chart-bell-curve-cumulative':
            self.blood_pressure_all_time_chart()
    def blood_pressure_week_chart(self, *args):
        plt.clf()
        self.root.get_screen("forteen").ids.box.clear_widgets()

        MDApp.get_running_app().root.current = "forteen"

        box = self.root.get_screen("forteen").ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT bloodSis FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY blood.dat ASC")
            sis = c.fetchall()

            blood_sistol = []
            for i in sis:
                blood_sistol.append(i[0])

            c.execute("SELECT bloodDis FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY blood.dat ASC")
            dis = c.fetchall()
            blood_distol = []
            for i in dis:
                blood_distol.append(i[0])

            c.execute("SELECT dat FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY blood.dat ASC")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, blood_sistol, '#b8180d', marker='o', label="Sistolic")
            plt.plot(date_time, blood_distol, 'r', label="Diastolic", marker='o')
            plt.legend('', frameon=False)
            plt.xticks(rotation=40)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("давление", fontsize=10)
            plt.title("График давления за неделю")
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def blood_pressure_month_chart(self, *args):
        plt.clf()
        self.root.get_screen("fivteen").ids.box15.clear_widgets()

        MDApp.get_running_app().root.current = "fivteen"
        box2 = self.root.get_screen("fivteen").ids.box15
        box2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT bloodSis FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 1 MONTH) ORDER BY blood.dat ASC")
            sis = c.fetchall()

            blood_sistol = []
            for i in sis:
                blood_sistol.append(i[0])

            c.execute("SELECT bloodDis FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 1 MONTH) ORDER BY blood.dat ASC")
            dis = c.fetchall()
            blood_distol = []
            for i in dis:
                blood_distol.append(i[0])

            c.execute("SELECT dat FROM blood WHERE DATE(dat) > (NOW() - INTERVAL 1 MONTH) ORDER BY blood.dat ASC")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, blood_sistol, '#b8180d', marker='o', label="Sistolic")
            plt.plot(date_time, blood_distol, 'r', label="Diastolic", marker='o')
            plt.legend('', frameon=False)
            plt.xticks(rotation=40)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("давление", fontsize=10)
            plt.title("График давления за месяц")

            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def blood_pressure_all_time_chart(self, *args):
        plt.clf()
        self.root.get_screen("sixteen").ids.box16.clear_widgets()

        MDApp.get_running_app().root.current = "sixteen"

        box3 = self.root.get_screen("sixteen").ids.box16
        box3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT bloodSis FROM blood ORDER BY blood.dat ASC")
            sis = c.fetchall()

            blood_sistol = []
            for i in sis:
                blood_sistol.append(i[0])

            c.execute("SELECT bloodDis FROM blood ORDER BY blood.dat ASC")
            dis = c.fetchall()
            blood_distol = []
            for i in dis:
                blood_distol.append(i[0])

            c.execute("SELECT dat FROM blood ORDER BY blood.dat ASC")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, blood_sistol, '#b8180d', marker='o', label="Sistolic")
            plt.plot(date_time, blood_distol, 'r', label="Diastolic", marker='o')
            plt.legend('', frameon=False)
            plt.xticks(rotation=40)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("давление", fontsize=10)
            plt.title("График давления за все \nвремя использования приложения")

            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()


    def glukosa_buttons(self, instance):
        if instance.icon == 'chart-line':
            self.glukosa_week_chart()
        elif instance.icon == 'chart-bell-curve':
            self.glukosa_month_chart()
        elif instance.icon == 'chart-bell-curve-cumulative':
            self.glukosa_all_time_chart()
    def glukosa_week_chart(self, *args):
        plt.clf()
        self.root.get_screen("twenty").ids.box20.clear_widgets()

        MDApp.get_running_app().root.current = "twenty"

        box = self.root.get_screen("twenty").ids.box20
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT glu_level FROM glukosa WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY)")
            glukos = c.fetchall()

            glukosa_in_week = []
            for i in glukos:
                glukosa_in_week.append(i[0])

            c.execute("SELECT dat FROM glukosa WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY)")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, glukosa_in_week, '#b8180d', marker='o', label="glukosa")
            plt.xticks(rotation=40)
            plt.legend('', frameon=False)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("глюкоза", fontsize=10)
            plt.title("График уровня глюкозы за неделю")

            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def glukosa_month_chart(self, *args):
        plt.clf()
        self.root.get_screen("twentyone").ids.box21.clear_widgets()

        MDApp.get_running_app().root.current = "twentyone"

        box = self.root.get_screen("twentyone").ids.box21
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT glu_level FROM glukosa WHERE DATE(dat) > (NOW() - INTERVAL 1 MONTH)")
            glukos = c.fetchall()

            glukosa_in_month = []
            for i in glukos:
                glukosa_in_month.append(i[0])

            c.execute("SELECT dat FROM glukosa WHERE DATE(dat) > (NOW() - INTERVAL 1 MONTH)")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, glukosa_in_month, '#b8180d', marker='o', label="glukosa")
            plt.xticks(rotation=40)
            plt.legend('', frameon=False)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("глюкоза", fontsize=10)
            plt.title("График уровня глюкозы за месяц")
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def glukosa_all_time_chart(self, *args):
        plt.clf()
        self.root.get_screen("twentytwo").ids.box22.clear_widgets()

        MDApp.get_running_app().root.current = "twentytwo"

        box = self.root.get_screen("twentytwo").ids.box22
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT glu_level FROM glukosa")
            glukosa = c.fetchall()

            glukosa_all_time = []
            for i in glukosa:
                glukosa_all_time.append(i[0])

            c.execute("SELECT dat FROM glukosa")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, glukosa_all_time, '#b8180d', marker='o', label="glukosa")
            plt.xticks(rotation=40)
            plt.legend('', frameon=False)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("глюкоза", fontsize=10)
            plt.title("График уровня глюкозы за все \nвремя использования приложения")
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()


    def physical_activity_buttons(self, instance):
        if instance.icon == 'chart-line':
            self.chart_minutes_for_physical_activity()
        elif instance.icon == 'chart-bell-curve':
            self.chart_calories_for_physical_activity()
    def chart_minutes_for_physical_activity(self, *args):
        plt.clf()
        self.root.get_screen("eighteen").ids.physic.clear_widgets()

        MDApp.get_running_app().root.current = "eighteen"

        phyact = self.root.get_screen("eighteen").ids.physic
        phyact.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT timeact FROM physics WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY physics.dat ASC")
            phys_activity = c.fetchall()

            act_for_week = []
            for phytime in phys_activity:
                act_for_week.append(phytime[0])

            c.execute("SELECT dat FROM physics WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY physics.dat ASC")
            date_of_phy = c.fetchall()
            date_time = []

            for i_date in date_of_phy:
                date_time.append(i_date[0])

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, act_for_week, '#b8180d', marker='o')
            plt.xticks(rotation=40)
            plt.legend('', frameon=False)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("минуты", fontsize=10)
            plt.title("График минут, затраченных  на \nфизическую активность за неделю")
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def chart_calories_for_physical_activity(self, *args):
        plt.clf()
        self.root.get_screen("twentyfour").ids.physic2.clear_widgets()

        MDApp.get_running_app().root.current = "twentyfour"

        phyact = self.root.get_screen("twentyfour").ids.physic2
        phyact.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT calorii FROM physics_cal WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY physics_cal.dat ASC")
            calorii_of_phys = c.fetchall()

            calorii = []
            for i in calorii_of_phys:
                calorii.append(i[0])



            c.execute("SELECT dat FROM physics_cal WHERE DATE(dat) > (NOW() - INTERVAL 7 DAY) ORDER BY physics_cal.dat ASC")
            cal_date = c.fetchall()
            date_time = []
            for i in cal_date:
                date_time.append(i[0])

            format_date = mdates.DateFormatter('%d-%m')
            x_ticks = date_time
            x_labels = date_time
            plt.xticks(ticks=x_ticks, labels=x_labels)
            plt.plot(date_time, calorii, '#b8180d', marker='o')
            plt.xticks(rotation=40)
            plt.legend('', frameon=False)
            plt.gca().xaxis.set_major_formatter(format_date)
            plt.ylabel("калории", fontsize=10)
            plt.title("График калорий, потраченных во время \nфизической активности за неделю")
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()


    def chart_glukosa_xe(self, *args):
        plt.clf()
        self.root.get_screen("twentyfive").ids.box242.clear_widgets()

        MDApp.get_running_app().root.current = "twentyfive"

        box = self.root.get_screen("twentyfive").ids.box242
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT xe FROM food_xe  INNER JOIN glukosa ON food_xe.dat = glukosa.dat")
            glukos = c.fetchall()

            glukosa = []
            for i in glukos:
                glukosa.append(i[0])

            c.execute("SELECT glu_level FROM food_xe  INNER JOIN glukosa ON food_xe.dat = glukosa.dat")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            plt.plot(date_time, glukosa, '#b8180d', marker='o', label="glukosa")
            plt.legend('', frameon=False)
            plt.xticks(rotation=40)
            plt.ylabel("глюкоза", fontsize=10)
            plt.xlabel("хе", fontsize=10)
            plt.title("График зависимости глюкозы от ХЕ")
            plt.gca()

            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def chart_glukosa_physical_activity(self, *args):
        plt.clf()
        self.root.get_screen("twentysix").ids.box26.clear_widgets()

        MDApp.get_running_app().root.current = "twentysix"

        box = self.root.get_screen("twentysix").ids.box26
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("SELECT calorii FROM physics_cal  INNER JOIN glukosa ON physics_cal.dat = glukosa.dat")
            glukos = c.fetchall()

            glukosa = []
            for i in glukos:
                glukosa.append(i[0])

            c.execute("SELECT glu_level FROM physics_cal  INNER JOIN glukosa ON physics_cal.dat = glukosa.dat")
            dat = c.fetchall()
            date_time = []
            for i in dat:
                date_time.append(i[0])

            o = [1, 2, 3]

            plt.plot(date_time, glukosa, '#b8180d', marker='o', label="glukosa")
            plt.legend('', frameon=False)
            plt.xticks(rotation=40)
            plt.ylabel("глюкоза", fontsize=10)
            plt.xlabel("физ активность", fontsize=10)
            plt.title("График зависимости глюкозы \nот физической активности")
            plt.gca()
            mydb.commit()
            mydb.close()
        except:
            print('add values')
            mydb.commit()
            mydb.close()
    def chart_blood_pressure_glukosa(self, *args):
        plt.clf()
        self.root.get_screen("twentyseven").ids.box27.clear_widgets()

        MDApp.get_running_app().root.current = "twentyseven"

        box = self.root.get_screen("twentyseven").ids.box27
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()
        c.execute("USE app_db")
        c.execute("SELECT CAST((bloodSis/bloodDis) AS SIGNED) FROM blood  INNER JOIN glukosa ON blood.dat = glukosa.dat ORDER BY blood.dat ASC")
        glukos = c.fetchall()[0]

        glukosa = []

        c.execute("SELECT bloodDis FROM blood  INNER JOIN glukosa ON blood.dat = glukosa.dat ORDER BY blood.dat ASC")
        glukos2 = c.fetchall()

        for i in glukos:
            glukosa.append(i)

        c.execute("SELECT glu_level FROM blood  INNER JOIN glukosa ON blood.dat = glukosa.dat")
        dat = c.fetchall()[0]
        date_time = []
        for i in dat:
            date_time.append(i)

        o = [1, 2, 3]

        plt.plot(date_time,glukosa,  '#b8180d', marker='o', label="glukosa")
        plt.legend('', frameon=False)
        plt.xticks(rotation=40)
        plt.ylabel("давление", fontsize=10)
        plt.xlabel("глюкоза", fontsize=10)
        plt.title("График зависимости давления \nот глюкозы")
        plt.gca()

        mydb.commit()
        mydb.close()

    def foo(self, item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="111222333",
        )
        c = mydb.cursor()
        c.execute("USE app_db")
        c.execute("""CREATE TABLE if not exists food_days1 (days1 VARCHAR(50), GIs1 INT, XEs1 INT)""")

        sql_command3 = "INSERT INTO food_days1 (days1) VALUES (%s)"
        values = (item.text,)

        c.execute(sql_command3, values)
        print(item.id)

        self.root.get_screen("ten").ids.container1.clear_widgets()

        c.execute("SELECT days1 FROM food_days1")
        records = c.fetchall()
        word = ''

        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.get_screen("ten").ids.container1.add_widget(
                OneLineListItem(text=f'{word}')
            )

            word = ''

        query = "SELECT CAST(SUM(XE) AS SIGNED) FROM food INNER JOIN food_days1 ON food.name = food_days1.days1"

        c.execute(query)

        self.sum1 = c.fetchall()[0]
        print(int(self.sum1[0]))
        if (int(self.sum1[0]) > 30):
            notify3()


        mydb.commit()
        mydb.close()
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
            wor = word + word1 + word2
            self.root.get_screen("twelve").ids.container.add_widget(
                MDRectangleFlatButton(text=record[0], size_hint={1, .15}, text_color=(0, 0, 0, 1),
                                      line_color=(0, 0, 0, 1), halign='left', on_release=self.foo)

            )

            word = ''
            word1 = ''
            word2 = ''
        c.execute("USE app_db")
        c.execute("""CREATE TABLE if not exists food_days1 (days1 VARCHAR(50), GIs1 VARCHAR(50), XEs1 VARCHAR(50))""")

        c.execute("SELECT days1 FROM food_days1")
        records = c.fetchall()
        word = ''

        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.get_screen("ten").ids.container1.add_widget(
                OneLineListItem(text=f'{word}')
            )
            word = ''

        if not self.root.get_screen("seven").ids.hero_list.children:
            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Nutrition(source="food.png", tag=f"Tag{0}", on_touch_down=self.on_tap_card_nutrition)
            )

            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Glukosa(source="glukosa.png", tag=f"Tag{4}", on_touch_down=self.on_tap_card_glukosa)
            )
            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Physics(source="physics.png", tag=f"Tag{1}", on_touch_down=self.on_tap_card_physics)
            )
            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Blood_Pressure(source="blood_pressure.png", tag=f"Tag{2}", on_touch_down=self.on_tap_card_blood_pressure)

            )
            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Meds(source="meds.png", tag=f"Tag{3}", on_touch_down=self.on_tap_card_meds)
            )
            self.root.get_screen("seven").ids.hero_list.add_widget(
                Other_classes.HeroCard_Statistics(source="stat.png", tag=f"Tag{5}", on_touch_down=self.on_tap_card_statistics)
            )


        mydb.commit()
        mydb.close()

    def on_tap_card_nutrition(self, *args):
        MDApp.get_running_app().root.current = "twelve"
    def on_tap_card_physics(self, *args):
        MDApp.get_running_app().root.current = "nine"
    def on_tap_card_blood_pressure(self, *args):
        MDApp.get_running_app().root.current = "thirteen"
    def on_tap_card_meds(self, *args):
        MDApp.get_running_app().root.current = "seventeen"
    def on_tap_card_glukosa(self, *args):
        MDApp.get_running_app().root.current = "nineteen"
    def on_tap_card_statistics(self, *args):
        MDApp.get_running_app().root.current = "twentythree"


    def back_to_window_five(self):
        MDApp.get_running_app().root.current = "five"
    def back_to_window_six(self):
        MDApp.get_running_app().root.current = "six"
    def back_to_window_seven(self, *args):
        MDApp.get_running_app().root.current = "seven"
    def back_to_window_nine(self):
        MDApp.get_running_app().root.current = "nine"
    def back_to_window_twelve(self):
        MDApp.get_running_app().root.current = "twelve"
    def back_to_window_thirteen(self):
        MDApp.get_running_app().root.current = "thirteen"
    def back_to_window_nineteen(self):
        MDApp.get_running_app().root.current = "nineteen"
    def back_to_window_twentythree(self):
        MDApp.get_running_app().root.current = "twentythree"


    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"

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

        kv = Builder.load_file('Autorization.kv')
        kv1 = Builder.load_file('Main_part.kv')
        kv2 = Builder.load_file('Main_part2.kv')

        if os.path.exists('first_launch.txt'):
            return kv2
        else:
            with open("first_launch.txt", 'w') as myfile:
                myfile.write('The application has been launched.')
        return kv

    def logger(self):
        try:

            self.fname = self.root.get_screen('five').ids.firstname.text
            self.sname = self.root.get_screen('five').ids.secondname.text

            self.root.get_screen('six').ids.welcome1_label.text = f'Mне нужно еще немного информации о тебе'

            Other_classes.EightWindow.log1(self, self.user_sex)

        except:
            show_popup(self)
            self.back_to_window_five()
    def logger1(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists user (sex VARCHAR(50), age INT, height INT, weight INT)""")

            self.age = self.root.get_screen('six').ids.age.text
            self.height = self.root.get_screen('six').ids.height.text
            self.weight = self.root.get_screen('six').ids.weight.text
            sql_request = "INSERT INTO user (age, height, weight, sex) VALUES (%s, %s, %s,%s)"
            values = (self.age, self.height, self.weight, self.user_sex)

            c.execute(sql_request, values)

            Other_classes.EightWindow.log(self, self.age, self.height, self.weight)
            mydb.commit()
            mydb.close()
            MDApp.get_running_app().root.current = "seven"
        except:
            show_popup(self)
            self.back_to_window_six()
    def bloodlog(self):
        try:
            self.bls = self.root.get_screen('thirteen').ids.blood1.text
            self.bld = self.root.get_screen('thirteen').ids.blood2.text

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists blood (bloodSis INT, bloodDis INT, dat DATE)""")

            c.execute(f"""INSERT INTO blood (bloodSis, bloodDis,dat) VALUES ({self.bls}, {self.bld},CURDATE())""")

            self.root.get_screen("thirteen").ids.blood1.text = ''
            self.root.get_screen("thirteen").ids.blood2.text = ''

            mydb.commit()
            mydb.close()
        except:
            show_popup(self)
    def medlog(self):
        try:
            self.meds = self.root.get_screen('seventeen').ids.meds.text
            self.edn = self.root.get_screen('seventeen').ids.edn.text
            self.doza = self.root.get_screen('seventeen').ids.doz.text

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists meds (med_name VARCHAR(50), ed_izm VARCHAR(50), doza VARCHAR(50))""")

            sql_command = "INSERT INTO meds (med_name, ed_izm, doza) VALUES (%s, %s, %s)"
            values = (self.root.get_screen("seventeen").ids.meds.text, self.root.get_screen("seventeen").ids.edn.text,
                      self.root.get_screen("seventeen").ids.doz.text,)

            c.execute(sql_command, values)

            self.root.get_screen("seventeen").ids.meds.text = ''
            self.root.get_screen("seventeen").ids.edn.text = ''
            self.root.get_screen("seventeen").ids.doz.text = ''

            mydb.commit()
            mydb.close()
        except:
            show_popup(self)
    def physlog(self):
        try:
            self.phy = self.root.get_screen('nine').ids.pa.text


            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists physics (timeact INT, dat DATE)""")

            c.execute(f"""INSERT INTO physics (timeact, dat) VALUES ({self.phy}, CURDATE())""")

            self.root.get_screen("nine").ids.pa.text = ''


            mydb.commit()
            mydb.close()
        except:
            show_popup(self)
    def physlog2(self):
        try:
            self.phy = self.root.get_screen('nine').ids.pa2.text


            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists physics_cal (calorii INT, dat DATE)""")

            c.execute(f"""INSERT INTO physics_cal (calorii, dat) VALUES ({self.phy}, CURDATE())""")

            self.root.get_screen("nine").ids.pa2.text = ''

            mydb.commit()
            mydb.close()
        except:
            show_popup(self)
    def glulog(self):
        try:
            self.glu = self.root.get_screen('nineteen').ids.glukosa.text

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )
            c = mydb.cursor()
            c.execute("USE app_db")
            c.execute("""CREATE TABLE if not exists glukosa (glu_level VARCHAR(50), dat DATE)""")

            c.execute(f"""INSERT INTO glukosa (glu_level, dat) VALUES ({self.glu}, CURDATE())""")

            self.root.get_screen("nineteen").ids.glukosa.text = ''

            mydb.commit()
            mydb.close()
        except:
            show_popup(self)

    def clear_five_window(self):
        self.root.get_screen('five').ids.firstname.text = ""
        self.root.get_screen('five').ids.secondname.text = ""
        self.root.get_screen('five').ids.check.active = False
        self.root.get_screen('five').ids.check2.active = False
    def clear_six_window(self):
        self.root.get_screen('six').ids.age.text = ""
        self.root.get_screen('six').ids.height.text = ""
        self.root.get_screen('six').ids.weight.text = ""
    def clear_eleven_window(self):
        self.root.get_screen('eleven').ids.dbname.text = ""
        self.root.get_screen('eleven').ids.dbgi.text = ""
        self.root.get_screen('eleven').ids.dbxe.text = ""

    def checkbox_click(self, instance, value, sex):

        if value:
            self.user_sex = sex
        else:
            self.user_sex = None
    def add_food_to_bd(self):

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="111222333",
            )

            c = mydb.cursor()

            c.execute("USE app_db")

            self.root.get_screen("twelve").ids.container.clear_widgets()

            sql_command = "INSERT INTO food (name, GI, XE) VALUES (%s, %s, %s)"
            values = (self.root.get_screen("eleven").ids.dbname.text, self.root.get_screen("eleven").ids.dbgi.text,
                      self.root.get_screen("eleven").ids.dbxe.text,)

            c.execute(sql_command, values)

            self.root.get_screen('eleven').ids.dbname.text = ""
            self.root.get_screen('eleven').ids.dbgi.text = ""
            self.root.get_screen('eleven').ids.dbxe.text = ""

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
                wor = word + word1 + word2
                self.root.get_screen("twelve").ids.container.add_widget(
                    MDRectangleFlatButton(text=record[0],
                                          size_hint={1, .15}, text_color=(1 / 255, 45 / 255, 80 / 255, 1),
                                          line_color=(1 / 255, 45 / 255, 80 / 255, 1), halign='left',
                                          on_release=self.foo)

                )

                word = ''
                word1 = ''
                word2 = ''

            mydb.commit()
            mydb.close()
        except:
            print('add values')
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




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="111222333",
)
c = mydb.cursor()
c.execute("USE app_db")
c.execute("""SELECT med_name FROM meds""")
medd = c.fetchall()[0]
medd = medd[0]
c.execute("""SELECT ed_izm FROM meds""")
ed = c.fetchall()[0]
ed = ed[0]
c.execute("""SELECT doza FROM meds""")
doz = c.fetchall()[0]
doz = doz[0]

mydb.commit()
mydb.close()


def notify():
    plyer.notification.notify(title='Напоминание', message=f'Примите {medd} {doz} {ed} ')
    tim()
def notify2():
    plyer.notification.notify(title='Напоминание', message=f'Не забудьте о физических упражнениях')
    tim2()

def notify3():
    plyer.notification.notify(title='Предупреждение', message=f'Превышена норма хлебных единиц')
    tim()
def tim():
    x = datetime.today()
    y = x.replace(day=x.day, hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t = y - x
    secs = delta_t.total_seconds()
    t = Timer(secs, notify)

def tim2():
    x1 = datetime.today()
    y1 = x1.replace(day=x1.day, hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t1 = y1 - x1
    secs1 = delta_t1.total_seconds()
    t1 = Timer(secs1, notify2)
    t1.start()



x = datetime.today()
y = x.replace(day=x.day, hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t = y - x

secs = delta_t.total_seconds()
t = Timer(secs, notify)
t.start()




x1 = datetime.today()
y1 = x1.replace(day=x1.day, hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t1 = y1 - x1

secs1 = delta_t1.total_seconds()
t1 = Timer(secs1, notify2)
t1.start()


def show_popup(self):
    show = Other_classes.Popups()

    popupWindow = Popup(title="Неверно введены данные", content=Label(text='Попробуйте снова'),
                        size_hint=(None, None), size=(270, 110))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()
