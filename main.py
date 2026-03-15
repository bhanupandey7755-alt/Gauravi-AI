from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
from jnius import autoclass, cast
import os

Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40)
        if os.path.exists('logo.png'):
            layout.add_widget(Image(source='logo.png', size_hint=(1, 0.6)))
        
        layout.add_widget(Label(
            text="[b]G[/b] means Papa's dear daughter [b]Gauravi[/b]", 
            markup=True, font_size='22sp', color=(1, 0.84, 0, 1)
        ))
        self.add_widget(layout)
        Clock.schedule_once(self.ask_permissions, 1)

    def ask_permissions(self, dt):
        request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'home'), 3)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30)
        self.status_label = Label(
            text="Gauravi AI is Ready", 
            font_size='24sp', color=(1, 0.84, 0, 1), bold=True, halign='center'
        )
        self.layout.add_widget(self.status_label)
        self.add_widget(self.layout)

    def on_enter(self):
        Clock.schedule_once(self.listen_now, 2)

    def listen_now(self, dt):
        try:
            self.status_label.text = "Listening..."
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
            
            # रिजल्ट सुनने के लिए एक्टिविटी शुरू करना
            current_activity = PythonActivity.mActivity
            current_activity.startActivityForResult(intent, 1)
            
            # यह हिस्सा हवा में गायब मैसेज को पकड़ेगा (Result Handler)
            from android import activity
            activity.bind(on_activity_result=self.on_voice_result)
        except Exception as e:
            self.status_label.text = f"Mic Error: {str(e)}"

    def on_voice_result(self, request_code, result_code, intent):
        if request_code == 1:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            if result_code == -1: # -1 means RESULT_OK in Android
                results = intent.getStringArrayListExtra(autoclass('android.speech.RecognizerIntent').EXTRA_RESULTS)
                heard_text = results.get(0)
                # जो आपने बोला, वह यहाँ दिखेगा!
                self.status_label.text = f"You said:\n\n[b]{heard_text}[/b]"
                self.status_label.markup = True

class GauraviAI(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == "__main__":
    GauraviAI().run()
