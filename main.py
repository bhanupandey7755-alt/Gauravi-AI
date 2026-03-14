from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import os

# Android की शक्तियों को जोड़ने के लिए
try:
    from jnius import autoclass
except:
    autoclass = None

Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        # लोगो चेक करें ताकि ऐप क्रैश न हो
        if os.path.exists('logo.png'):
            self.logo = Image(source='logo.png', size_hint=(1, 0.6))
        else:
            self.logo = Label(text="[ G ]", font_size='80sp', color=(1, 0.84, 0, 1))
        
        # फॉन्ट चेक करें
        f_name = "hindi.ttf" if os.path.exists("hindi.ttf") else None
        
        self.msg = Label(
            text="[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True,
            font_name=f_name, 
            font_size='22sp', 
            color=(1, 0.84, 0, 1),
            halign='center'
        )
        
        layout.add_widget(self.logo)
        layout.add_widget(self.msg)
        self.add_widget(layout)
        
        Clock.schedule_once(self.speak_welcome, 1)
        Clock.schedule_once(self.go_to_home, 5)

    def speak_welcome(self, dt):
        if autoclass:
            try:
                TTS = autoclass('android.speech.tts.TextToSpeech')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                self.tts = TTS(PythonActivity.mActivity, None)
                txt = "G means Papa's dear daughter Gauravi"
                Clock.schedule_once(lambda d: self.tts.speak(txt, TTS.QUEUE_FLUSH, None), 2)
            except:
                pass

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        f_name = "hindi.ttf" if os.path.exists("hindi.ttf") else None
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(
            text="Gauravi AI is Listening...", 
            font_name=f_name,
            font_size='28sp', 
            color=(1, 0.84, 0, 1)
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
