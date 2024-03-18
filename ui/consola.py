from service.persoanaService import PersoanaService
from service.evenimentService import EvenimentService
from service.persoanaEvenimentService import PersoanaEvenimentService
from domeniu.exceptii.duplicateError import DuplicateError

class Consola:
    def __init__(self, persoanaService: PersoanaService, evenimentService: EvenimentService, persoanaEvenimentService: PersoanaEvenimentService):
        self.__persoanaEvenimentService = persoanaEvenimentService
        self.__persoanaService = persoanaService
        self.__evenimentService = evenimentService

    def adaugaPersoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei: ")
            nume = input("Dati numele persoanei: ")
            adresa = input("Dati adresa persoanei: ")
            self.__persoanaService.adauga(idPersoana, nume, adresa)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def adaugaEveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            data = input("Dati data organizarii evenimentului: ")
            timp = input("Dati numarul de ore al evenimentului: ")
            descriere = input("Dati o descriere evenimentului: ")
            self.__evenimentService.adauga(idEveniment, data, timp, descriere)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)


    def modificaPersoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei de modificat:")
            numeNou = input("Dati numele nou al persoanei:")
            adresaNou = input("Dati adresa noua al persoanei: ")
            self.__persoanaService.modifica(idPersoana, numeNou, adresaNou)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modificaEveniment(self):
        try:
            idEveniment = input("Dati noul id al evenimentului: ")
            data = input("Dati data noua al evenimentului: ")
            timp = input("Dati timpul nou al evenimentului: ")
            descriere = input("Dati o noua descriere pentru evenimentul selectat: ")
            self.__evenimentService.modifica(idEveniment, data, timp, descriere)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def sterge(self):
        try:
            idPersoana = input("Dati id-ul persoanei de sters: ")
            self.__persoanaService.sterge(idPersoana)
        except KeyError as e:
            print(e)

    def stergeEveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului de sters: ")
            self.__evenimentService.sterge(idEveniment)
        except KeyError as e:
            print(e)

    def inscrierePersoanaLaEveniment(self):
        try:
            idPersoanaEveniment = input("Dati id-ul inscrierii: ")
            idPersoana = input("Dati id-ul persoanei: ")
            idEveniment = input("Dati id-ul evenimentului: ")
            self.__persoanaEvenimentService.adaugaInscriere(idPersoanaEveniment, idPersoana, idEveniment)
        except DuplicateError as e:
            print(e)
        except KeyError as e:
            print(e)

    def stergeInscriere(self):
        idPersoana = input("Dati id-ul persoanei: ")
        idEveniment = input("Dati id-ul evenimentului: ")
        self.__persoanaEvenimentService.stergeInscriere(idPersoana, idEveniment)

    def ordoneazaEvenimenteDupaParticipanti(self):
        rezultat = self.__evenimentService.ordoneazaEvenimenteDupaNrParticipanti()
        self.afiseaza(rezultat)

    def persoaneEvenimenteMax(self):
            rezultat = self.__persoanaService.persoaneLaCeleMaiMulteEvenimente()
            print(rezultat)

    def persoaneInscrisiLaEveniment(self):
        try:
            idEveniment = input("Id eveniment: ")
            listaPersoane = self.__persoanaEvenimentService.persoaneInscriseLaEveniment(idEveniment)
            print(listaPersoane)
        except:
            print("Date incorecte! Reincercati!")

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga persoana")
        print("2. Modifica persoana")
        print("3. Sterge persoana")
        print("a. Afiseaza toate persoanele")
        print("4. Adauga eveniment")
        print("5. Modifica eveniment")
        print("6. Sterge eveniment")
        print("b. Afiseaza toate evenimentele")
        print("7. Inscriere persoana la eveniment")
        print("8. Sterge inscriere")
        print("9. Ordoneaza evenimentele dupa persoane")
        print("10. Id-ul persoanelor participante la cele mai multe evenimente")
        print("11. Id-ul persoanelor inscrise la un eveniment dat")
        print("i. Afiseaza toate inscrierile")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.adaugaPersoana()
            elif optiune == '2':
                self.modificaPersoana()
            elif optiune == '3':
                self.sterge()
            elif optiune == 'a':
                self.afiseaza(self.__persoanaService.getAllPersoane())
            elif optiune == '4':
                self.adaugaEveniment()
            elif optiune == '5':
                self.modificaEveniment()
            elif optiune == '6':
                self.stergeEveniment()
            elif optiune == '7':
                self.inscrierePersoanaLaEveniment()
            elif optiune == '8':
                self.stergeInscriere()
            elif optiune == '9':
                self.ordoneazaEvenimenteDupaParticipanti()
            elif optiune == '10':
                self.persoaneEvenimenteMax()
            elif optiune == '11':
                self.persoaneInscrisiLaEveniment()
            elif optiune == 'i':
                self.afiseaza(self.__persoanaEvenimentService.getAllInscrieri())
            elif optiune == 'b':
                self.afiseaza(self.__evenimentService.getAllEvenimente())
            elif optiune == 'x':
                break
            else:
                print("Optiune gresita, reincercati!")
