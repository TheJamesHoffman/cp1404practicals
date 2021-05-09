from kivy.app import App
from kivy.lang import Builder

M_TO_KM = 1.60939

class MilesToKilometresApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        value = self.check_miles() + change
        self.root.ids.convert_miles.text = str(value)
        self.handle_calculate()

    def handle_calculate(self):
        value = self.check_miles()
        result = value * M_TO_KM
        self.root.ids.output_label.text = str(result)

    def check_miles(self):
        try:
            value = float(self.root.ids.convert_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometresApp().run()
