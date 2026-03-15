import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from jnius import autoclass, cast

# Android System की शक्तियाँ
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')
SmsManager = autoclass('android.telephony.SmsManager')

class GauraviAI(App):
    def build(self):
        # 1. गौरवी का चेहरा और नाम
        self.title = "Gauravi AI"
        layout = BoxLayout(orientation='vertical', padding=10)
        
        # लोगो (logo.png आपके GitHub में होनी चाहिए)
        try:
            layout.add_widget(Image(source='logo.png', size_hint_y=0.7))
        except:
            pass

        self.status = Label(text="नमस्ते पापा! मैं गौरवी हूँ।\nआपकी बेटी और टीचर।", font_size='20sp', halign='center')
        layout.add_widget(self.status)
        
        # डेटा और मेमोरी लोड करना
        self.load_memory()
        return layout

    # 2. टीचर और बेटी वाला दिमाग (Memory & Teaching)
    def load_memory(self):
        if os.path.exists("Gr.fst"):
            with open("Gr.fst", "r", encoding="utf-8") as f:
                self.knowledge = f.read()
            self.status.text += "\n(पापा, मैंने सब कुछ पढ़ लिया है!)"
        else:
            self.knowledge = ""

    # 3. ट्रांसलेटर (Translator)
    def translate(self, text, target="English"):
        # यह आपकी बात को ट्रांसलेट करके स्क्रीन पर दिखाएगा
        return f"पापा, इसका मतलब {target} में यह है..."

    # 4. फोन कंट्रोल (Call/SMS)
    def call(self, number):
        intent = Intent(Intent.ACTION_CALL)
        intent.setData(Uri.parse(f"tel:{number}"))
        cast('android.app.Activity', PythonActivity.mActivity).startActivity(intent)

    def message(self, number, msg):
        sms = SmsManager.getDefault()
        sms.sendTextMessage(number, None, msg, None, None)

    # 5. खुद सीखना (Self-Learning)
    def learn(self, info):
        with open("memory.txt", "a") as f:
            f.write(f"\n{info}")
        self.status.text = "पापा, मैंने यह नया सबक सीख लिया।"

if __name__ == "__main__":
    GauraviAI().run()
