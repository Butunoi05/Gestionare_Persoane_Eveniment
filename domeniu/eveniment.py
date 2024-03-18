from domeniu.entitate import Entitate


class Eveniment(Entitate):
    def __init__(self, idEveniment, data, timp, descriere):
        super().__init__(idEveniment)
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def getData(self):
        return self.__data

    def getTimp(self):
        return self.__timp

    def getDescriere(self):
        return self.__descriere

    def setData(self, data):
        self.__data = data

    def setTimp(self, timp):
        self.__timp = timp

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def __str__(self):
        return f"id: {self.getIdEntitate()}, data: {self.__data}, timp: {self.__timp}, descriere: {self.__descriere}"