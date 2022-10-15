import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tables
import threading




titleWindow = 'Process Manager Project'
colorFondo = '#173055'
colorFuentePrincipal = '#FFFFFF'
colorEntry='#F5F5F5'
mensajeHora='Reloj Sistema:'
mensajeTSimulacion = 'Tiempo de simulacion'
mensajeEstadoCpu='Estado CPU: '
mensajeColaProcesos = 'Cola de Procesos en:'
fuenteTitulo =('Mixed',30)
fuentePrincipal =('Mixed,20')

#Ventana Principal
ventana = tk.Tk()
ventana.geometry('1200x720')
ventana.title(titleWindow)
ventana.resizable(0,0)
ventana.config(bg=colorFondo)
#ventana.configure(background='black')

#Configurar el grid
ventana.rowconfigure(0, weight=0)
ventana.rowconfigure(1, weight=2)
ventana.rowconfigure(2, weight=2)
ventana.rowconfigure(3, weight=2)
ventana.rowconfigure(4, weight=2)
ventana.rowconfigure(5, weight=2)
ventana.rowconfigure(6, weight=2)
ventana.rowconfigure(7, weight=2)
ventana.rowconfigure(8, weight=2)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)
ventana.columnconfigure(5, weight=1)
ventana.columnconfigure(6, weight=1)
ventana.columnconfigure(7, weight=1)
ventana.columnconfigure(8, weight=1)
ventana.columnconfigure(9, weight=1)
ventana.columnconfigure(10, weight=1)
ventana.columnconfigure(11, weight=1)
ventana.columnconfigure(12, weight=1)
ventana.columnconfigure(13, weight=1)


#Componente Titulo Principal
labelTitulo1=tk.Label(ventana,text=titleWindow, bg=colorFondo, fg=colorFuentePrincipal, font=fuenteTitulo)
labelTitulo1.grid(row=1, column=1, columnspan=5)

#Componente Hora del sistema
labelHoraSistema=tk.Label(ventana, text=mensajeHora+datetime.now().time().strftime('%H:%M:%S'),
                          bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelHoraSistema.grid(row=1, column=10)
    #Funcionamiento Hora del sistema
def updateHour():
    while True:
        labelHoraSistema.config(text=mensajeHora+datetime.now().time().strftime('%H:%M:%S'))
        time.sleep(1)

hiloTime=threading.Thread(target=updateHour)
hiloTime.start()

#Separador
separador=ttk.Separator(ventana,orient='horizontal')
separador.grid(row=1, column=1, sticky='SWE', columnspan=12)

#Input Tiempo de Simulacion
#Texto Tiempo de simulacion
labelTSimulacion = tk.Label(ventana,text=mensajeTSimulacion,bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelTSimulacion.grid(row=2, column=1, sticky='SWE', columnspan=2)

#Entrada Tiempo de Simulacion

imageSimulacion=tk.PhotoImage(file='sources/images/entry1.png')
labelEntrySimulacion=tk.Label(ventana, image=imageSimulacion, border=0, bg=colorFondo)
labelEntrySimulacion.grid(row=2, column=3, sticky='SWE', columnspan=2)
entryTSimulacion = tk.Entry(ventana, bg=colorEntry, border=0, font=fuentePrincipal, width=15)
entryTSimulacion.grid(row=2, column=3, columnspan=2, sticky='S', pady=10)

#BotonStarSimulacion
imageButtonSimulacion = tk.PhotoImage(file='sources/images/buttom.png')
bottomStarSimulacion = tk.Button(ventana, image=imageButtonSimulacion, bd=0, bg=colorFondo)
bottomStarSimulacion.grid(row=2, column=5, sticky='S')

#Estado CPU
labelEstadoCPU = tk.Label(ventana, text=mensajeEstadoCpu, bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelEstadoCPU.grid(row=2, column=9, sticky='WE', columnspan=2)

#Tabla de procesos
imageTablaProcesos = tk.PhotoImage(file='sources/images/frameEstadoProcesos.png')
labelTablaProceso = tk.Label(ventana, image=imageTablaProcesos, bg=colorFondo)
labelTablaProceso.grid(row=3, column=6, columnspan=7, rowspan=2)
panelTablaProcesos = tk.PanedWindow(ventana, bg='yellow', width=450, height=140)
panelTablaProcesos.grid(row=3, column=6, columnspan=7, rowspan=2)



#ComboBox Cola de procesos
#Label
labelColaProcesos = tk.Label(ventana, text=mensajeColaProcesos, bg=colorFondo, fg=colorFuentePrincipal, font=fuentePrincipal)
labelColaProcesos.grid(row=4, column=1,columnspan=2,sticky='N')
#ComboBoxEstados
comboBoxEstadosProcesos = ttk.Combobox(ventana, state='readonly', values=['Blocked','Ready','Execute'], font=fuentePrincipal)
comboBoxEstadosProcesos.grid(row=4, column=3,sticky='N')

#GraficaEstadoProcesos
imageEstadosProcesos = tk.PhotoImage(file='sources/images/grapframe.png')
labelGrapfEstadosProceso = tk.Label(ventana, image=imageEstadosProcesos, bg=colorFondo, bd=0)
labelGrapfEstadosProceso.grid(row=5, column=1, sticky='NSWE',columnspan=4, rowspan=2)
panelEstadoProcesos = tk.PanedWindow(ventana,  bg='yellow', width=280, height=160)
panelEstadoProcesos.grid(row=5, column=1,columnspan=4, rowspan=2)


#TextArea Eventos
imageEventos=tk.PhotoImage(file='sources/images/frameEventos.png')
labelEventos=tk.Label(ventana, image=imageEventos, bg=colorFondo)
labelEventos.grid(row=6, column=6 ,sticky='NSWE', columnspan=5, rowspan=2)
panelEventos = tk.PanedWindow(ventana, bg='yellow', width=390 , height=130)
panelEventos.grid(row=6, column=6, columnspan=5, rowspan=2)


#Prueba Tablas
def _init():
    table_process_test = tables._set_properties_table_process(panelTablaProcesos)
    table_events_test = tables._set_properties_table_events(panelEventos)
    tables._test_table_process(table_process_test) #Este es pa probar
    tables._test_table_events(table_events_test) #Este es pa probar


#_init()
ventana.mainloop()