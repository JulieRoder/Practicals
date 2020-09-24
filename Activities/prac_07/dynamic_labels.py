"""
CP1404 Practical
Dynamic Kivy Labels program
Student name: Julie-Anne Roder
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App for dynamic labels."""

    def __init__(self, **kwargs):
        """Main App construct."""
        super().__init__(**kwargs)
        self.list_of_names = ['Jim', 'Bob', 'Joe', 'Simon', 'Jane', 'John', 'Kim', 'Kate', 'Bebe', 'Chris', 'Charlie']

    def build(self):
        """Build Kivy GUI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from names in list_of_names."""
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.labels_listing.add_widget(temp_label)


DynamicLabelsApp().run()
