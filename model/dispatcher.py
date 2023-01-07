from datetime import datetime
import time

from model.cpu import CPU
from model.process import Process, Status
from logger import Logger

class Dispatcher:

    def __init__(self, cpu: CPU, preemptive):
        self.cpu = cpu
        self.preemptive = preemptive

    def run(self, process: Process, quantum_time):

        process.status = Status.RUNNING

        self.cpu.set_context(process)
        Logger.log(datetime.now(), process, "Processo em execução!")

        if self.preemptive:
            if process.burst_time <= quantum_time:  # Tempo restante de processamento é menor ou igual que o tempo de quantum
                time.sleep(process.burst_time/1000)
                process.total_cpu_time += process.burst_time
                process.burst_time = 0
                process.status = Status.DEAD
                Logger.log(datetime.now(), process, "Processo completamente finalizado!")

            else:
                time.sleep(quantum_time/1000)
                process.total_cpu_time += quantum_time
                process.burst_time -= quantum_time
                process.status = Status.READY
                Logger.log(datetime.now(), process, f'Processo finalizado! Ainda resta {process.burst_time}ms de processamento.')
        else:
            time.sleep(process.burst_time/1000)
            process.total_cpu_time += process.burst_time
            process.burst_time = 0
            process.status = Status.DEAD
            Logger.log(datetime.now(), process, "Processo completamente finalizado!")

        return process
