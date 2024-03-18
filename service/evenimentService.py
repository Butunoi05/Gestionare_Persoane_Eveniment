from domeniu.eveniment import Eveniment
from repository.repository import Repository

class EvenimentService:
    def __init__(self, evenimentRepository: Repository, persoanaEvenimentRepository: Repository):
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository
        self.__evenimentRepository = evenimentRepository

    def getAllEvenimente(self):
        return self.__evenimentRepository.getAll()

    def adauga(self, idEveniment, data, timp, descriere):
        eveniment = Eveniment(idEveniment, data, timp, descriere)
        self.__evenimentRepository.adauga(eveniment)

    def modifica(self, idEvenimentNou, dataNou, timpNou, descriereNou):
        evenimentNou = Eveniment(idEvenimentNou, dataNou, timpNou, descriereNou)
        self.__evenimentRepository.modifica(evenimentNou)

    def sterge(self, idEveniment):
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdEveniment() == idEveniment:
                self.__persoanaEvenimentRepository.sterge(inscriere.getIdEveniment())
        self.__evenimentRepository.sterge(idEveniment)

    def ordoneazaEvenimenteDupaNrParticipanti(self):
        evenimenteNrParticipanti = {}
        inscrieri = self.__persoanaEvenimentRepository.getAll()
        for inscriere in inscrieri:
            if inscriere.getIdEveniment() in evenimenteNrParticipanti:
                evenimenteNrParticipanti[inscriere.getIdEveniment()] += 1
            else:
                evenimenteNrParticipanti[inscriere.getIdEveniment()] = 1
        idEvenimenteOrdonate = sorted(evenimenteNrParticipanti,
                                      key=lambda idEveniment: evenimenteNrParticipanti[idEveniment])
        evenimenteOrdonate = []
        for idEveniment in idEvenimenteOrdonate:
            evenimenteOrdonate.append((idEveniment, evenimenteNrParticipanti[idEveniment]))
        return evenimenteOrdonate



