# -*- coding: utf-8 -*- #

import wx
import Datacom

class avisos(wx.Dialog):


    def __init__(self, parent, erro):
        super(avisos, self).__init__(parent=parent, size=(280, 160), title='Erro')
        self.panel = wx.Panel(self)
        erro = wx.StaticText(self.panel, label=erro, size=( -1, 60))
        self.ok_button = wx.Button(self.panel, size=(70, 25), label='Ok')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(28)
        vbox.Add(erro, 0, wx.ALIGN_CENTER)
        vbox.Add(self.ok_button, 0, wx.ALIGN_CENTER)

        self.ok_button.Bind(wx.EVT_BUTTON, self.onPressOk)

        self.Centre()
        self.panel.SetSizer(vbox)


    def onPressOk(self, event):

        self.Destroy()


class editor_pessoa(wx.Dialog):


    def __init__(self, parent, index, selection):
        super(editor_pessoa, self).__init__(parent=parent, size=(430, 226), title='Editor')
        self.panel = wx.Panel(self)
        self.fld_id = wx.TextCtrl(self.panel, size=(60, 23), style=wx.TE_READONLY)
        self.fld_name = wx.TextCtrl(self.panel, size=(200, 23))
        self.fld_idc = wx.TextCtrl(self.panel, size=(60, 23))
        self.fld_namec = wx.TextCtrl(self.panel, size=(200, 23), style=wx.TE_READONLY)
        choices = ['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo', 'Morto']
        self.fld_civil = wx.Choice(self.panel, size=(110, 23), choices=choices)
        self.fld_phone = wx.TextCtrl(self.panel, size=(125, 23))
        self.fld_adress = wx.TextCtrl(self.panel, size=(316, 23))
        self.index = index
        self.parent = parent
        self.selection = selection
        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.first_civil = -1
        self.first_idc = 'NULL'
        self.init_Editor()


    def init_Editor(self):
        txt_id = wx.StaticText(self.panel, label='ID Pessoa: ', size=(66, 18))
        txt_name = wx.StaticText(self.panel, label='Nome: ', size=(36, 18))
        txt_idc = wx.StaticText(self.panel, label='ID Cônjuge: ', size=(66, 18))
        txt_namec = wx.StaticText(self.panel, label='Nome: ', size=(36, 18))
        txt_civil = wx.StaticText(self.panel, label='Estado Civil: ', size=(66, 18))
        txt_phone = wx.StaticText(self.panel, label='Telefone: ', size=(56, 18))
        txt_adress = wx.StaticText(self.panel, label='Endereço: ', size=(66, 18))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(txt_id, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(self.fld_id, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(txt_name, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(self.fld_name, 0, wx.ALIGN_CENTER)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(txt_idc, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(10)
        hbox2.Add(self.fld_idc, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(10)
        hbox2.Add(txt_namec, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(10)
        hbox2.Add(self.fld_namec, 0, wx.ALIGN_CENTER)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(txt_civil, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(10)
        hbox3.Add(self.fld_civil, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(20)
        hbox3.Add(txt_phone, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(5)
        hbox3.Add(self.fld_phone, 0, wx.ALIGN_CENTER)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(txt_adress, 0, wx.ALIGN_CENTER)
        hbox4.AddSpacer(10)
        hbox4.Add(self.fld_adress, 0, wx.ALIGN_CENTER)

        if self.selection == 0:
            att_btn = wx.Button(self.panel, label='Atualizar pessoa', size=(123, 25))
            del_btn = wx.Button(self.panel, label='Deletar pessoa', size=(123, 25))
            shw_btn = wx.Button(self.panel, label='Exibir veículos', size=(123, 25))
            hbox5 = wx.BoxSizer(wx.HORIZONTAL)
            hbox5.Add(att_btn, 0, wx.ALIGN_CENTER)
            hbox5.AddSpacer(13)
            hbox5.Add(del_btn, 0, wx.ALIGN_CENTER)
            hbox5.AddSpacer(13)
            hbox5.Add(shw_btn, 0, wx.ALIGN_CENTER)
            att_btn.Bind(wx.EVT_BUTTON, self.onPressAttButton)
            del_btn.Bind(wx.EVT_BUTTON, self.onPressDelButton)
            shw_btn.Bind(wx.EVT_BUTTON, self.onPressShwButton)
            self.fillSpaces()
        else:
            self.fld_civil.SetSelection(0)
            add_btn = wx.Button(self.panel, label='Adicionar pessoa', size=(395, 25))
            hbox5 = wx.BoxSizer(wx.HORIZONTAL)
            hbox5.Add(add_btn, 0, wx.ALIGN_CENTER)
            add_btn.Bind(wx.EVT_BUTTON, self.onPressAddButton)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(12)
        vbox.Add(hbox1, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox2, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox3, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox4, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox5, 0, wx.ALIGN_CENTER)

        self.Centre()
        self.panel.SetSizer(vbox)


    def fillSpaces(self):

        command = 'SELECT p.* FROM pessoa p ' \
                  'WHERE p.id_pessoa = {0}'.format(self.index)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        self.fld_id.write(str(self.cursor[0][0]))
        self.fld_civil.SetSelection(self.cursor[0][2] - 1)
        self.fld_name.write(str(self.cursor[0][3]))
        self.fld_adress.write(str(self.cursor[0][4]))
        self.fld_phone.write(str(self.cursor[0][5]))
        self.first_civil = self.cursor[0][2]

        if self.cursor[0][2] == 2:
            command = 'SELECT p.id_conjuge, p2.nome FROM pessoa p ' \
                      'JOIN pessoa p2 on p.id_conjuge = p2.id_pessoa ' \
                      'WHERE p.id_pessoa = {0}'.format(self.index)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_execute(self.cursor, command)

            self.fld_idc.write(str(self.cursor[0][0]))
            self.fld_namec.write(str(self.cursor[0][1]))
            self.first_idc = self.cursor[0][0]


    def onPressAttButton(self, event):

        name = self.nullOrNot(self.fld_name.GetLineText(0))
        phone = self.nullOrNot(self.fld_phone.GetLineText(0))
        adress = self.nullOrNot(self.fld_adress.GetLineText(0))
        idc = self.setNull(self.fld_idc.GetLineText(0))
        civil = self.fld_civil.GetSelection() + 1
        valid = 1

        # Condições casamento / separação

        if (not self.isIdValid(self.parent, idc) or idc == self.first_idc) and civil == 2:
            avisos(self.parent, 'O ID do cônjuge é inválido!').Show()
            valid = 0
        elif name == 'NULL':
            avisos(self.parent, 'Digite um nome!').Show()
            valid = 0
        elif phone == 'NULL':
            avisos(self.parent, 'Digite um fone!').Show()
            valid = 0
        elif adress == 'NULL':
            avisos(self.parent, 'Digite um endereço!').Show()
            valid = 0
        elif civil != self.first_civil and civil == 2 and idc != self.first_idc:
            if self.isMarried(idc):
                avisos(self.parent, 'Não é possível realizar este casamento\n'
                                    '    pois o cônjuge já está casado!').Show()
                valid = 0
            else:
                self.getMarried(self.index, idc)
        elif civil == self.first_civil and idc != self.first_idc:
            if not self.isIdValid(self.parent, idc):
                avisos(self.parent, 'O ID do cônjuge é inválido!').Show()
                valid = 0
            else:
                if self.isMarried(idc):
                    avisos(self.parent, 'Não é possível realizar este casamento\n'
                                        '    pois o cônjuge já está casado!').Show()
                    valid = 0
                elif self.first_civil == 2:
                    avisos(self.parent, 'Não é possível realizar este casamento\n'
                                        '      pois a pessoa já está casada!').Show()
                    valid = 0
                else:
                    self.getMarried(self.index, idc)
                    civil = 2

        if civil != self.first_civil and self.first_civil == 2 and civil != 5 and civil != 6:
            self.endMarriage(self.first_idc, civil)

        if civil != 2 and civil != 5 and civil != 6:
            idc = 'NULL'

        if civil == 5 and self.first_civil == 2:
            self.endMarriage(idc, 6)

        if civil == 6 and self.first_civil == 2:
            self.endMarriage(idc, 5)

        if (civil == 5 or civil == 6) and idc == 'NULL':
            idc = self.first_idc

        if valid:
            command = 'UPDATE pessoa p ' \
                      'SET p.nome = {1}, p.fone = {2}, p.endereco = {3}, p.estado_civil = {4}, ' \
                      'p.id_conjuge = {5} ' \
                      'WHERE p.id_pessoa = {0}'.format(self.index, name, phone, adress, civil, idc)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            self.parent.panel2.onPressSrchButton(self.parent.panel2)

            if civil == 5 or civil == 6:
                self.endMarriage(self.index, civil)
            self.Destroy()


    def onPressAddButton(self, event):

        name = self.nullOrNot(self.fld_name.GetLineText(0))
        phone = self.nullOrNot(self.fld_phone.GetLineText(0))
        adress = self.nullOrNot(self.fld_adress.GetLineText(0))
        idc = self.setNull(self.fld_idc.GetLineText(0))
        civil = self.fld_civil.GetSelection()+1
        valid = 1

        # Condições casamento / separação

        if not self.isIdValid(self.parent, idc) and civil == 2:
            avisos(self.parent, 'O ID do cônjuge é inválido!').Show()
            valid = 0
        elif name == 'NULL':
            avisos(self.parent, 'Digite um nome!').Show()
            valid = 0
        elif phone == 'NULL':
            avisos(self.parent, 'Digite um fone!').Show()
            valid = 0
        elif adress == 'NULL':
            avisos(self.parent, 'Digite um endereço!').Show()
            valid = 0
        elif civil == 2 or idc != self.first_idc:
            if not self.isIdValid(self.parent, idc):
                avisos(self.parent, 'O ID do cônjuge é inválido!').Show()
                valid = 0
            elif self.isMarried(idc):
                avisos(self.parent, 'Não é possível realizar este casamento\n'
                                    '    pois o cônjuge já está casado!').Show()
                valid = 0
            else:
                civil = 2


        if valid:
            command = 'INSERT INTO pessoa' \
                      '(nome, fone, endereco, estado_civil, id_conjuge) VALUES' \
                      '({0}, {1}, {2}, {3}, {4})'.format(name, phone, adress, civil, idc)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            if civil == 2:
                self.getMarried(self.getLastId(self.parent), idc)
            self.parent.panel2.onPressAllButton(self.parent.panel2)
            self.Destroy()


    def onPressDelButton(self, event):

        command = 'SELECT p.estado_civil FROM pessoa p ' \
                  'WHERE p.id_pessoa = {0}'.format(self.index)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        if self.cursor[0][0] == 2:
            avisos(self.parent, 'Não é possível excluir esta pessoa\n'
                                '           pois ela está casada.').Show()
        elif self.ownVehicles():
            avisos(self.parent, 'Não é possível excluir esta pessoa\n'
                                '       pois ela possui um carro.').Show()
        else:
            command = 'DELETE FROM pessoa ' \
                      'WHERE id_pessoa = {}'.format(self.index)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            self.parent.panel2.onPressSrchButton(self.parent.panel2)
            self.Destroy()


    def onPressShwButton(self, event):

        if not self.ownVehicles():
            avisos(self.parent, 'Esta pessoa não possui veículos.').Show()
        else:
            self.parent.panel3.v_list.DeleteAllItems()

            command = 'SELECT v.* FROM vw_veiculos v ' \
                      'JOIN pertence per ON v.num_chassi = per.num_chassi ' \
                      'JOIN pessoa p ON per.id_pessoa = p.id_pessoa ' \
                      'WHERE per.dono_atual = 1 AND p.id_pessoa = {}'.format(self.index)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_execute(self.cursor, command)

            index = 0
            for info in self.cursor:
                self.parent.panel3.v_list.InsertItem(index, str(info[0]))
                self.parent.panel3.v_list.SetItem(index, 1, info[1])
                self.parent.panel3.v_list.SetItem(index, 2, info[2])
                self.parent.panel3.v_list.SetItem(index, 3, str(info[3]))
                index += 1

            self.parent.panel3.choicebox.SetSelection(1)
            self.parent.panel3.Show()
            self.parent.panel2.Hide()
            self.parent.Layout()
            self.Destroy()


    def ownVehicles(self):

        command = 'SELECT per.num_chassi FROM pertence per ' \
                  'JOIN pessoa p ON per.id_pessoa = p.id_pessoa ' \
                  'WHERE per.dono_atual = 1 AND p.id_pessoa = {}'.format(self.index)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        if not self.cursor:
            return []
        else:
            vehicle_num = []
            for i in self.cursor:
                vehicle_num.append(i)
            return vehicle_num


    def isMarried(self, id_fiance):

        command = 'SELECT p.estado_civil FROM pessoa p ' \
                  'WHERE p.id_pessoa = {}'.format(id_fiance)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        if self.cursor[0][0] == 2:
            return 1
        return 0


    def getMarried(self, id_self, id_fiance):

        command = 'UPDATE pessoa p ' \
                  'SET p.id_conjuge = {}, p.estado_civil = 2 ' \
                  'WHERE p.id_pessoa = {}'.format(id_self, id_fiance)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)


    def endMarriage(self, id_self, newCivil):

        command = 'UPDATE pessoa p ' \
                  'SET p.id_conjuge = NULL, p.estado_civil = {} ' \
                  'WHERE p.id_pessoa = {}'.format(newCivil, id_self)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)


    @staticmethod
    def getLastId(parent):

        command = 'SELECT id_pessoa ' \
                  'FROM pessoa ORDER BY id_pessoa ' \
                  'DESC LIMIT 1'

        cursor = Datacom.start_cursor(parent.mydb)
        cursor = Datacom.cursor_execute(cursor, command)

        return cursor[0][0]


    @staticmethod
    def isIdValid(parent, id_search):

        command = 'SELECT p.id_pessoa ' \
                  'FROM pessoa p ' \
                  'WHERE p.id_pessoa = {}'.format(id_search)

        cursor = Datacom.start_cursor(parent.mydb)
        cursor = Datacom.cursor_execute(cursor, command)

        if not cursor:
            return 0
        return 1


    @staticmethod
    def setNull(text):
        if text == '':
            return 'NULL'
        else:
            return text


    @staticmethod
    def nullOrNot(text):
        if text == '':
            return 'NULL'
        else:
            return '\'{}\''.format(text)


class editor_veiculo(wx.Dialog):


    def __init__(self, parent, chassis, selection):

        super(editor_veiculo, self).__init__(parent=parent, size=(430, 256), title='Editor')
        self.panel = wx.Panel(self)
        self.fld_id = wx.TextCtrl(self.panel, size=(74, 23))
        self.fld_name = wx.TextCtrl(self.panel, size=(186, 23), style=wx.TE_READONLY)
        self.fld_chassis = None
        self.fld_price = wx.TextCtrl(self.panel, size=(110, 23))
        self.fld_model = wx.TextCtrl(self.panel, size=(125, 23))
        self.fld_brand = wx.TextCtrl(self.panel, size=(110, 23))
        self.fld_color = wx.TextCtrl(self.panel, size=(70, 23))
        self.fld_year = wx.TextCtrl(self.panel, size=(50, 23))
        self.fld_bdate = wx.TextCtrl(self.panel, size=(90, 23))
        self.chassis = chassis
        self.parent = parent
        self.selection = selection
        self.owner_id = None
        self.cursor = None
        self.history = None
        self.init_Editor()


    def init_Editor(self):

        txt_id = wx.StaticText(self.panel, label='ID Dono: ', size=(66, 18))
        txt_name = wx.StaticText(self.panel, label='Nome: ', size=(36, 18))
        txt_chassis = wx.StaticText(self.panel, label='Chassi: ', size=(66, 18))
        txt_price = wx.StaticText(self.panel, label='Preço: ', size=(56, 18))
        txt_model = wx.StaticText(self.panel, label='Modelo: ', size=(66, 18))
        txt_brand = wx.StaticText(self.panel, label='Marca: ', size=(56, 18))
        txt_color = wx.StaticText(self.panel, label='Cor: ', size=(36, 18))
        txt_year = wx.StaticText(self.panel, label='Ano: ', size=(36, 18))
        txt_bdate =  wx.StaticText(self.panel, label='DT Compra: ', size=(66, 18))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(txt_id, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(self.fld_id, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(txt_name, 0, wx.ALIGN_CENTER)
        hbox1.AddSpacer(10)
        hbox1.Add(self.fld_name, 0, wx.ALIGN_CENTER)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(txt_chassis, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(10)
        if self.selection == 0:
            self.fld_chassis = wx.TextCtrl(self.panel, size=(125, 23), style=wx.TE_READONLY)
        else:
            self.fld_chassis = wx.TextCtrl(self.panel, size=(125, 23))
        hbox2.Add(self.fld_chassis, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(20)
        hbox2.Add(txt_price, 0, wx.ALIGN_CENTER)
        hbox2.AddSpacer(5)
        hbox2.Add(self.fld_price, 0, wx.ALIGN_CENTER)


        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(txt_model, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(10)
        hbox3.Add(self.fld_model, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(20)
        hbox3.Add(txt_brand, 0, wx.ALIGN_CENTER)
        hbox3.AddSpacer(5)
        hbox3.Add(self.fld_brand, 0, wx.ALIGN_CENTER)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(txt_bdate, 0, wx.ALIGN_CENTER)
        hbox4.AddSpacer(10)
        hbox4.Add(self.fld_bdate, 0, wx.ALIGN_CENTER)
        hbox4.AddSpacer(15)
        hbox4.Add(txt_color, 0, wx.ALIGN_CENTER)
        hbox4.Add(self.fld_color, 0, wx.ALIGN_CENTER)
        hbox4.AddSpacer(15)
        hbox4.Add(txt_year, 0, wx.ALIGN_CENTER)
        hbox4.AddSpacer(4)
        hbox4.Add(self.fld_year, 0, wx.ALIGN_CENTER)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(12)
        vbox.Add(hbox1, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox4, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox3, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(12)
        vbox.Add(hbox2, 0, wx.ALIGN_CENTER)

        if self.selection == 0:
            att_btn = wx.Button(self.panel, label='Atualizar veículo', size=(181, 25))
            del_btn = wx.Button(self.panel, label='Deletar veículo', size=(181, 25))
            shw_btn = wx.Button(self.panel, label='Exibir proprietário', size=(181, 25))
            his_btn = wx.Button(self.panel, label='Exibir histórico de proprietários', size=(181, 25))
            hbox5 = wx.BoxSizer(wx.HORIZONTAL)
            hbox5.Add(att_btn, 0, wx.ALIGN_CENTER)
            hbox5.AddSpacer(13)
            hbox5.Add(del_btn, 0, wx.ALIGN_CENTER)
            hbox6 = wx.BoxSizer(wx.HORIZONTAL)
            hbox6.Add(shw_btn, 0, wx.ALIGN_CENTER)
            hbox6.AddSpacer(13)
            hbox6.Add(his_btn, 0, wx.ALIGN_CENTER)
            vbox.AddSpacer(12)
            vbox.Add(hbox5, 0, wx.ALIGN_CENTER)
            vbox.AddSpacer(6)
            vbox.Add(hbox6, 0, wx.ALIGN_CENTER)

            att_btn.Bind(wx.EVT_BUTTON, self.onPressAttButton)
            del_btn.Bind(wx.EVT_BUTTON, self.onPressDelButton)
            shw_btn.Bind(wx.EVT_BUTTON, self.onPressShwButton)
            his_btn.Bind(wx.EVT_BUTTON, self.onPressHisButton)
            self.fillSpaces()
        else:
            add_btn = wx.Button(self.panel, label='Adicionar veículo', size=(395, 50))
            hbox5 = wx.BoxSizer(wx.HORIZONTAL)
            hbox5.Add(add_btn, 0, wx.ALIGN_CENTER)
            add_btn.Bind(wx.EVT_BUTTON, self.onPressAddButton)
            vbox.AddSpacer(18)
            vbox.Add(hbox5, 0, wx.ALIGN_CENTER)


        self.Centre()
        self.panel.SetSizer(vbox)


    def fillSpaces(self):

        command = 'SELECT v.*, p.id_pessoa, p.nome, per.data_compra ' \
                  'FROM veiculo v ' \
                  'JOIN pertence per ON per.num_chassi = v.num_chassi ' \
                  'JOIN pessoa p ON per.id_pessoa = p.id_pessoa ' \
                  'WHERE v.num_chassi = \'{}\' AND per.dono_atual = 1'.format(self.chassis)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        self.fld_chassis.write(self.cursor[0][0])
        self.fld_price.write(str(self.cursor[0][1]))
        self.fld_color.write(self.cursor[0][2])
        self.fld_year.write(str(self.cursor[0][3]))
        self.fld_model.write(self.cursor[0][4])
        self.fld_brand.write(self.cursor[0][5])
        self.fld_id.write(str(self.cursor[0][6]))
        self.fld_name.write(self.cursor[0][7])
        self.fld_bdate.write(self.cursor[0][8])
        self.owner_id = self.cursor[0][6]


    def onPressDelButton(self, event):

        if self.history:
            self.history.Destroy()

        command = 'DELETE FROM pertence ' \
                  'WHERE num_chassi = \'{}\''.format(self.chassis)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)

        command = 'DELETE FROM veiculo ' \
                  'WHERE num_chassi = \'{}\''.format(self.chassis)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
        self.parent.panel3.onPressSrchButton(self.parent.panel3)
        self.Destroy()


    def onPressAddButton(self, event):

        chassis = editor_pessoa.nullOrNot(self.fld_chassis.GetLineText(0))
        bdate = editor_pessoa.nullOrNot(self.fld_bdate.GetLineText(0))
        brand = editor_pessoa.nullOrNot(self.fld_brand.GetLineText(0))
        model = editor_pessoa.nullOrNot(self.fld_model.GetLineText(0))
        color = editor_pessoa.nullOrNot(self.fld_color.GetLineText(0))
        year = editor_pessoa.setNull(self.fld_year.GetLineText(0))
        id_person = editor_pessoa.setNull(self.fld_id.GetLineText(0))
        price = editor_pessoa.setNull(self.fld_price.GetLineText(0))
        valid = 1

        if not editor_pessoa.isIdValid(self.parent, id_person):
            avisos(self.parent, 'Não é possível adicionar o carro\n'
                                '    pois o ID do dono é inválido!').Show()
            valid = 0
        elif self.isChassisOnDb(self.parent, chassis) or chassis == 'NULL':
            avisos(self.parent, 'Não é possível adicionar o carro\n'
                                'pois o número do chassi já está\n'
                                '      cadastrado ou é inválido!').Show()
            valid = 0
        elif year == 'NULL':
            avisos(self.parent, 'Digite um ano!').Show()
            valid = 0
        elif bdate == 'NULL':
            avisos(self.parent, 'Digite uma data de compra!').Show()
            valid = 0
        elif price == 'NULL':
            avisos(self.parent, 'Digite um preço!').Show()
            valid = 0
        elif model == 'NULL':
            avisos(self.parent, 'Digite um modelo!').Show()
            valid = 0
        elif brand == 'NULL':
            avisos(self.parent, 'Digite uma marca!').Show()
            valid = 0
        elif color == 'NULL':
            avisos(self.parent, 'Digite uma cor!').Show()
            valid = 0

        if valid:
            command = 'INSERT INTO veiculo' \
                      '(num_chassi, marca, modelo, cor, ano, preco) VALUES ' \
                      '({0}, {1}, {2}, {3}, {4}, {5})' \
                      ''.format(chassis, brand, model, color, year, price)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)

            command = 'INSERT INTO pertence' \
                      '(num_chassi, id_pessoa, data_compra) VALUES ' \
                      '({}, {}, {})' \
                      ''.format(chassis, id_person, bdate)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            self.parent.panel3.onPressAllButton(self.parent.panel3)
            self.Destroy()


    def onPressShwButton(self, event):

        self.parent.panel2.p_list.DeleteAllItems()


        command = 'SELECT p.* FROM vw_pessoas p ' \
                  'JOIN pertence per ON p.id_pessoa = per.id_pessoa ' \
                  'WHERE per.dono_atual = 1 AND per.num_chassi = \'{}\''.format(self.chassis)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        self.parent.panel2.p_list.InsertItem(0, str(self.cursor[0][0]))
        self.parent.panel2.p_list.SetItem(0, 1, self.cursor[0][1])
        self.parent.panel2.p_list.SetItem(0, 2, self.cursor[0][2])
        self.parent.panel2.p_list.SetItem(0, 3, self.cursor[0][3])

        self.parent.panel2.choicebox.SetSelection(0)
        self.parent.panel2.Show()
        self.parent.panel3.Hide()
        self.parent.Layout()
        self.Destroy()


    def onPressAttButton(self, event):

        if self.history:
            self.history.Destroy()

        bdate = editor_pessoa.nullOrNot(self.fld_bdate.GetLineText(0))
        brand = editor_pessoa.nullOrNot(self.fld_brand.GetLineText(0))
        model = editor_pessoa.nullOrNot(self.fld_model.GetLineText(0))
        color = editor_pessoa.nullOrNot(self.fld_color.GetLineText(0))
        year = editor_pessoa.setNull(self.fld_year.GetLineText(0))
        id_person = editor_pessoa.setNull(self.fld_id.GetLineText(0))
        price = editor_pessoa.setNull(self.fld_price.GetLineText(0))
        valid = 1
        new_owner = 0

        if not editor_pessoa.isIdValid(self.parent, id_person):
            avisos(self.parent, 'Não é possível atualizar o carro\n'
                                '    pois o ID do dono é inválido!').Show()
            valid = 0
        elif year == 'NULL':
            avisos(self.parent, 'Digite um ano!').Show()
            valid = 0
        elif bdate == 'NULL':
            avisos(self.parent, 'Digite uma data de compra!').Show()
            valid = 0
        elif price == 'NULL':
            avisos(self.parent, 'Digite um preço!').Show()
            valid = 0
        elif model == 'NULL':
            avisos(self.parent, 'Digite um modelo!').Show()
            valid = 0
        elif brand == 'NULL':
            avisos(self.parent, 'Digite uma marca!').Show()
            valid = 0
        elif color == 'NULL':
            avisos(self.parent, 'Digite uma cor!').Show()
            valid = 0
        elif id_person != str(self.owner_id):
            new_owner = 1
        
        if valid:
            command = 'UPDATE veiculo ' \
                      'SET marca = {1}, modelo = {2}, cor = {3}, ano = {4}, preco = {5} ' \
                      'WHERE num_chassi = {0}'.format(self.chassis, brand, model, color, year, price)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            
            if new_owner:
                command = 'SELECT id_pertence FROM pertence ' \
                          'WHERE num_chassi = \'{}\''.format(self.chassis)

                self.cursor = Datacom.start_cursor(self.parent.mydb)
                self.cursor = Datacom.cursor_execute(self.cursor, command)
                
                command = 'UPDATE pertence ' \
                          'SET dono_atual = 0 ' \
                          'WHERE num_chassi = \'{}\''.format(self.chassis)
                
                self.cursor = Datacom.start_cursor(self.parent.mydb)
                self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
                
                command = 'INSERT INTO pertence' \
                          '(id_pessoa, num_chassi, data_compra, dono_atual) VALUES ' \
                          '({0}, {1}, {2}, 1)'.format(id_person, self.chassis, bdate)

                self.cursor = Datacom.start_cursor(self.parent.mydb)
                self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
            
            self.parent.panel3.onPressSrchButton(self.parent.panel3)
            self.Destroy()


    def onPressHisButton(self, event):

        self.history = exibir_historico(self.parent, self.chassis)
        self.history.Centre()
        self.history.Show()
    

    @staticmethod
    def isChassisOnDb(parent, num_chassi):

        command = 'SELECT v.num_chassi ' \
                  'FROM veiculo v ' \
                  'WHERE v.num_chassi = {}'.format(num_chassi)

        cursor = Datacom.start_cursor(parent.mydb)
        cursor = Datacom.cursor_execute(cursor, command)

        if cursor:
            return 1
        return 0
    

class exibir_historico(wx.Dialog):
    
    
    def __init__(self, parent, chassis):

        super(exibir_historico, self).__init__(parent=parent, size=(500, 226), title='Histórico')
        self.panel = wx.Panel(self)
        self.chassis = chassis
        self.list = wx.ListCtrl(self.panel, wx.ID_ANY, style=wx.LC_REPORT, size=(-1, 125))
        self.list.InsertColumn(0, 'ID Dono', width=60)
        self.list.InsertColumn(1, 'Nome', width=160)
        self.list.InsertColumn(2, 'Data da compra', width=100)
        self.list.InsertColumn(3, 'Dono atual?', width=80)
        self.list.InsertColumn(4, 'ID', width=60)
        self.del_btn = wx.Button(self.panel, label='Deletar histórico de edição selecionado', size=(466, 25))
        self.del_btn.Bind(wx.EVT_BUTTON, self.onPressDelButton)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.AddSpacer(15)
        self.vbox.Add(self.list, 0, wx.ALIGN_CENTER)
        self.vbox.AddSpacer(11)
        self.vbox.Add(self.del_btn, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.vbox)
        self.parent = parent
        self.cursor = None
        self.fillSpaces()


    def fillSpaces(self):

        self.list.DeleteAllItems()

        command = 'SELECT * FROM vw_hist_donos ' \
                  'WHERE num_chassi = \'{}\''.format(self.chassis)

        self.cursor = Datacom.start_cursor(self.parent.mydb)
        self.cursor = Datacom.cursor_execute(self.cursor, command)

        index = 0
        for info in self.cursor:
            self.list.InsertItem(index, str(info[0]))
            self.list.SetItem(index, 1, info[1])
            self.list.SetItem(index, 2, info[2])
            if info[3]:
                self.list.SetItem(index, 3, 'Sim')
            else:
                self.list.SetItem(index, 3, 'Não')
            self.list.SetItem(index, 4, str(info[4]))
            index += 1


    def onPressDelButton(self, event):

        if self.list.GetFocusedItem() != -1:
            id_del = self.list.GetItemText(self.list.GetFocusedItem(), 4)

            command = 'SELECT dono_atual FROM pertence ' \
                      'WHERE id_pertence = {}'.format(id_del)

            self.cursor = Datacom.start_cursor(self.parent.mydb)
            self.cursor = Datacom.cursor_execute(self.cursor, command)

            print(self.cursor[0][0])

            if self.cursor[0][0]:
                avisos(self.parent, 'Não é possível excluir o dado selecionado\n'
                                    'pois esta pessoa é a atual dona do carro!').Show()
            else:
                command = 'DELETE FROM pertence ' \
                          'WHERE id_pertence = {}'.format(id_del)

                self.cursor = Datacom.start_cursor(self.parent.mydb)
                self.cursor = Datacom.cursor_commit(self.parent.mydb, self.cursor, command)
                self.fillSpaces()