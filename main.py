from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput

class paginas(BoxLayout):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = [1,1,1,1]
        Window.size =  400,600
        self.spacing = 10
        self.padding = 10
        self.login()

    def login(self):
        Window.size = 400,600
        pag = BoxLayout(orientation='vertical', padding=[120,120], spacing=11)
        im = Image(source="icon_user.png", size_hint=(1,3))
        texto = Label(text='LOGIN', font_size=30, font_name=('Arial'), color=get_color_from_hex('#0D214F'), bold=True)
        texto1 = Label(text='Usuário:', font_size=20, color=get_color_from_hex('#0D214F'))
        texto2 = Label(text='Senha:',font_size=20, color=get_color_from_hex('#0D214F'))
        email = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        senha = TextInput(text='', background_color=get_color_from_hex('#FFF7FC'))
        botao_login = Button(text='Login',background_color=get_color_from_hex('#0D214F'))
        botao_cadastro = Button(text='Fazer cadastro', background_color=get_color_from_hex('#0D214F'))
        botao_cadastro.bind(on_press=self.botao_cadastro)

        pag.add_widget(im)
        pag.add_widget(texto)
        pag.add_widget(texto1)
        pag.add_widget(email)
        pag.add_widget(texto2)
        pag.add_widget(senha)
        pag.add_widget(botao_login)
        pag.add_widget(botao_cadastro)
        self.add_widget(pag)

    def botao_cadastro(self, instance):
        self.clear_widgets()
        self.add_widget(self.cadastro())

    def cadastro(self):
        Window.size = 400,500
        pag = BoxLayout(orientation='vertical', padding=[120,120], spacing=11)
        texto = Label(text='CADASTRO',font_size=30, font_name=('Arial'), bold=True, color=get_color_from_hex('#0D214F'))
        texto1 = Label(text='E-mail:', font_size=20, color=get_color_from_hex('#0D214F'))
        texto2 = Label(text='Senha:', font_size=20, color=get_color_from_hex('#0D214F'))
        email = TextInput(text='')
        senha = TextInput(text='')
        botao = Button(text='Cadastrar', background_color=get_color_from_hex('#0D214F'))
        voltar = Button(text='Voltar', background_color=get_color_from_hex('#0D214F'))
        voltar.bind(on_press=self.voltar_pag)

        pag.add_widget(texto)
        pag.add_widget(texto1)
        pag.add_widget(email)
        pag.add_widget(texto2)
        pag.add_widget(senha)
        pag.add_widget(botao)
        pag.add_widget(voltar)

        return pag
    
    def voltar_pag(self, instance):
        self.clear_widgets()
        self.login()


class Meuapp(App):
    def build(self):
        home = ScreenManager()
        screen_paginas = Screen(name='Paginas')
        screen_paginas.add_widget(paginas())
        home.add_widget(screen_paginas)
        return home
        
    
if __name__ == "__main__":
    Meuapp().run()
