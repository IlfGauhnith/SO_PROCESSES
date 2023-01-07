import builtins
from enum import Enum
from model.process import Process


class SchedulingAlgorithm (Enum):
    ROUND_ROBIN = 1
    SHORTEST_JOB_FIRST = 2


class Scheduler:
    def __init__(self, scheduling_algorithm: SchedulingAlgorithm, quantum_time: int):
        self.ready = []
        self.blocked = []
        self.scheduling_algorithm = scheduling_algorithm
        self.quantum_time = quantum_time

    def add_to_ready(self, process: Process):
        self.ready.append(process)

    def get_next_ready(self):
        return self.ready.pop(0)

    def add_to_blocked(self, process: Process):
        self.ready.append(process)

    def shortest_job_first(self):
        self.ready.sort(key=lambda p: p.burst_time, reverse=False)

    def sort_ready_queue(self):

        if self.scheduling_algorithm == SchedulingAlgorithm.ROUND_ROBIN:
            pass  # Round Robin é FIFO com preempção e sem prioridade. Não há necessidade de ordenação.

        elif self.scheduling_algorithm == SchedulingAlgorithm.SHORTEST_JOB_FIRST:
            self.shortest_job_first()

    def ready_is_empty(self):
        return len(self.ready) == 0
