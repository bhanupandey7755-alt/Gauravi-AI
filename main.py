from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# बैकग्राउंड को पूरा काला रखने के लिए
Window.clearcolor = (0, 0, 0, 1)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # यह आपके अपलोड किए हुए लोगो को स्क्रीन पर दिखाएगा
        self.logo = Image(source='logo.png', size_hint=(1, 0.7))
        
        # गोल्डन अक्षरों में स्वागत संदेश
        self.msg = Label(
            text="नमस्ते पापा!", 
            font_size='26sp', 
            color=(1, 0.84, 0, 1), 
            bold=True
        )
        
        layout.add_widget(self.logo)
        layout.add_widget(self.msg)
        self.add_widget(layout)
        
        # 4 सेकंड बाद अपने आप होम स्क्रीन पर ले जाए
        Clock.schedule_once(self.go_to_home, 4)

    def go_to_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30)
        
        layout.add_widget(Label(
            text="गौरवी AI सक्रिय है", 
            font_size='30sp', 
            color=(1, 0.84, 0, 1), 
            bold=True
        ))
        
        layout.add_widget(Label(
            text="मैं आपकी क्या मदद कर सकती हूँ?", 
            font_size='18sp',
            color=(0.9, 0.9, 0.9, 1)
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
