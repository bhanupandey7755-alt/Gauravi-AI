from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

# स्क्रीन का बैकग्राउंड काला करने के लिए
Window.clearcolor = (0, 0, 0, 1)

class GauraviAI(App):
    def build(self):
        self.title = "Gauravi AI"
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # 1. धड़कता हुआ गोल्ड 'G' लोगो
        self.logo = Label(
            text="G",
            font_size='150sp',
            font_name='Roboto',  # Android का स्टैंडर्ड फॉन्ट
            color=(1, 0.84, 0, 1), # गोल्ड कलर (RGB: 255, 215, 0)
            bold=True
        )
        
        # 2. ऐप का नाम (गोल्डन अक्षरों में)
        self.name_label = Label(
            text="GAURAVI AI",
            font_size='30sp',
            color=(1, 0.84, 0, 1),
            bold=True,
            size_hint=(1, 0.2)
        )

        # 3. स्टेटस मैसेज
        self.status = Label(
            text="नमस्ते पापा!",
            font_size='18sp',
            color=(0.8, 0.8, 0.8, 1) # हल्का सफेद/ग्रे
        )

        layout.add_widget(self.logo)
        layout.add_widget(self.name_label)
        layout.add_widget(self.status)

        # लोगो को धड़काने (Pulse) के लिए टाइमर
        Clock.schedule_interval(self.pulse_animation, 0.05)
        
        return layout

    def pulse_animation(self, dt):
        # यह धीरे-धीरे चमक बढ़ाएगा और घटाएगा
        current_opacity = self.logo.color[3]
        if not hasattr(self, 'direction'): self.direction = -0.01
        
        new_opacity = current_opacity + self.direction
        
        if new_opacity <= 0.4: self.direction = 0.01
        if new_opacity >= 1.0: self.direction = -0.01
        
        self.logo.color = (1, 0.84, 0, new_opacity)

if __name__ == "__main__":
    GauraviAI().run()
