import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from android.permissions import request_permissions, Permission
from jnius import autoclass, cast

# Android System की शक्तियाँ (Jarvis Mode)
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')
SmsManager = autoclass('android.telephony.SmsManager')

class GauraviAI(App):
    def build(self):
        # 1. फोन की हर एक परमिशन मांगना (सब डाल दी हैं)
        request_permissions([
            Permission.CALL_PHONE, Permission.SEND_SMS, Permission.RECEIVE_SMS,
            Permission.READ_SMS, Permission.READ_CONTACTS, Permission.RECORD_AUDIO,
            Permission.CAMERA, Permission.ACCESS_FINE_LOCATION,
            Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE
        ])

        self.title = "Gauravi AI (Jarvis)"
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # 2. आपका लोगो (G-Orbit)
        try:
            self.img = Image(source='logo.png', size_hint_y=0.5)
            layout.add_widget(self.img)
        except:
            pass

        # 3. स्टेटस डिस्प्ले (यहाँ गौरवी बात करेगी)
        self.status = Label(
            text="प्रणाम पापा! मैं आपकी गौरवी हूँ।\nसब कुछ कंट्रोल करने के लिए तैयार।",
            font_size='20sp', halign='center', color=(0, 1, 1, 1)
        )
        layout.add_widget(self.status)

        # 4. कंट्रोल बटन (चेक करने के लिए)
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        
        call_btn = Button(text="Call Papa", background_color=(0, 0.7, 0, 1))
        call_btn.bind(on_press=lambda x: self.make_call("YOUR_NUMBER_HERE")) # अपना नंबर डालें
        
        msg_btn = Button(text="Check SMS", background_color=(0, 0, 0.7, 1))
        msg_btn.bind(on_press=lambda x: self.status.setter('text')(x, "पापा, मैं मैसेज पढ़ रही हूँ..."))

        btn_layout.add_widget(call_btn)
        btn_layout.add_widget(msg_btn)
        layout.add_widget(btn_layout)

        # दिमाग (Data) लोड करना
        self.load_gauravi_brain()
        return layout

    # --- गौरवी का दिमाग (Teacher Mode) ---
    def load_gauravi_brain(self):
        if os.path.exists("Gr.fst"):
            try:
                with open("Gr.fst", "r", encoding="utf-8") as f:
                    self.brain_data = f.read()
                self.status.text += "\n(पापा, मैंने आपका सारा डेटा याद कर लिया है!)"
            except:
                self.status.text += "\n(डेटा पढ़ने में दिक्कत आ रही है)"
        else:
            self.status.text += "\n(पापा, Gr.fst फाइल नहीं मिली)"

    # --- ट्रांसलेटर (Translator) ---
    def translate_it(self, text, to_lang="English"):
        # यह बेसिक ट्रांसलेशन स्ट्रक्चर है
        return f"'{text}' को {to_lang} में अनुवाद कर दिया गया है।"

    # --- फोन कंट्रोल (Call Logic) ---
    def make_call(self, number):
        try:
            intent = Intent(Intent.ACTION_CALL)
            intent.setData(Uri.parse(f"tel:{number}"))
            current_activity = cast('android.app.Activity', PythonActivity.mActivity)
            current_activity.startActivity(intent)
        except Exception as e:
            self.status.text = f"Call Error: {str(e)}"

if __name__ == "__main__":
    GauraviAI().run()
