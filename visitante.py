class Visitante:
    def __init__(self, nombre, hora_entrada, tiempo_permanencia):
        self.__nombre = nombre
        self.__entrada = int(hora_entrada)
        self.__permanencia = int(tiempo_permanencia)
        self.__salida = self.__entrada + self.__permanencia

    def get_nombre(self):
        return self.__nombre

    def get_entrada(self):
        return self.__entrada

    def get_permanencia(self):
        return self.__permanencia

    def get_salida(self):
        return self.__salida
