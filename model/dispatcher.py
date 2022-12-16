from datetime import datetime
import time

from model.cpu import CPU
from model.process import Process, Status
from logger import Logger

class Dispatcher:

    def __init__(self, cpu: CPU):
        self.cpu = cpu

    def run(self, process: Process):

        process.status = Status.RUNNING

        self.cpu.set_context(process)
        Logger.log(datetime.now(), process, "Processo em execução!")

        if process.burst_time <= process.quantum_time:  # Tempo restante de processamento é menor ou igual que o tempo de quantum
            time.sleep(process.burst_time/1000)
            process.burst_time = 0
            process.status = Status.DEAD
            Logger.log(datetime.now(), process, "Processo completamente finalizado!")

        else:
            time.sleep(process.quantum_time/1000)
            process.burst_time -= process.quantum_time
            process.status = Status.READY
            Logger.log(datetime.now(), process, f'Processo finalizado! Ainda resta {process.burst_time}ms de processamento.')

        return process
