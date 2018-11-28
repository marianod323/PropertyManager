# -*- coding: utf-8 -*- #

import wx


class interface(wx.Frame):

    def __init__(self, wid, hei, title, *args, **kw):
        super(interface, self).__init__(None, title=title,
                                        size=(wid, hei), *args, **kw)
        self.init_Table()

    def init_Table(self):

        panel = wx.Panel()

        screens = ['Pessoas', 'Veículos']
        choicebox = wx.ComboBox(panel, choices=screens, size=(494, 25))

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        srchtxt = wx.StaticText(panel, label='Pesquisa: ', size=(56, 18))
        srchfld = wx.TextCtrl(panel, size=(352, 23))
        srchbt = wx.Button(panel, label='Buscar', size=(75, 25))
        hbox.Add(srchtxt, 0, wx.ALIGN_CENTER)
        hbox.Add(srchfld, 0, wx.ALIGN_CENTER)
        hbox.AddSpacer(10)
        hbox.Add(srchbt, 0, wx.ALIGN_CENTER)

        vbox = wx.BoxSizer(wx.VERTICAL)

        p_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(-1, 420))
        p_list.InsertColumn(0, 'ID', width=60)
        p_list.InsertColumn(1, 'Nome', width=200)
        p_list.InsertColumn(2, 'Est. Civil', width=110)
        p_list.InsertColumn(3, 'Fone', width=120)

        addpbtn = wx.Button(self, label='Adicionar pessoa', size=(496, 25))

        vbox.AddSpacer(10)
        vbox.Add(choicebox, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(10)
        vbox.Add(hbox, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(10)
        vbox.Add(p_list, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(10)
        vbox.Add(addpbtn, 0, wx.ALIGN_CENTER)

        self.SetSizer(vbox)
        self.Centre()


app = wx.App()

ex = interface(wid = 530, hei = 583, title = 'Proprietário')
ex.Show()
app.MainLoop()