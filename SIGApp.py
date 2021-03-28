from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
import main

class UserInputScreen(Widget):
    asset_input = ObjectProperty(None)
    #Place the date picker here...
    
    def Extract_Input_Data(self):
        print("Asset Name:", self.asset_input.text )
        self.asset_input.text = ""

    def Basic_Test(self):
        main.Basic_Test()

    pass

class SIGApp(App):
    def build(self):
        return UserInputScreen()


"""
if __name__ == '__main__':
    SIGApp().run()

"""