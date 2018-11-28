# -*- coding: utf-8 -*- #

import wx
import Datacom
import Editor

# Organizar para ordenar tabela

class pessoa(wx.Panel):


    def __init__(self, parent):

        super(pessoa, self).__init__(parent=parent)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.p_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(-1, 420))
        self.parent = parent
        screens = ['Pessoas', 'Veículos']
        self.choicebox = wx.Choice(self, choices=screens, size=(494, 25))
        self.cursor = Datacom.start_cursor(parent.mydb)
        self.srchfld = wx.TextCtrl(self, size=(352, 23))
        self.command = ''
        self.init_Pessoa()


    def init_Pessoa(self):

        srchtxt = wx.StaticText(self, label='Pesquisa: ', size=(56, 18))
        srchbt = wx.Button(self, label='Buscar', size=(75, 25))
        self.hbox.Add(srchtxt, 0, wx.ALIGN_CENTER)
        self.hbox.Add(self.srchfld, 0, wx.ALIGN_CENTER)
        self.hbox.AddSpacer(10)
        self.hbox.Add(srchbt, 0, wx.ALIGN_CENTER)

        self.p_list.InsertColumn(0, 'ID', width=60)
        self.p_list.InsertColumn(1, 'Nome', width=200)
        self.p_list.InsertColumn(2, 'Est. Civil', width=110)
        self.p_list.InsertColumn(3, 'Fone', width=120)

        addpbtn = wx.Button(self, label='Adicionar pessoa', size=(130, 25))
        allbtn = wx.Button(self, label='Mostrar todos', size=(130, 25))
        clrbtn = wx.Button(self, label='Limpar tabela', size=(130, 25))

        self.hbox2.AddSpacer(10)
        self.hbox2.Add(addpbtn, 0, wx.ALIGN_CENTER)
        self.hbox2.AddSpacer(10)
        self.hbox2.Add(allbtn, 0, wx.ALIGN_CENTER)
        self.hbox2.AddSpacer(10)
        self.hbox2.Add(clrbtn, 0, wx.ALIGN_CENTER)

        self.vbox.AddSpacer(10)
        self.vbox.Add(self.choicebox, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.hbox, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.p_list, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.hbox2, 0, wx.ALIGN_CENTER)

        self.SetSizer(self.vbox)

        self.choicebox.Bind(wx.EVT_CHOICE, self.onSelectScreen)

        allbtn.Bind(wx.EVT_BUTTON, self.onPressAllButton)

        clrbtn.Bind(wx.EVT_BUTTON, self.onPressClrButton)

        srchbt.Bind(wx.EVT_BUTTON, self.onPressSrchButton)

        addpbtn.Bind(wx.EVT_BUTTON, self.onPressAddButton)

        self.p_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onSelectItem)


    def onSelectScreen(self, event):

        selected = event.GetSelection()
        if selected == 1:
            self.parent.panel3.choicebox.SetSelection(1)
            self.parent.panel3.Show()
            self.Hide()
        self.parent.Layout()


    def onPressAllButton(self, event):

        self.p_list.DeleteAllItems()

        self.command = 'SELECT * FROM vw_pessoas'

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, self.command)

        index = 0
        for info in self.cursor:
            self.p_list.InsertItem(index, str(info[0]))
            self.p_list.SetItem(index, 1, info[1])
            self.p_list.SetItem(index, 2, info[2])
            self.p_list.SetItem(index, 3, str(info[3]))
            index += 1


    def onPressClrButton(self, event):
        self.p_list.DeleteAllItems()


    def onPressSrchButton(self, event):

        self.p_list.DeleteAllItems()

        self.command = 'SELECT * FROM vw_pessoas ' \
                       'WHERE Nome LIKE \'%{}%\''.format(self.srchfld.GetLineText(0))

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, self.command)

        index = 0
        for info in self.cursor:
            self.p_list.InsertItem(index, str(info[0]))
            self.p_list.SetItem(index, 1, info[1])
            self.p_list.SetItem(index, 2, info[2])
            self.p_list.SetItem(index, 3, str(info[3]))
            index += 1


    def onSelectItem(self, event):

        Editor.editor_pessoa(self.parent, self.p_list.GetItemText(self.p_list.GetFocusedItem()), 0).Show()


    def onPressAddButton(self, event):

        Editor.editor_pessoa(self.parent, 0, 1).Show()
