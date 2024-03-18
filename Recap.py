#DOMENIU
class Entitate:
    def __init__(self, idEntitate):
        self.__idEntitate = idEntitate

    def getIdEntitate(self):
        return self.__idEntitate

    def setIdEntitate(self, idEntitate_nou):
        self.__idEntitate = idEntitate_nou

class Persoana(Entitate):
    def __init__(self, idPersoana, nume, adresa):
        super().__init__(idPersoana)
        self.__nume = nume
        self.__adresa = adresa

    def getNume(self):
        return self.__nume

    def getAdreasa(self):
        return self.__adresa

    def setNume(self, nume_nou):
        self.__nume = nume_nou

    def setAdresa(self, adresa_noua):
        self.__adresa = adresa_noua

    def __str__(self):
        return f"id: {self.getIdEntitate()}, nume: {self.getNume()}, adresa: {self.getAdreasa()}"

#REPOSITORY
class Repository:
    def __init__(self):
        self.__entitati = {}

    def getAll(self):
        return list(self.__entitati.values())

    def getById(self, idEntitate):
        if idEntitate in self.__entitati:
            return self.__entitati[idEntitate]
        return None

    def adauga(self, entitate):
        if self.getById(entitate.getIdEntitate()) is not None:
            raise KeyError("Entitatea cu id-ul dat este deja!")
        self.__entitati[entitate.getIdEntitate()] = entitate

    def modifica(self, entitate_noua):
        if self.getById(entitate_noua.getIdEntitate()) is None:
            raise KeyError("Nu exista entitatea cu id-ul dat!")
        self.__entitati[entitate_noua.getIdEntitate()] = entitate_noua

    def sterge(self, idEntitate):
        if idEntitate in self.__entitati:
            self.__entitati.pop(idEntitate)
        else:
            raise KeyError("Nu exista entitate cu id-ul dat!")

#PERSOANA_SERVICE
class PersoanaService:
    def __init__(self, persoanaRepo: Repository):
        self.__persoanaRepo = persoanaRepo

    def getAll(self):
        return self.__persoanaRepo.getAll()

    def adauga(self, id, nume, adresa):
        persoana = Persoana(id, nume, adresa)
        self.__persoanaRepo.adauga(persoana)

    def modifica(self, id, nume_nou, adresa_noua):
        persoana_noua = Persoana(id, nume_nou, adresa_noua)
        return self.__persoanaRepo.modifica(persoana_noua)

    def sterge(self, id):
        return self.__persoanaRepo.sterge(id)

#UI - CONSOLA

class Consola:
    def __init__(self, persoanaService: PersoanaService):
        self.__persoanaService = persoanaService

    def adauga(self):
        try:
            id = int(input("Dati id-ul persoanei: "))
            nume = input("Dati numele persoanei: ")
            adresa = input("Dati adresa persoanei: ")

            self.__persoanaService.adauga(id, nume, adresa)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def sterge(self):
        try:
            id = input("Dati id-ul persoanei pe care il veti sterge: ")
            self.__persoanaService.sterge(id)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifica(self):
        try:
            id = input(int("Dati id-ul persoanei pe care il veti modifica: "))
            nume_nou = input(str("Dati numele nou: "))
            adresa_noua = input(str("Dati adresa noua: "))

            self.__persoanaService.modifica(id, nume_nou, adresa_noua)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)


    def lista(self):
        self.__persoanaService.getAll()

    def meniu(self):
        while True:
            self.print_meniu()
            x = input("Dati optiunea: ")
            if x == '1':
                self.adauga()
            elif x == "2":
                self.modifica()
            elif x == "3":
                self.sterge()
            elif x == 'a':
                print(self.lista())
            elif x == 'x':
                break
            else:
                print("Caracter invalid, reincercati!")

    def print_meniu(self):
        print("1. Adaugare persoana")
        print("2. Modificare persoana")
        print("3. Stergere persoana")
        print("a. Lista persoanelor")
        print("x pentru a iesi din meniu")


#MAIN
def main():

    persoanaSer = PersoanaService(Repository)
    consola = Consola(persoanaSer)

    consola.meniu()

main()