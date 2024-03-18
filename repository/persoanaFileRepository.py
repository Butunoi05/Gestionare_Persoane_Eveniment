from domeniu.persoana import Persoana
from repository.persoanaRepository import PersoanaRepository
from repository.repository import Repository


class persoanaFileRepository(PersoanaRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self, persoana):
        super().adauga(persoana)
        self.scrie_in_fisier()

    def modifica(self, persoana):
        super().modifica(persoana)
        self.scrie_in_fisier()

    def sterge(self, id):
        super().sterge(id)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        try:
            f = open(self.__nume_fisier, "r")
            linie = f.readline().strip("\n")
            while linie != "":
                lista_atribute = linie.split(",")
                id = lista_atribute[0]
                nume = lista_atribute[1]
                adresa = lista_atribute[2]
                persoana = Persoana(id, nume, adresa)
                super().adauga(persoana)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului")

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w")
            lista_persoane = super().getAll()
            for persoana in lista_persoane:
                id = persoana.getIdEntitate()
                nume = persoana.getNume()
                adresa = persoana.getAdresa()
                linie = str(id) + "," + nume + "," + adresa + "\n"
                f.write(linie)
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier)
