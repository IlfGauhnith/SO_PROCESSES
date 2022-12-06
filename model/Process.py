import binascii
import os
from enum import Enum


class Status (Enum):
    RUNNING = 1
    READY = 2
    BLOCKED = 3


class Type (Enum):
    IO_BOUND = 1
    CPU_BOUND = 2


class HardwareContext:

    def __init__(self):
        self.reg1 = binascii.b2a_hex(os.urandom(15))
        self.reg2 = binascii.b2a_hex(os.urandom(15))
        self.reg3 = binascii.b2a_hex(os.urandom(15))
        self.pc = binascii.b2a_hex(os.urandom(15))

    def __str__(self):
        return f'{self.__class__.__name__}:[reg1:{self.reg1}, reg2:{self.reg2}, reg3:{self.reg3}, pc:{self.pc}]'


class Process:

    def __init__(self, pid: int, name: str, process_type: Type):
        self.pid = pid
        self.name = name
        self.type = process_type
        self.total_cpu_time = 0
        self.hardware_context = HardwareContext()
        self.status = Status(2)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}:[pid:{self.pid}, name:{self.name}, process_type:{self.type}, ' \
               f'total_cpu_time:{self.total_cpu_time}, {self.hardware_context}]'
