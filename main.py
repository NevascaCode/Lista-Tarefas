from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDIconButton
Window.size = (360, 540)

class Remover(MDIconButton):
    def __init__(self, tarefa, **kwargs):
        super().__init__(**kwargs)
        self.tarefa = tarefa

class NovaTarefa(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Tarefa(OneLineListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.botao_remover = Remover(self)
        self.efeito_ativo = MDFloatLayout(md_bg_color=[0,0,0,.25], pos_hint={"center_y":.5})
    def verificar_check(self, tarefa):
        if not self.ids.check.active:
            self.remove_widget(self.botao_remover)
            self.remove_widget(self.efeito_ativo)
        else:
            self.add_widget(self.botao_remover)
            self.add_widget(self.efeito_ativo)

class Tela(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ListaTarefas(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click = True
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "200"
        print(self.theme_cls.primary_color)
        return Builder.load_file("lista_win.kv")

    def salvar_lista(self):
        ...

    def adicionar_tarefa(self):
        if self.click:
            self.root.add_widget(NovaTarefa())

    def criar_tarefa(self, text):
        self.root.ids.lista_tarefas.add_widget(Tarefa(text=text))

ListaTarefas().run()
