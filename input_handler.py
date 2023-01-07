from model.process import Type
class InputHandler:
    @staticmethod
    def int_input(msg, interval=(0, 0)):
        while True:
            try:
                user_input = int(input(msg))

                if interval[0] < interval[1]:
                    if not (interval[0] <= user_input <= interval[1]):
                        raise ValueError()

                break
            except ValueError:
                print("Entrada inválida.\n")

        return user_input

    @staticmethod
    def str_input(msg):
        while True:
            try:
                user_input = str(input(msg))

                if len(user_input) == 0:
                    raise ValueError()

                break
            except ValueError:
                print("Entrada inválida.\n")

        return user_input

    @staticmethod
    def process_type_input(msg):
        while True:
            try:
                user_input = str(input(msg))

                if user_input.upper() != "IO" and user_input.upper() != "CPU":
                    raise ValueError()

                break
            except ValueError:
                print("Entrada inválida.\n")

        if user_input == "IO":
            return Type.IO_BOUND
        else:
            return Type.CPU_BOUND

    @staticmethod
    def bool_input(msg):
        while True:
            try:
                user_input = input(msg).upper()

                if user_input not in ('SIM', 'NAO', 'S', 'N'):
                    raise ValueError()

                break
            except ValueError:
                print("Entrada inválida.\n")

        if user_input == 'SIM' or user_input == 'S':
            return True
        else:
            return False
