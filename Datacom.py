# -*- coding: utf-8 -*- #

import mysql.connector as mysql


def start_database():

    mydb = mysql.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="proprietario"
    )

    return mydb


def start_cursor(mydb):

    mycursor = mydb.cursor()

    return mycursor


def cursor_execute(my_cursor, command):

    my_cursor.execute(command)

    my_cursor = my_cursor.fetchall()

    return my_cursor

def cursor_commit(mydb, my_cursor, command):

    my_cursor.execute(command)

    mydb.commit()