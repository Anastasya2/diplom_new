from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd_extensions.akivymd.uix.charts import AKPieChart

import Other_classes

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 324)
Config.set("graphics", "height", 491)

from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.templates import RotateWidget
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty
import sqlite3


class Popups(FloatLayout):
    pass


class ElevationCard(FakeRectangularElevationBehavior, MDCard):
    pass


class HeroCard_Nutrition(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_Physics(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_Blood_Pressure(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_Meds(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_Glukosa(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_Statistics(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_xe_calculator(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_info(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_diabet(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_diapozon_sugar(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_symptoms(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_lechenie(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_diagnostica(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_first_help(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()

class HeroCard_profilactica(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class HeroCard_calculator_in(ElevationCard):
    source = StringProperty()
    tag = StringProperty()
    manager = ObjectProperty()


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThreeWindow(Screen):
    pass


class FourWindow(Screen):
    pass


class FiveWindow(MDScreen):
    pass


class SixWindow(MDScreen):
    pass


class SevenWindow(MDScreen):
    pass


class EightWindow(MDScreen):

    conn = sqlite3.connect('diabet.db')
    cursor = conn.cursor()

    cursor.execute("SELECT age FROM user")
    age = cursor.fetchall()[0]

    cursor.execute("SELECT height FROM user")
    hei = cursor.fetchall()[0]

    cursor.execute("SELECT weight FROM user")
    wei = cursor.fetchall()[0]

    age = float(age[0])
    hei = float(hei[0])
    weight = float(wei[0])
    cursor.execute("SELECT sex FROM user")
    se = cursor.fetchall()[0]
    sex = se[0]

    conn.commit()
    conn.close()

    sex = None
    age = 1
    hei = float(1)
    weight = float(1)

    def log(self, age, height, weight):

        EightWindow.age = float(age)
        EightWindow.hei = float(height)
        EightWindow.weight = float(weight)
    def log1(self, sex):

        EightWindow.sex = sex


    def set_screen(self):
        MDApp.get_running_app().root.current = "twelve"
        self.remove_chart()

    try:

        ind = float(weight / (hei * hei) * 10000)

        al = 20

        if (ind < 18.5) and (age > 18):
            al = 30
        elif (ind >= 18.5) and (age > 18):
            al = 20
        elif (age > 4) and (age < 6):
            al = 13
        elif (age > 7) and (age < 10):
            al = 16
        elif (age > 11) and (age < 14) and (sex == "female"):
            al = 17
        elif (age > 11) and (age < 14) and (sex == "male"):
            al = 20
        elif (age > 15) and (age < 18) and (sex == "female"):
            al = 18
        elif (age > 15) and (age < 18) and (sex == "male"):
            al = 21
        else:
            al = 20

        conn = sqlite3.connect('diabet.db')
        cursor = conn.cursor()

        query = "SELECT CAST(SUM(XE) AS SIGNED) FROM food INNER JOIN food_days1 ON food.name = food_days1.days1"

        cursor.execute(query)



        sum1 = cursor.fetchall()[0]
        sum1 = sum1[0]
        sum1 = float(sum1)
        all = float(al)
        my = float(100)
        new = float((sum1 * my) / all)
        ost = my - new

        if new < 100:
            items = [{"За этот день": new, "Норма": ost}]
        elif new >= 100:
            items = [{"За этот день": 100, "Норма": 0}]

        conn.commit()
        conn.close()
    except:
        conn.commit()
        conn.close()

        items = [{"За этот день": 0, "Норма": 100}]

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):

        self.piechart = AKPieChart(
            items=self.items,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=[None, None],
            size=(dp(300), dp(300)),

        )
        try:
            self.ids.chart_box.add_widget(self.piechart)
            self.ids.wel.text = f'Сегодня употреблено: {int(self.sum1)} ХЕ'
            self.ids.wel1.text = f'Норма ХЕ: {int(self.al)}'
        except:
            self.ids.wel.text = f'Сегодня употреблено: 0 ХЕ'
            self.ids.wel1.text = f'Норма ХЕ: {int(self.al)}'

    def update_chart(self):
        self.ids.wel.text = ' '

        if (EightWindow.ind < 18.5) and (EightWindow.age > 18):
            EightWindow.al = 30
        elif (EightWindow.ind >= 18.5) and (EightWindow.age > 18):
            EightWindow.al = 20
        elif (EightWindow.age > 4) and (EightWindow.age < 6):
            EightWindow.al = 13
        elif (EightWindow.age > 7) and (EightWindow.age < 10):
            EightWindow.al = 16
        elif (EightWindow.age > 11) and (EightWindow.age < 14) and (EightWindow.sex == "female"):
            EightWindow.al = 17
        elif (EightWindow.age > 11) and (EightWindow.age < 14) and (EightWindow.sex == "male"):
            EightWindow.al = 20
        elif (EightWindow.age > 15) and (EightWindow.age < 18) and (EightWindow.sex == "female"):
            EightWindow.al = 18
        elif (EightWindow.age > 15) and (EightWindow.age < 18) and (EightWindow.sex == "male"):
            EightWindow.al = 21
        else:
            EightWindow.al = 20

        try:

            conn = sqlite3.connect('diabet.db')
            cursor = conn.cursor()

            query = "SELECT CAST(SUM(XE) AS SIGNED) FROM food INNER JOIN food_days1 ON food.name = food_days1.days1"

            cursor.execute(query)

            sum1 = cursor.fetchall()[0]
            sum1 = sum1[0]
            sum1 = float(sum1)
            all = float(EightWindow.al)
            my = float(100)
            new = float((sum1 * my) / all)
            ost = my - new

            if new < 100:
                self.piechart.items = [{"За этот день": new, "Норма": ost}]
            elif new >= 100:
                self.piechart.items = [{"За этот день": 100, "Норма": 0}]

            self.ids.wel.text = f'Сегодня употреблено: {int(sum1)} ХЕ'



            conn.commit()
            conn.close()

        except:
            conn.commit()
            conn.close()

            self.piechart.items = [{"За этот день": 0, "Норма": 100}]
            try:
                self.ids.wel.text = f'Сегодня употреблено: {int(sum1)} ХЕ'
            except:
                self.ids.wel.text = f'Сегодня употреблено: 0 ХЕ'

    def remove_chart(self):
        self.ids.chart_box.remove_widget(self.piechart)
        self.ids.wel.text = ''


class NineWindow(MDScreen):
    pass


class TenWindow(MDScreen):

    def one(self):
        self.add_widget(GridLayout(cols=1, spacing=10, size_hint_y=None))

        for i in range(10):
            self.btn = MDRaisedButton(text=str(i), size_hint_y=None, height=40)
            self.add_widget(self.btn)



class ElevenWindow(MDScreen):

    def show_popup(self, item):
        show = Other_classes.Popups()

        popupWindow = Popup(title="Введите граммы", content=show,
                            size_hint=(None, None), size=(300, 163))
        self.gram = self.root.get_screen("twelve").ids.gr.text

        popupWindow.open()


class TwelveWindow(MDScreen):

    def show_popup(self, item):
        show = Other_classes.Popups()

        popupWindow = Popup(title="Введите граммы", content=show,
                            size_hint=(None, None), size=(300, 163))
        self.gram = self.root.get_screen("twelve").ids.gr.text

        popupWindow.open()


class ThirteenWindow(MDScreen):
    pass


class ForteenWindow(MDScreen):
    pass


class FivteenWindow(MDScreen):
    pass


class SixteenWindow(MDScreen):
    pass


class SeventeenWindow(MDScreen):
    pass

class EighteenWindow(MDScreen):
    pass


class NineteenWindow(MDScreen):
    pass


class TwentyWindow(MDScreen):
    pass

class TwentyOneWindow(MDScreen):
    pass

class TwentyTwoWindow(MDScreen):
    pass

class TwentyThreeWindow(MDScreen):
    pass

class TwentyFourWindow(MDScreen):
    pass


class TwentyFiveWindow(MDScreen):
    pass

class TwentySixWindow(MDScreen):
    pass

class TwentySevenWindow(MDScreen):
    pass


class TwentyEightWindow(MDScreen):
    pass

class TwentyNineWindow(MDScreen):
    pass

class ThirtyWindow(MDScreen):
    pass

class ThirtyOneWindow(MDScreen):
    pass

class ThirtyTwoWindow(MDScreen):
    pass

class ThirtyThreeWindow(MDScreen):
    pass

class ThirtyFourWindow(MDScreen):
    pass

class ThirtyFiveWindow(MDScreen):
    pass

class ThirtySixWindow(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class RootButton(MDFloatingActionButton, RotateWidget):
    pass


class Content(BoxLayout):
    pass

def show_popup(self, item):
    show = Other_classes.Popups()

    popupWindow = Popup(title="Введите граммы", content=show,
                        size_hint=(None, None), size=(300, 163))
    self.gram = self.root.get_screen("twelve").ids.gr.text

    print(self.gram)
    popupWindow.open()