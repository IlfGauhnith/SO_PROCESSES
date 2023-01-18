import sys
from datetime import datetime
from logger import Logger
from model.process import Process, Type, Status
from model.scheduler import Scheduler, SchedulingAlgorithm
from model.cpu import CPU
from model.dispatcher import Dispatcher
from input_handler import InputHandler


def run_dev_mode(scheduler, dispatcher):
    file = open('mock.txt', 'r')
    mocked_processes = file.readline().split(';')

    for process in mocked_processes:
        process = process.split(',')
        scheduler.add_to_ready(Process(int(process[0]), process[1], process[2], int(process[3])))

    while not scheduler.ready_is_empty():

        scheduler.sort_ready_queue()

        for _ in range(0, len(scheduler.ready)):
            current_process = scheduler.get_next_ready()
            current_process = dispatcher.run(current_process, scheduler.quantum_time)

            if current_process.status == Status.READY:
                scheduler.add_to_ready(current_process)

            elif current_process.status == Status.BLOCKED:
                scheduler.add_to_blocked(current_process)

            Logger.linebreaker()


if __name__ == '__main__':
    dev_mode = False
    menu_choice = -1
    user_choice = -1
    cpu = CPU()
    dispatcher = Dispatcher(cpu, True)  # Preemptivo por padrão
    scheduler = Scheduler(SchedulingAlgorithm(1), 100)  # 100ms de quantum e round-robin por padrão.

    if dev_mode:
        run_dev_mode(scheduler, dispatcher)
    else:
        while True:

            print("Digite 1 para entrar no menu de criação de processos.")
            print("Digite 2 para configurar o algoritmo de escalonamento.")
            print("Digite 3 para iniciar o processamento.")
            print("Digite 0 para fechar o programa.")

            menu_choice = InputHandler.int_input("Digite sua escolha: ", interval=(0, 3))
            print("\n")

            if menu_choice == 1:
                while True:
                    process_pid = InputHandler.int_input("Digite o pid: ", interval=(0, 9999))
                    process_name = InputHandler.str_input("Digite o nome: ")
                    process_type = InputHandler.process_type_input("Digite o tipo do processo (IO ou CPU): ")
                    process_burst_time = InputHandler.int_input("Digite o burst time(ms): ", (1, sys.maxsize))

                    process = Process(process_pid, process_name, process_type, process_burst_time)
                    Logger.log(datetime.now(), process, "Processo criado!")
                    scheduler.add_to_ready(process)

                    print("\n")
                    print("Digite 1 para criar um novo processo.")
                    print("Digite 0 para sair do menu de criação de processos")

                    menu_choice = InputHandler.int_input("Digite sua escolha: ", interval=(0, 1))

                    if menu_choice == 0:
                        break

            elif menu_choice == 2:
                print("\n")
                print("Digite 1 para Round-Robin com quantum.")
                print("Digite 2 para Completely Fair Scheduling.")

                user_choice = InputHandler.int_input("Digite sua escolha: ", interval=(1, 2))

                if user_choice == 1:
                    scheduler.scheduling_algorithm = SchedulingAlgorithm.ROUND_ROBIN
                elif user_choice == 2:
                    scheduler.scheduling_algorithm.COMPLETELY_FAIR_SCHEDULING

                scheduler.quantum_time = InputHandler.int_input("Digite o tempo de quantum (ms): ", (1, 9999))
                dispatcher.preemptive = InputHandler.bool_input("Preemptivo (Sim ou Nao)? ")

            elif menu_choice == 3:
                while not scheduler.ready_is_empty():

                    scheduler.sort_ready_queue()

                    for _ in range(0, len(scheduler.ready)):
                        current_process = scheduler.get_next_ready()
                        current_process = dispatcher.run(current_process, scheduler.quantum_time)

                        if current_process.status == Status.READY:
                            scheduler.add_to_ready(current_process)

                        elif current_process.status == Status.BLOCKED:
                            scheduler.add_to_blocked(current_process)

                        Logger.linebreaker()

            elif menu_choice == 0:
                break
