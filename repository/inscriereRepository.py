from repository.repository import Repository

class InscriereRepository(Repository):

    def __init__(self, persoanaRepository, evenimentRepository):
        super().__init__()
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def adauga(self, inscriere):
        idPersoana = inscriere.getIdPersoana()
        idEveniment = inscriere.getIdEveniment()

        if self.__persoanaRepository.getById(idPersoana) == -1 or self.__evenimentRepository.getById(idEveniment) == -1:
            raise KeyError("Persoana sau evenimentul nu exista!")
        elif self.gasesteInscriereDupaId(idPersoana, idEveniment) != -1:
            raise KeyError("Persoana este deja inscrisa la acest eveniment!")
        else:
            super().adauga(inscriere)

    def gasesteInscriereDupaId(self, idPersoana, idEveniment):
        for i in range(0, len(self._lista)):
            inscriereCurenta = self._lista[i]
            if inscriereCurenta.getIdPersoana() == idPersoana and inscriereCurenta.getIdEveniment() == idEveniment:
                return i
        return -1

    def existaInscriereEveniment(self, idEveniment):
        for i in range (0, len(self._lista)):
            inscriereCurenta = self._lista[i]
            if inscriereCurenta.getIdEveniment() == idEveniment:
                return True
        return False

    def stergeInscrieriEveniment(self, idEveniment):
        i = 0
        while i < len(self._lista):
            inscriereCurenta = self._lista[i]
            if inscriereCurenta.getIdEveniment() == idEveniment:
                idInscriere = inscriereCurenta.getIdEntitate()
                super().sterge(idInscriere)
                i = i - 1
            i = i + 1