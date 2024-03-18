from domeniu.entitate import Entitate


class PersoanaEveniment(Entitate):
    def __init__(self, idPersoanaEveniment, idPersoana, idEveniment):
        super().__init__(idPersoanaEveniment)
        self.__idPersoana = idPersoana
        self.__idEveniment = idEveniment

    def getIdPersoana(self):
        return self.__idPersoana

    def getIdEveniment(self):
        return self.__idEveniment

    def setIdPersoana(self, idPersoana):
        self.__idPersoana = idPersoana

    def setIdEveniment(self, idEveniment):
        self.__idEveniment = idEveniment

    def __str__(self):
        return f'id: {self.getIdEntitate()}, idPersoana: {self.__idPersoana}' \
                f' idEveniment: {self.__idEveniment}'
