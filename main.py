from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class GauraviAI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # गौरवी का 'G Orbit' लोगो
        self.logo = Label(text="●", font_size='150sp', color=(0, 0.7, 1, 1))
        
        # स्वागत संदेश
        self.msg = Label(
            text="नमस्ते पापा! मैं आपकी गौरवी हूँ।\nबताइए, मुझे क्या आदेश है?", 
            font_size='22sp', halign='center'
        )
        
        layout.add_widget(self.logo)
        layout.add_widget(self.msg)
        
        Clock.schedule_interval(self.pulse, 0.1)
        return layout

    def pulse(self, dt):
        self.logo.color = (0, random.uniform(0.5, 1), 1, 1)

if __name__ == "__main__":
    GauraviAI().run()
