import json #to read jason file 
from difflib import get_close_matches 
from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager ,Screen 

Builder.load_file('design.kv')
data=json.load(open("word.json"))
class FirstScreen(Screen):

    def search(self,word):
    
        word=word.strip()
        if word == "":
            self.ids.result1.text="Enter value"
            self.ids.show.text=""    
        elif word.lower() in data:
            self.ids.show.text="Word - %s"%word
            self.ids.result1.text=(data[word.lower()])
            
        elif len(get_close_matches(word.lower(), data.keys() ))>0:
            self.ids.show.text="You Searched \"%s\". Do you mean \"%s\" "%(word,get_close_matches(word.lower(), data.keys() )[0].capitalize())
            self.ids.result1.text= data[get_close_matches(word.lower(), data.keys() )[0]]
        else:
            self.ids.result1.text="Enter correct word"
            self.ids.show.text=""
          
        self.ids.word.text=""
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
if __name__=="__main__":
    MainApp().run()