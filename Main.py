# -*- coding: utf-8 -*- #

import GUI
import wx

def main():
    app = wx.App()
    ex = GUI.interface(wid = 530, hei = 583, title = 'Proprietário')
    ex.Show()
    app.MainLoop()



if __name__ == '__main__':
    main()