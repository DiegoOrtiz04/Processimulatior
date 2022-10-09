from ast import Return
import string
from time import sleep


import time
import random

class Cpu:

    def __init__(self):
        self.bussy = False
        self.actualProcess

    def process():
            time.sleep(1)

class Simulator:

    def __init__(self,simulation_time,delay,max_next_process_time,max_process_life_time,max_next_IO_time,max_IO_execution_time,quantum):
        self.simulation_time = simulation_time
        self.delay = delay
        self.max_next_process_time = max_next_process_time
        self.max_process_life_time = max_process_life_time
        self.max_next_IO_time = max_next_IO_time
        self.max_IO_execution_time = max_IO_execution_time
        self.quantum = quantum
        self.blocketProcessList= []
        self.readyProcessList = []

    def print_quantum(self):
        print(self.quantum)

class Process:

    def __init__(self,id,life_Time,NextIO,IO,status,quantum):
        self.id = id
        self.life_Time = life_Time
        self.NextIO = NextIO
        self.IO = IO
        self.status = status
        self.quantum = quantum

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
        return Process(self.processNumber,self.generateRandomTimeLife(max_process_life_time),self.generateRandomIOaction(max_next_IO_time),self.generateRandomIOtimeAction(max_IO_execution_time),"Ready",0)


simulador = Simulator(50,1,5,20,4,4,3)
simulador.print_quantum()
procesCreator = ProcessCreator(0)
for i in range(1,10):
    proceso = procesCreator.createProcess(20,4,4)
    proceso.print_information()