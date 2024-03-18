from domeniu.exceptii.duplicateError import DuplicateError
from domeniu.persoanaEveniment import PersoanaEveniment
from repository.repository import Repository


class PersoanaEvenimentService:
    def __init__(self, persoanaEvenimentRepository: Repository, persoanaRepository: Repository, evenimentRepository: Repository):
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def adaugaInscriere(self, idPersoanaEveniment, idPersoana, idEveniment):
        if self.__persoanaRepository.getById(idPersoana) is None:
            raise KeyError("Nu exista o persoana cu id-ul dat!")
        if self.__evenimentRepository.getById(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu id-ul dat!")

        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() == idPersoana and inscriere.getIdEveniment() == idEveniment:
                raise DuplicateError("Persoana este deja inscrisa in evenimentul dat!")

        inscriere = PersoanaEveniment(idPersoanaEveniment, idPersoana, idEveniment)
        self.__persoanaEvenimentRepository.adauga(inscriere)

    def getAllInscrieri(self):
            return self.__persoanaEvenimentRepository.getAll()

    def persoaneInscriseLaEveniment(self, id_Eveniment):
        if self.__evenimentRepository.getById(id_Eveniment) is None:
            raise KeyError("Nu exista un eveniment cu id-ul dat!")

        lista = []
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdEveniment() == id_Eveniment:
                id_Persoana = inscriere.getIdPersoana()
                lista.append(id_Persoana)
        return lista

    def stergeInscriere(self, idPersoana, idEveniment):
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdPersoana() == idPersoana and inscriere.getIdEveniment() == idEveniment:
                self.__persoanaEvenimentRepository.sterge(inscriere.getIdEntitate())
