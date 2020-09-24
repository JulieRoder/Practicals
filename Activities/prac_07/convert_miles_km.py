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

    def handle_convert(self):
        """Calculate the conversion from miles to kilometres."""
        miles = self.valid_number()
        kilometres = miles * self.CONVERSION_RATE
        self.root.ids.output_label.text = str(kilometres)

    def handle_increment(self, increment):
        """Increase input_number by given increment."""
        number = self.valid_number()
        new_number = number + increment
        self.root.ids.input_number.text = str(new_number)

    def valid_number(self):
        """Returns a valid number or 0.0 ."""
        try:
            number = float(self.root.ids.input_number.text)
            if number < 0:
                return 0.0
            return number
        except ValueError:
            return 0.0


MilesToKilometreConverterApp().run()
