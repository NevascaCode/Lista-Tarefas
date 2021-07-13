from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineListItem
Window.size = (360, 540)

class NovaTarefa(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Tarefa(OneLineListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Tela(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ListaTarefas(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click = True
    def build(self):
        return Builder.load_file("lista_win.kv")

    def salvar_lista(self):
        ...

    def adicionar_tarefa(self):
        if self.click:
            self.root.add_widget(NovaTarefa())

    def criar_tarefa(self, text):
        self.root.ids.lista_tarefas.add_widget(Tarefa(text=f"     {text}"))

ListaTarefas().run()
