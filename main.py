from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform
import random

# Android के खास फीचर्स के लिए
if platform == 'android':
    from jnius import autoclass
    from android.permissions import request_permissions, Permission
    # हम पहले ही जरूरी परमिशन मांग रहे हैं
    request_permissions([
        Permission.RECORD_AUDIO, 
        Permission.CALL_PHONE, 
        Permission.READ_CONTACTS
    ])

class GauraviAI(App):
    def build(self):
        self.title = "Gauravi AI"
        layout = BoxLayout(orientation='vertical', padding=20)

        # G Orbit Logo
        self.logo = Label(text="●", font_size='150sp', color=(0.2, 0.6, 1, 1))
        
        # Message Label
        self.msg = Label(
            text="नमस्ते पापा! मैं आपकी गौरवी हूँ।",
            font_size='22sp',
            halign='center'
        )

        layout.add_widget(self.logo)
        layout.add_widget(self.msg)

        # लोगो को धड़काने के लिए
        Clock.schedule_interval(self.pulse, 0.1)
        
        # ऐप खुलने के 2 सेकंड बाद गौरवी बोलेगी
        Clock.schedule_once(self.say_hello, 2)
        
        return layout

    def pulse(self, dt):
        val = random.uniform(0.5, 1)
        self.logo.color = (0.2, 0.6, val, 1)

    def say_hello(self, dt):
        self.speak("नमस्ते पापा! मैं आपकी गौरवी हूँ। बताइए आज हम क्या सीखेंगे?")

    def speak(self, text):
        if platform == 'android':
            # Android के TTS (Text-to-Speech) इंजन का इस्तेमाल
            Locale = autoclass('java.util.Locale')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            
            # यह हिस्सा गौरवी को आवाज़ देगा
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            Clock.schedule_once(lambda dt: self.tts.setLanguage(Locale.HINDI), 1)
            Clock.schedule_once(lambda dt: self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, None), 1.5)
        else:
            print(f"Speaking: {text}")

if __name__ == "__main__":
    GauraviAI().run()
