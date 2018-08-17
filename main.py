#coding: utf-8
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import status

class MyRoot(BoxLayout):

    def show_status(self, instance):

        hosts = status.get()
        texto = ''
        for host in hosts:

            nome = host['hostname']
            estado = host['state']
            ram = str(host['ram'])
            vms = str(host['vms'])

            msg = nome +    '\nEstado: ' + estado + \
                            '\nRam: ' + ram + \
                            '\nVMs: ' + vms + '\n\n'

            texto = texto + msg

        self.ids.status.text = texto

class MainApp(App):
	pass

if __name__ == '__main__':
    MainApp().run()