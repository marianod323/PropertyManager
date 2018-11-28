# -*- coding: utf-8 -*- #

import wx
import Pessoa
import Veiculos
import Datacom


class interface(wx.Frame):


    def __init__(self, wid, hei, title, *args, **kw):

        super(interface, self).__init__(None, title=title,
            size=(wid, hei), *args, **kw)
        self.panel = wx.Panel(self)
        screens = ['Pessoas', 'Veículos']
        self.choicebox = wx.Choice(self.panel, choices=screens, size=(494, 25))
        self.mydb = Datacom.start_database()
        self.panel2 = Pessoa.pessoa(self)
        self.panel3 = Veiculos.veiculos(self)
        self.init_Interface()


    def init_Interface(self):

        self.panel2.Hide()
        self.panel3.Hide()

        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.panel, 1, wx.EXPAND)
        self.Sizer.Add(self.panel2, 1, wx.EXPAND)
        self.Sizer.Add(self.panel3, 1, wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        txt = wx.StaticText(self.panel, label='Escolha uma tabela para iniciar.', size=(180, 18))


        vbox.AddSpacer(10)
        vbox.Add(self.choicebox, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(20)
        vbox.Add(txt, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(vbox)

        self.choicebox.Bind(wx.EVT_CHOICE, self.onSelectScreen)


        self.Centre()


    def onSelectScreen(self, event):

        selected = event.GetSelection()
        if selected == 0:
            self.panel2.choicebox.SetSelection(0)
            self.panel2.Show()
            self.panel.Hide()
        else:
            self.panel3.choicebox.SetSelection(1)
            self.panel3.Show()
            self.panel.Hide()
        self.Layout()