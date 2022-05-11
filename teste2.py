class Sistema:
    def __init__(self):
        self.__texto = ''

    def le_entrada(self):
        self.__texto = input()

    def exibe_saida(self):
        print(self.__texto)

sistema = Sistema()
sistema.le_entrada()
sistema.exibe_saida()