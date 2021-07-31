from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.button import MDIconButton
import json
import datetime
Window.size = (360, 540)

class Remover(MDIconButton):
    def __init__(self, tarefa, **kwargs):
        super().__init__(**kwargs)
        self.tarefa = tarefa

    def remover_item_do_json(self, texto_item, secondary_text, check_ativado):
        with open("lista.json", "r") as arquivo:
            lista = json.load(arquivo)

        with open("lista.json", "w") as arquivo:
            l = lista["items"].index({texto_item: check_ativado, "data":secondary_text})
            lista["items"].pop(l)
            json.dump(lista, arquivo, indent=4)


class NovaTarefa(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Tarefa(TwoLineListItem):
    def __init__(self, active_ini=False, **kwargs):
        super().__init__(**kwargs)
        self.active_ini = active_ini
        self.botao_remover = Remover(self)
        self.efeito_ativo = MDFloatLayout(md_bg_color=[0,0,0,.1], pos_hint={"center_y":.5})
        if active_ini:
            self.ids.check.active = active_ini
    def verificar_check(self, tarefa):
        if self.ids.check.active:
            self.add_widget(self.botao_remover)
            self.add_widget(self.efeito_ativo)
        else:
            self.remove_widget(self.botao_remover)
            self.remove_widget(self.efeito_ativo)
        if self.active_ini:
            self.active_ini = False
        else:
            self.atualizar_item(self.text, not self.ids.check.active)

    def atualizar_item(self, texto_item, check_ativado):
        with open("lista.json", "r") as arquivo:
            lista = json.load(arquivo)

        with open("lista.json", "w") as arquivo:
            l = lista["items"].index({texto_item: check_ativado, "data":self.secondary_text})
            lista["items"][l] = {texto_item: not check_ativado, "data":self.secondary_text}
            json.dump(lista, arquivo, indent=4)

    def atualizar_item(self, texto_item, check_ativado):
        with open("lista.json", "r") as arquivo:
            lista = json.load(arquivo)

        with open("lista.json", "w") as arquivo:
            l = lista["items"].index({texto_item: check_ativado, "data":self.secondary_text})
            lista["items"][l] = {texto_item: not check_ativado, "data":self.secondary_text}
            json.dump(lista, arquivo, indent=4)


class Tela(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ListaTarefas(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click = True

    def on_start(self):
        print("aaa")
        with open("lista.json", "r") as arquivo:
            lista = json.load(arquivo)
            for item in lista["items"]:
                for chave in item.keys():
                    self.root.ids.lista_tarefas.add_widget(Tarefa(text=chave, secondary_text=item["data"], active_ini=item[chave]))
                    break


    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        return Builder.load_file("lista_win.kv")

    def adicionar_tarefa(self):
        if self.click:
            self.root.add_widget(NovaTarefa())

    def salvar_item_json(self, texto_item, secondary_text, check_ativado=False):
        with open("lista.json", "r") as arquivo:
            lista = json.load(arquivo)

        with open("lista.json", "w") as arquivo:
            lista["items"].append({texto_item: check_ativado, "data":secondary_text})
            json.dump(lista, arquivo, indent=4)


    def criar_tarefa(self, text):
        self.root.ids.lista_tarefas.add_widget(Tarefa(text=text, secondary_text=f"{datetime.date.today()}"))
        self.salvar_item_json(text, f"{datetime.date.today()}")

ListaTarefas().run()
