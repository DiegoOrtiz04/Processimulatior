import tkinter as tk
from tkinter import ttk
from datetime import datetime



titleWindow = 'Process Manager Project'
colorFondo = '#173055'
colorFuentePrincipal = '#FFFFFF'
mensajeHora='Reloj Sistema:'
mensajeTSimulacion = 'Tiempo de simulacion'
mensajeEstadoCpu='Estado CPU: '
mensajeColaProcesos = 'Cola de Procesos en:'

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
labelTitulo1=tk.Label(ventana,text=titleWindow, bg=colorFondo, fg=colorFuentePrincipal, font=('Mixed',30))
labelTitulo1.grid(row=1, column=1, columnspan=5)

#Componente Hora del sistema
labelHoraSistema=tk.Label(ventana, text=mensajeHora+datetime.now().time().strftime('%H:%M:%S'), bg=colorFondo, fg=colorFuentePrincipal)
labelHoraSistema.grid(row=1, column=10)

#Separador
separador=ttk.Separator(ventana,orient='horizontal')
separador.grid(row=1, column=1, sticky='SWE', columnspan=12)

#Input Tiempo de Simulacion
#Texto Tiempo de simulacion
labelTSimulacion = tk.Label(ventana,text=mensajeTSimulacion,bg=colorFondo, fg=colorFuentePrincipal)
labelTSimulacion.grid(row=2, column=1, sticky='WE', columnspan=3)
#Entrada Tiempo de Simulacion
entryTSimulacion = tk.Entry(ventana)
entryTSimulacion.grid(row=2, column=4, sticky='WE', columnspan=2)
#BotonStarSimulacion
bottomStarSimulacion = tk.Button(ventana, text='>')
bottomStarSimulacion.grid(row=2, column=6)

#Estado CPU
labelEstadoCPU = tk.Label(ventana, text=mensajeEstadoCpu, bg=colorFondo, fg=colorFuentePrincipal)
labelEstadoCPU.grid(row=2, column=9, sticky='WE', columnspan=2)

#Tabla de procesos
panelTablaProcesos = tk.PanedWindow(ventana, bg=colorFuentePrincipal)
panelTablaProcesos.grid(row=3, column=7, sticky='NSWE', columnspan=6, rowspan=2)



#ComboBox Cola de procesos
#Label
labelColaProcesos = tk.Label(ventana, text=mensajeColaProcesos, bg=colorFondo, fg=colorFuentePrincipal)
labelColaProcesos.grid(row=4, column=1,columnspan=3)
#ComboBoxEstados
comboBoxEstadosProcesos = ttk.Combobox(ventana, state='readonly', values=['Blocked','Ready','Execute'])
comboBoxEstadosProcesos.grid(row=4, column=4)

#GraficaEstadoProcesos
panelEstadoProcesos = tk.PanedWindow(ventana,  bg=colorFuentePrincipal)
panelEstadoProcesos.grid(row=5, column=1, sticky='NSWE',columnspan=5, rowspan=3)

#TextArea Eventos
panelEventos = tk.PanedWindow(ventana)
panelEventos.grid(row=6, column=8,sticky='NSWE', columnspan=5, rowspan=2)

ventana.mainloop()