import string
from time import sleep


import time

class Cpu:

    bussy = False

    def star():
        for i in range(0,50):
            print(i)
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

    def print_quantum(self):
        print(self.quantum)

class Process:
    life_time = 19;


simulador = Simulator(50,1,5,20,4,4,3)
simulador.print_quantum()