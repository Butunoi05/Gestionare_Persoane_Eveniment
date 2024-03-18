from domeniu.exceptii.duplicateError import DuplicateError


class Repository:
    def __init__(self):
        self.__entitati = {}
        self._lista = []

    def getAll(self):
        '''
        returneaza lista de entitati
        :return:
        '''
        return list(self.__entitati.values())

    def entitati(self):
        return list(self.__entitati.values())

    def getById(self, idEntitate):
        '''
        returneaza entitatea cu acelasi id
        :param idEntitate: str
        :return:
        '''
        if idEntitate in self.__entitati:
            return self.__entitati[idEntitate]
        return None

    def adauga(self, entitate):
        '''
        adauga o entitate in dictionar
        :param entitate: str
        :return:
        '''
        if self.getById(entitate.getIdEntitate()) is not None:
            raise DuplicateError("Exista deja o entitate cu id-ul dat!")
        self.__entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entitateNoua):
        '''
        modifica o entitate dupa id
        :param entitateNoua:str
        :return:
        '''
        if self.getById(entitateNoua.getIdEntitate()) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.__entitati[entitateNoua.getIdEntitate()] = entitateNoua

    def sterge(self, idEntitate):
        '''
        sterge o entitate dupa id
        :param idEntitate: str
        :return:
        '''
        if self.getById(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.__entitati.pop(idEntitate)
