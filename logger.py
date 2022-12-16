class Logger:
    @staticmethod
    def log(time, process, msg):
        print(f'[{time}] [{process}] {msg}')

    @staticmethod
    def linebreaker():
        print('')
