from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        if os.path.exists('logo.png'):
            layout.add_widget(Image(source='logo.png', size_hint=(1, 0.6)))
        
        self.msg = Label(
            text="[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True, font_size='22sp', color=(1, 0.84, 0, 1), halign='center'
        )
        layout.add_widget(self.msg)
        self.add_widget(layout)
        Clock.schedule_once(self.ask_permissions, 1)

    def ask_permissions(self, dt):
        request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
        Clock.schedule_once(self.go_to_home, 4)

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30)
        self.status_label = Label(
            text="Gauravi AI is Ready", 
            font_size='28sp', color=(1, 0.84, 0, 1), bold=True
        )
        self.layout.add_widget(self.status_label)
        self.add_widget(self.layout)

    def on_enter(self):
        # होम स्क्रीन पर आते ही पहले बोलेगी, फिर सुनेगी
        Clock.schedule_once(self.start_voice, 1)

    def start_voice(self, dt):
        try:
            # 1. बोलना (Speaking)
            TTS = autoclass('android.speech.tts.TextToSpeech')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.tts = TTS(PythonActivity.mActivity, None)
            txt = "G means Papa's dear daughter Gauravi. I am ready, Papa."
            Clock.schedule_once(lambda d: self.tts.speak(txt, TTS.QUEUE_FLUSH, None), 1)
            
            # 2. सुनना (Listening) - बोलने के 4 सेकंड बाद शुरू होगा
            Clock.schedule_once(self.listen_now, 5)
        except:
            self.status_label.text = "Voice Error"

    def listen_now(self, dt):
        try:
            self.status_label.text = "Listening..."
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            PythonActivity.mActivity.startActivityForResult(intent, 1)
        except:
            self.status_label.text = "Mic Error"

class GauraviAI(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == "__main__":
    GauraviAI().run()
