# -*- coding: utf-8 -*- #

import wx
import Datacom
import Editor

class veiculos(wx.Panel):


    def __init__(self, parent):

        super(veiculos, self).__init__(parent=parent)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.v_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT, size=(-1, 420))
        self.parent = parent
        screens = ['Pessoas', 'Veículos']
        self.choicebox = wx.Choice(self, choices=screens, size=(494, 25))
        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.srchfld = wx.TextCtrl(self, size=(290, 23))
        self.init_Veiculo()


    def init_Veiculo(self):

        srchtxt = wx.StaticText(self, label='Pesquisa por modelo: ', size=(118, 18))
        srchbt = wx.Button(self, label='Buscar', size=(75, 25))
        self.hbox.Add(srchtxt, 0, wx.ALIGN_CENTER)
        self.hbox.Add(self.srchfld, 0, wx.ALIGN_CENTER)
        self.hbox.AddSpacer(10)
        self.hbox.Add(srchbt, 0, wx.ALIGN_CENTER)

        self.v_list.InsertColumn(1, 'Chassi', width=180)
        self.v_list.InsertColumn(0, 'ID dono', width=60)
        self.v_list.InsertColumn(2, 'Modelo', width=190)
        self.v_list.InsertColumn(3, 'Ano', width=60)

        addvbtn = wx.Button(self, label='Adicionar veículo', size=(130, 25))
        allbtn = wx.Button(self, label='Mostrar todos', size=(130, 25))
        clrbtn = wx.Button(self, label='Limpar tabela', size=(130, 25))

        self.hbox2.AddSpacer(10)
        self.hbox2.Add(addvbtn, 0, wx.ALIGN_CENTER)
        self.hbox2.AddSpacer(10)
        self.hbox2.Add(allbtn, 0, wx.ALIGN_CENTER)
        self.hbox2.AddSpacer(10)
        self.hbox2.Add(clrbtn, 0, wx.ALIGN_CENTER)

        self.vbox.AddSpacer(10)
        self.vbox.Add(self.choicebox, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.hbox, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.v_list, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(10)
        self.vbox.Add(self.hbox2, 0, wx.ALIGN_CENTER)

        self.SetSizer(self.vbox)

        self.choicebox.Bind(wx.EVT_CHOICE, self.onSelectScreen)

        allbtn.Bind(wx.EVT_BUTTON, self.onPressAllButton)

        clrbtn.Bind(wx.EVT_BUTTON, self.onPressClrButton)

        srchbt.Bind(wx.EVT_BUTTON, self.onPressSrchButton)

        addvbtn.Bind(wx.EVT_BUTTON, self.onPressAddButton)

        self.v_list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onSelectItem)


    def onSelectScreen(self, event):

        selected = event.GetSelection()
        if selected == 0:
            self.parent.panel2.choicebox.SetSelection(0)
            self.parent.panel2.Show()
            self.Hide()
        self.parent.Layout()


    def onPressAllButton(self, event):

        self.v_list.DeleteAllItems()

        command = 'SELECT * FROM vw_veiculos'

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        index = 0
        for info in self.cursor:
            self.v_list.InsertItem(index, str(info[0]))
            self.v_list.SetItem(index, 1, str(info[1]))
            self.v_list.SetItem(index, 2, info[2])
            self.v_list.SetItem(index, 3, str(info[3]))
            index += 1


    def onPressClrButton(self, event):
        self.v_list.DeleteAllItems()


    def onPressSrchButton(self, event):

        self.v_list.DeleteAllItems()

        command = 'SELECT * FROM vw_veiculos ' \
                  'WHERE modelo LIKE \'%{}%\''.format(self.srchfld.GetLineText(0))

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        index = 0
        for info in self.cursor:
            self.v_list.InsertItem(index, str(info[0]))
            self.v_list.SetItem(index, 1, info[1])
            self.v_list.SetItem(index, 2, info[2])
            self.v_list.SetItem(index, 3, str(info[3]))
            index += 1

    def onSelectItem(self, event):

        Editor.editor_veiculo(self.parent, self.v_list.GetItemText(self.v_list.GetFocusedItem(), 1), 0).Show()


    def onPressAddButton(self, event):

        Editor.editor_veiculo(self.parent, 0, 1).Show()
