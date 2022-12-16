import sys
from datetime import datetime



from logger import Logger
from model.process import Process, Type, Status
from model.scheduler import Scheduler, SchedulingAlgorithm
from model.cpu import CPU
from model.dispatcher import Dispatcher
from input_handler import InputHandler

if __name__ == '__main__':
    processes = []
    menu_choice = -1
    user_choice = -1
    cpu = CPU()
    dispatcher = Dispatcher(cpu)
    scheduler = Scheduler(SchedulingAlgorithm(1))

    while True:

        print("Digite 1 para entrar no menu de criação de processos.")
        print("Digite 2 para mudar o algoritmo de escalonamento.")
        print("Digite 3 para iniciar o processamento.")
        print("Digite 0 para fechar o programa.")

        menu_choice = InputHandler.int_input("Digite sua escolha: ", interval=(0, 3))
        print("\n")

        if menu_choice == 1:
            while True:
                process_pid = InputHandler.int_input("Digite o pid: ", (0, 9999))
                process_name = InputHandler.str_input("Digite o nome: ")
                process_type = InputHandler.process_type_input("Digite o tipo do processo (IO ou CPU): ")
                process_quantum = InputHandler.int_input("Digite o tempo de quantum (ms): ", (1, sys.maxsize))
                process_burst_time = InputHandler.int_input("Digite o burst time(ms): ", (1, sys.maxsize))

                process = Process(process_pid, process_name, process_type, process_quantum, process_burst_time)
                Logger.log(datetime.now(), process, "Processo criado!")

                print("\n")
                print("Digite 1 para criar um novo processo.")
                print("Digite 0 para sair do menu de criação de processos")

                menu_choice = InputHandler.int_input("Digite sua escolha: ", interval=(0, 1))

                if menu_choice == 0:
                    break

        elif menu_choice == 0:
            break

"""
    while not scheduler.ready_is_empty():
        current_process = scheduler.get_next_ready()
        current_process = dispatcher.run(current_process)

        if current_process.status == Status.READY:
            scheduler.add_to_ready(current_process)

        elif current_process.status == Status.BLOCKED:
            scheduler.add_to_blocked(current_process)

        Logger.linebreaker()
"""