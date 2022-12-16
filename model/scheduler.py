import builtins
from enum import Enum
from model.process import Process


class SchedulingAlgorithm (Enum):
    ROUND_ROBIN = 1
    COMPLETELY_FAIR_SCHEDULING = 2


class Scheduler:
    def __init__(self, scheduling_algorithm: SchedulingAlgorithm):
        self.ready = []
        self.blocked = []
        self.scheduling_algorithm = scheduling_algorithm

    def add_to_ready(self, process: Process):
        self.ready.append(process)

    def get_next_ready(self):
        return self.ready.pop(0)

    def add_to_blocked(self, process: Process):
        self.ready.append(process)

    def completely_fair_scheduling(self):
        pass

    def sort_ready_queue(self):

        if self.scheduling_algorithm == SchedulingAlgorithm.ROUND_ROBIN:
            pass  # Round Robin é FIFO com preempção e sem prioridade. Não há necessidade de ordenação.

        elif self.scheduling_algorithm == SchedulingAlgorithm.COMPLETELY_FAIR_SCHEDULING:
            self.completely_fair_scheduling()

    def ready_is_empty(self):
        return len(self.ready) == 0
