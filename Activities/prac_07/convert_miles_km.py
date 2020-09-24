"""
CP1404 Practicals
Miles to Kilometres Converter program
Student name: Julie-Anne Roder
"""
from kivy.app import App
from kivy.app import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometreConverterApp(App):
    """Kivy app to convert miles into kilometres."""
    CONVERSION_RATE = 1.60934
    message = StringProperty()

    def build(self):
        """Build the App from 'convert_miles_km.kv' file."""
        self.title = 'Miles to Kilometre Converter'
        Window.size = (300, 300)
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        kilometres = miles * self.CONVERSION_RATE
        self.message = self.root.ids.output_label.text = kilometres


MilesToKilometreConverterApp().run()
