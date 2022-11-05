from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 324)
Config.set("graphics", "height", 491)

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.templates import RotateWidget
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDRaisedButton


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
    btn_visible = False
    duration = 0.2

    def do_anim_show_btn_meds(self, *args):
        anim = Animation(y=dp(56) + dp(60), t="out_circ", d=self.duration, )
        anim &= Animation(x=(self.center_x - self.ids.meds.width / 2) - dp(80), t="out_circ",
                          d=self.duration + 0.3, )
        anim.start(self.ids.meds)

    def do_anim_hide_btn_meds(self, *args):
        anim = Animation(x=self.center_x - self.ids.meds.width / 2, t="out_circ", d=self.duration + 0.3, )
        anim &= Animation(y=dp(56), t="out_circ", d=self.duration, )
        anim.start(self.ids.meds)

    def do_anim_show_btn_blood(self, *args):
        Animation(y=dp(56) + dp(120), t="out_circ", d=self.duration, ).start(self.ids.blood)

    def do_anim_hide_btn_blood(self, *args):
        Animation(y=dp(56), t="out_circ", d=self.duration, ).start(self.ids.blood)

    def do_anim_show_btn_food(self, *args):
        anim = Animation(y=dp(56) + dp(60), t="out_circ", d=self.duration, )
        anim &= Animation(x=(self.center_x - self.ids.food.width / 2) + dp(80), t="out_circ", d=self.duration + 0.3, )
        anim.start(self.ids.food)

    def do_anim_hide_btn_food(self, *args):
        anim = Animation(x=self.center_x - self.ids.food.width / 2, t="out_circ", d=self.duration + 0.3, )
        anim &= Animation(y=dp(56), t="out_circ", d=self.duration, )
        anim.start(self.ids.food)

    def anim_btn(self) -> None:
        Animation(rotate_value_angle=45 if not self.btn_visible else 0, d=0.1).start(self.ids.btn_root)

        if not self.btn_visible:
            Clock.schedule_once(self.do_anim_show_btn_meds)
            Clock.schedule_once(self.do_anim_show_btn_food, 0.1)
            Clock.schedule_once(self.do_anim_show_btn_blood, 0.2)
        else:
            Clock.schedule_once(self.do_anim_hide_btn_meds)
            Clock.schedule_once(self.do_anim_hide_btn_food, 0.1)
            Clock.schedule_once(self.do_anim_hide_btn_blood, 0.2)

        self.btn_visible = not self.btn_visible

    def on_size(self, *args):
        if self.btn_visible:
            self.anim_btn()


class EightWindow(MDScreen):
    pass


class NineWindow(MDScreen):
    pass


class TenWindow(MDScreen):
    def one(self):
        # self.lau = GridLayout(cols = 1, spacing = 10, size_hint_y = None)
        # self.lau.bind(minimum_height = self.lau.setter('height'))
        self.add_widget(GridLayout(cols=1, spacing=10, size_hint_y=None))

        for i in range(10):
            self.btn = MDRaisedButton(text=str(i), size_hint_y=None, height=40)
            self.add_widget(self.btn)

    # ro = ScrollView(size_hint = (1,None), size=(Window.width, Window.height ) )
    # ro.add_widget(lau)


class ElevenWindow(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class RootButton(MDFloatingActionButton, RotateWidget):
    pass
