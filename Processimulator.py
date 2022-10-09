from ast import Return
from pickle import FALSE
import string
from time import sleep


import time
import random

class Cpu:

    def __init__(self):
        self.bussy = False
    
    def process(self):
        time.sleep(1)

    def getBussy(self):
        return self.bussy

    def setBussy(self,newBussy):
        self.bussy = newBussy


class Simulator:

    def __init__(self,simulation_time,delay,max_next_process_time,max_process_life_time,max_next_IO_time,max_IO_execution_time,quantum):
        self.simulation_time = simulation_time
        self.delay = delay
        self.max_next_process_time = max_next_process_time
        self.max_process_life_time = max_process_life_time
        self.max_next_IO_time = max_next_IO_time
        self.max_IO_execution_time = max_IO_execution_time
        self.quantum = quantum
        self.nextProcessCreator = 0
        self.actualProcess= None
        self.processCreator = ProcessCreator(0)
        self.cpu = Cpu()
        self.blocketProcessList= []
        self.readyProcessList = []

    def print_quantum(self):
        print(self.quantum)

    def randomGeneratorTimeNextProcess(self):
        return random.randint(0,self.max_next_process_time)

    def start(self):
        self.actualProcess = self.processCreator.createProcess(self.max_process_life_time,self.max_next_IO_time,self.max_IO_execution_time)
        self.actualProcess.setQuantum(self.quantum)
        self.actualProcess.setStatus("running")
        self.nextProcessCreator = self.randomGeneratorTimeNextProcess()
        while(self.simulation_time>0):
            self.showInformation()
            if self.actualProcess != None:
                self.actualProcess.print_information()
                if self.actualProcess.getQuantum()>0:
                    self.actualProcess.setQuantum(self.actualProcess.getQuantum()-1)
                if self.actualProcess.getQuantum() == 0:
                    self.blocketProcessList.append(self.actualProcess)
                    self.actualProcess=None
            else:
                print("none");
            if self.nextProcessCreator <= 0:
                self.readyProcessList.append(self.processCreator.createProcess(self.max_process_life_time,self.max_next_IO_time,self.max_IO_execution_time))
                self.nextProcessCreator = self.randomGeneratorTimeNextProcess()
            if self.actualProcess==None:
                self.cpu.setBussy(False)
                if len(self.readyProcessList)>0:
                    self.actualProcess = self.readyProcessList.pop(0)
                    self.actualProcess.setQuantum(self.quantum)                    
            self.simulation_time = self.simulation_time-1
            self.nextProcessCreator = self.nextProcessCreator-1
            self.cpu.process()

    def showInformation(self):
            print("----------------------------------")
            print("Tiempo restante : ",self.simulation_time)
            print("Creacion Proximo Proceso: ",self.nextProcessCreator)
            print("Ready processes queue")
            if len(self.readyProcessList) >0:
                for i in self.readyProcessList:
                    i.print_information()
            else:
                print("None")
            print("blocked processes queue")
            if len(self.blocketProcessList) >0:
                for j in self.blocketProcessList:
                    j.print_information()
            else:
                print("None")
            
            

class Process:

    def __init__(self,id,life_Time,NextIO,IO,status):
        self.id = id
        self.life_Time = life_Time
        self.NextIO = NextIO
        self.IO = IO
        self.status = status
        self.quantum = 0

    def setQuantum(self,newQuantum):
        self.quantum = newQuantum

    def getQuantum(self):
        return self.quantum

    def setStatus(self,newStatus):
        self.status = newStatus

    def print_information(self):
        print("Id: " , self.id , ", Life Time: " , self.life_Time , ", Next IO: ", self.NextIO , ", IO: " , self.IO , ", Status: " , self.status , ", quantum: " ,  self.quantum)

class ProcessCreator:

    def __init__(self,processNumber):
        self.processNumber=processNumber

    def generateRandomTimeLife(self,max_process_life_time):
        return random.randint(1,max_process_life_time)

    def generateRandomIOaction(self,max_next_IO_time):
        return random.randint(1,max_next_IO_time)

    def generateRandomIOtimeAction(self,max_IO_execution_time):
        return random.randint(1,max_IO_execution_time)

    def createProcess(self,max_process_life_time,max_next_IO_time,max_IO_execution_time):
        self.processNumber = self.processNumber + 1
        return Process(self.processNumber,self.generateRandomTimeLife(max_process_life_time),self.generateRandomIOaction(max_next_IO_time),self.generateRandomIOtimeAction(max_IO_execution_time),"Ready")


simulador = Simulator(50,1,5,20,4,4,3)
simulador.start()