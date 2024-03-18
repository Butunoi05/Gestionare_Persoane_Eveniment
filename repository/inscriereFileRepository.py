from domeniu.persoanaEveniment import PersoanaEveniment
from repository.inscriereRepository import InscriereRepository

class InscriereFileRepository(InscriereRepository):
    def __init__(self, nume_fisier, persoanaRepository, evenimentRepository):
        super().__init__(persoanaRepository, evenimentRepository)
        self.__nume_fisier = nume_fisier
        self.citesteDinFisier()

    def adauga(self, inscriere):
        super().adauga(inscriere)
        self.scrieInFisier()

    def modifica(self, inscriere):
        super().modifica(inscriere)
        self.scrieInFisier

    def sterge(self, idEntitate):
        super().sterge(idEntitate)
        self.scrieInFisier()

    def citesteDinFisier(self):
        try:
            f = open(self.__nume_fisier, "r")
            linie = f.readline().strip("\n")
            while linie != "":
                listaAtribute = linie.split(",")
                id = listaAtribute[0]
                persoanaId = listaAtribute[1]
                evenimentId = listaAtribute[2]
                inscriere = PersoanaEveniment(id, persoanaId, evenimentId)
                super().adauga(inscriere)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier)

    def scrieInFisier(self):
        try:
            f = open(self.__nume_fisier, "w")
            listaInscrieri = super().getAll()
            for inscriere in listaInscrieri:
                id = inscriere.getIdEntitate()
                idPersoana = inscriere.getIdPersoana()
                idEveniment = inscriere.getIdEveniment()
                linie = str(id) + "," + str(idPersoana) + "," + str(idEveniment) + "\n"
                f.write(linie)
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului" + self.__nume_fisier)

