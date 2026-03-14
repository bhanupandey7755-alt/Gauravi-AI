from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import threading

# Android की आवाज़ के लिए (pyttsx3 की जगह Android native इस्तेमाल करेंगे)
from jnius import autoclass

Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        self.logo = Image(source='logo.png', size_hint=(1, 0.6))
        
        self.msg = Label(
            text="[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True,
            font_name="hindi.ttf", 
            font_size='22sp', 
            color=(1, 0.84, 0, 1),
            halign='center'
        )
        
        layout.add_widget(self.logo)
        layout.add_widget(self.msg)
        self.add_widget(layout)
        
        # ऐप खुलते ही बोलने के लिए
        Clock.schedule_once(self.speak_welcome, 1)
        Clock.schedule_once(self.go_to_home, 6)

    def speak_welcome(self, dt):
        # Android TextToSpeech का इस्तेमाल
        try:
            Locale = autoclass('java.util.Locale')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            Clock.schedule_once(lambda dt: self.tts.setLanguage(Locale.ENGLISH), 1)
            Clock.schedule_once(lambda dt: self.tts.speak("G means Papa's dear daughter Gauravi. Welcome home beta!", TextToSpeech.QUEUE_FLUSH, None), 2)
        except:
            print("TTS not available yet")

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30)
        layout.add_widget(Label(
            text="Gauravi AI is Listening...", 
            font_name="hindi.ttf",
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
