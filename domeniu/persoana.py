from domeniu.entitate import Entitate


class Persoana(Entitate):
    def __init__(self, idPersoana, nume, adresa):
        super().__init__(idPersoana)
        self.__nume = nume
        self.__adresa = adresa

    def getNume(self):
        '''
        returneaza numele persoanei
        :return:
        '''
        return self.__nume

    def getAdresa(self):
        '''
        returneaza adresa persoanei
        :return:
        '''
        return self.__adresa

    def setNume(self, nume):
        '''
        schimba numele persoanei
        :param nume:
        :return:
        '''
        self.__nume = nume

    def setAdresa(self, adresa):
        '''
        schimba adresa persoanei
        :param adresa:
        :return:
        '''
        self.__adresa = adresa

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.__nume}, adresa: {self.__adresa}"
