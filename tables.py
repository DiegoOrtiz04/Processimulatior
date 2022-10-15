import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, NO, END, RIGHT, Y
import constants as cs
from Processimulatior.Processimulator import Process

window = tk.Tk()


def _init():
    window.geometry('600x400')
    window.title('Hola mundo')
    table = _set_properties_table()
    _testFillTable(table)

def _set_properties_table():
    table_frame = tk.Frame(window)
    table_frame.pack(pady=20)
    table_scroll = tk.Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT,fill=Y)
    table = ttk.Treeview(table_frame,yscrollcommand= table_scroll.set)
    table['columns'] = cs.COLUMNS_NAME
    table_scroll.config(command=table.yview)
    _createTableProcess(table, cs.COLUMNS_PROCESSES_STATUS)
    return table


def _createTableProcess(table,columnsInput):
    table.column("#0",width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[0],width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[1], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[2], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[3], width=80, anchor=CENTER)
    table.column(cs.COLUMNS_NAME[4], width=80, anchor=CENTER)
    table.heading("#0", text='Process', anchor =CENTER)
    table.heading(cs.COLUMNS_NAME[0], text=columnsInput[1], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[1], text=columnsInput[2], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[2], text=columnsInput[3], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[3], text=columnsInput[4], anchor=CENTER)
    table.heading(cs.COLUMNS_NAME[4], text=columnsInput[5], anchor=CENTER)
    table.pack()

#Add elements to table
def _addProcess(table,process):
    table.insert("",END,text=process.id,values=(
        process.life_Time,
        process.NextIO,
        process.IO,
        process.status,
        process.quantum
    ))

def _popProcess(table):
    print(type(table.get_children()))
    print("-----------------------------------------")
    print(table.get_children().__len__())

#(self,id,life_Time,NextIO,IO,status):
def _testFillTable(table):
    for i in range(40):
        _addProcess(table,Process(i,"0/0","2/2",2,"Busy"))

_init()
window.mainloop()
