from model.Process import Process


class CPU:

    def __init__(self):
        self.reg1 = None
        self.reg2 = None
        self.reg3 = None
        self.pc = None

    def set_context(self, process: Process):
        self.reg1 = process.hardware_context.reg1
        self.reg2 = process.hardware_context.reg2
        self.reg3 = process.hardware_context.reg3
        self.pc = process.hardware_context.pc
