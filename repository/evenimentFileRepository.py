from domeniu.eveniment import Eveniment
from repository.evenimentRepository import EvenimentRepository

class EvenimentFileRepository(EvenimentRepository):
    
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()
        
    def adauga(self, eveniment):
        super().adauga(eveniment)
        self.scrie_in_fisier()

    def modifica(self, eveniment):
        super().modifica(eveniment)
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
                data = lista_atribute[1]
                durata = lista_atribute[2]
                descriere = lista_atribute[3]
                eveniment = Eveniment(id, data, durata, descriere)
                super().adauga(eveniment)
                linie = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier)

    def scrie_in_fisier(self):
        try:
            f = open(self.__nume_fisier, "w")
            lista_evenimente = super().getAll()
            for eveniment in lista_evenimente:
                id = eveniment.getIdEntitate()
                data = eveniment.getData()
                durata = eveniment.getTimp()
                descriere = eveniment.getDescriere()
                linie = str(id) + "," + data + "," + durata + "," + descriere + "\n"
                f.write(linie)
            f.close()
        except IOError:
            print("Eroare la deschiderea fisierului " + self.__nume_fisier)