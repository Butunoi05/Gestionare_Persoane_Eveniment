from domeniu.persoana import Persoana
from repository.repository import Repository

class PersoanaService:
    def __init__(self, persoanaRepository: Repository, persoanaEvenimentRepository: Repository):
        self.__persoanaRepository = persoanaRepository
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository

    def getAllPersoane(self):
        '''
        returneaza lista de persoane
        :return: o lista de obiecte de tipul Persoana
        '''
        return self.__persoanaRepository.getAll()


    #def cauta_persoana_id(self, id_persoana):
        #self.__persoanaRepository.getById(id_persoana)


    def adauga(self, idPersoana, nume, adresa):
        '''
        adauga o persoana
        :param idPersoana: int
        :param nume: str
        :param adresa: str
        :return:
        '''
        persoana = Persoana(idPersoana, nume, adresa)
        self.__persoanaRepository.adauga(persoana)

    def modifica(self, idPersoana, numeNou, adresaNoua):
        '''
        modifica o persoana dupa id
        :param idPersoana: str
        :param numeNou: str
        :param adresaNou: str
        :return:
        '''

        persoanaNoua = Persoana(idPersoana, numeNou, adresaNoua)
        self.__persoanaRepository.modifica(persoanaNoua)

    def sterge(self, idPersoana):
        '''
        sterge o persoana dupa id
        :param idPersoana: str
        :return:
        '''
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() == idPersoana:
                self.__persoanaEvenimentRepository.sterge(inscriere.getIdEntitate())
        self.__persoanaRepository.sterge(idPersoana)

    def persoaneLaCeleMaiMulteEvenimente(self):
        evenimentePersoana = {}
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        maxId = 0
        max = 0
        l = []
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() in evenimentePersoana:
                evenimentePersoana[inscriere.getIdPersoana()] += 1
                if int(evenimentePersoana[inscriere.getIdPersoana()]) > int(max):
                    maxId = int(inscriere.getIdPersoana())
                    max = int(evenimentePersoana[inscriere.getIdPersoana()])

            else:
                evenimentePersoana[inscriere.getIdPersoana()] = 1
                if int(evenimentePersoana[inscriere.getIdPersoana()]) > int(max):
                    maxId = int(inscriere.getIdPersoana())
                    max = int(evenimentePersoana[inscriere.getIdPersoana()])
        for inscriere in inscrieri:
            if evenimentePersoana[inscriere.getIdPersoana()] == max:
                evenimentePersoana[inscriere.getIdPersoana()] = 0
                l.append(inscriere.getIdPersoana())
        return l