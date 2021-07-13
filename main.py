from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 640)

kv ='''
<MDBoxLayout>:

'''

class ListaTarefas(MDApp):
    def build(self):
        return Builder.load_file("lista_window.kv")

ListaTarefas().run()
