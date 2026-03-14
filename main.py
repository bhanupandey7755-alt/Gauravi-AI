from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from jnius import autoclass

# बैकग्राउंड पूरी तरह काला
Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        self.logo = Image(source='logo.png', size_hint=(1, 0.6))
        
        self.display_text = "G means Papa's dear daughter Gauravi"
        
        self.msg = Label(
            text=f"[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True,
            font_name="hindi.ttf", 
            font_size='22sp', 
            color=(1, 0.84, 0, 1),
            halign='center'
        )
        
        layout.add_widget(self.logo)
        layout.add_widget(self.msg)
        self.add_widget(layout)
        
        # आवाज़ शुरू करने और स्क्रीन बदलने का समय
        Clock.schedule_once(self.speak_welcome, 1)
        Clock.schedule_once(self.go_to_home, 5)

    def speak_welcome(self, dt):
        try:
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Locale = autoclass('java.util.Locale')
            
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            Clock.schedule_once(lambda dt: self.tts.setLanguage(Locale.ENGLISH), 1)
            Clock.schedule_once(lambda dt: self.tts.speak(self.display_text, TextToSpeech.QUEUE_FLUSH, None), 2)
        except:
            pass

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30)
        
        self.status_label = Label(
            text="Gauravi AI is Listening...", 
            font_name="hindi.ttf",
            font_size='28sp', 
            color=(1, 0.84, 0, 1),
            bold=True
        )
        
        self.layout.add_widget(self.status_label)
        self.add_widget(self.layout)

    def on_enter(self):
        # होम स्क्रीन पर आते ही माइक्रोफोन सक्रिय करें
        Clock.schedule_once(self.start_listening, 1)

    def start_listening(self, dt):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            
            PythonActivity.mActivity.startActivityForResult(intent, 1)
        except:
            self.status_label.text = "Microphone Error"

class GauraviAI(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == "__main__":
    GauraviAI().run()
