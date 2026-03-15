from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
import os

# बैकग्राउंड काला
Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        # लोगो चेक - अगर लोगो फाइल है तो दिखाओ, वरना टेक्स्ट दिखाओ
        if os.path.exists('logo.png'):
            layout.add_widget(Image(source='logo.png', size_hint=(1, 0.6)))
        else:
            layout.add_widget(Label(text="[ G ]", font_size='80sp', color=(1, 0.84, 0, 1)))
        
        # आपका संदेश
        self.msg = Label(
            text="[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True,
            font_size='22sp', 
            color=(1, 0.84, 0, 1),
            halign='center'
        )
        layout.add_widget(self.msg)
        self.add_widget(layout)
        
        # ऐप शुरू होते ही परमिशन मांगना (Android 11+ के लिए ज़रूरी)
        Clock.schedule_once(self.ask_permissions, 1)

    def ask_permissions(self, dt):
        # माइक्रोफोन और इंटरनेट की अनुमति मांगना
        request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
        # परमिशन के बाद 4 सेकंड रुककर होम पर जाएंगे
        Clock.schedule_once(self.go_to_home, 4)

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(
            text="Gauravi AI is Ready", 
            font_size='28sp', 
            color=(1, 0.84, 0, 1),
            bold=True
        ))
        self.add_widget(layout)

class GauraviAI(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == "__main__":
    GauraviAI().run()
