# Taylor Paielli, Timothy Sullivan, 12:00 GUI Project
import kivy
import json
kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
import time
import order

# You can create and load your kv code in the Python file
Builder.load_file('SunFresh.kv')


# Create a class for all screens in which you can include
# helpful methods specific to that screen
class Login(Screen):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.store = JsonStore('../../Downloads/Kivy_Practice/Login.json')

    def login(self):
        username  = self.ids.name.text
        self.store.put(username, Password=self.ids.password.text)

    def check(self):
        if self.store.exists(self.ids.name.text):
            with open('../../Downloads/Kivy_Practice/Login.json') as fp:
                dict = json.load(fp)
            self.ids.display.text = dict[self.ids.password.text['Password']]
        else:
            self.ids.name.text = 'does not exist'


class Home(Screen):
    pass


class Maps(Screen):
    pass


class Order(Screen):
    pass


class Qdoba(Screen):

    def order_no4(self):
        order.Orders.toJSON("Supreme Nachos","4", str(time.ctime()))

    def order_no5(self):
        order.Orders.toJSON("Tacos","5", str(time.ctime()))

    def order_no6(self):
        order.Orders.toJSON("Burrito","6", str(time.ctime()))


class Starbucks(Screen):

    def order_no7(self):
        order.Orders.toJSON("Caramel Frap","7", str(time.ctime()))

    def order_no8(self):
        order.Orders.toJSON("Bacon Gouda","8", str(time.ctime()))

    def order_no9(self):
        order.Orders.toJSON("Chai Latte","9", str(time.ctime()))

class Ein(Screen):

    def order_no10(self):
        order.Orders.toJSON("Breakfast Sandwhich","10", str(time.ctime()))

    def order_no11(self):
        order.Orders.toJSON("Plain Bagel","11", str(time.ctime()))

    def order_no12(self):
        order.Orders.toJSON("Smoothie","12", str(time.ctime()))

class Jamba(Screen):

    def order_no1(self):
        order.Orders.toJSON("Peach Perfection","1", str(time.ctime()))
        
    def order_no2(self):
        order.Orders.toJSON("Mango Madness","2", str(time.ctime()))

    def order_no3(self):
        order.Orders.toJSON("Berry Blast","3", str(time.ctime()))

# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(Login(name="login"))
screen_manager.add_widget(Home(name="home"))
screen_manager.add_widget(Maps(name="maps"))
screen_manager.add_widget(Order(name="order"))
screen_manager.add_widget(Qdoba(name="qdoba"))
screen_manager.add_widget(Starbucks(name="starbucks"))
screen_manager.add_widget(Ein(name="ein"))
screen_manager.add_widget(Jamba(name="jamba"))


class KivyApp(MDApp):

    def build(self):
        mapview = MapView()
        Window.set_title("Sunny's Kitchen")
        self.icon = 'logo.png'
        return screen_manager
        return mapview


sample_app = KivyApp()
sample_app.run()
