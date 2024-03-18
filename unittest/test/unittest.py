#REPOSITORY TEST
import unittest
from domeniu.persoana import Persoana
from repository.repository import Repository
from domeniu.exceptii.duplicateError import DuplicateError

class TestRepository(unittest.TestCase):
    def setUp(self):
        from domeniu.persoana import Persoana
        from repository.repository import Repository
        from domeniu.exceptii.duplicateError import DuplicateError
        self.duplicateError = DuplicateError("mesaj")
        self.repository = Repository()
        persoana = Persoana("1", "Ana", "Albac")
        self.repository.adauga(persoana)

    def test_adauga(self):
        persoana = Persoana("2", "Anastasia", "Albacoi")
        self.repository.adauga(persoana)
        persoane = self.repository.getAll()
        assert len(persoane) == 2
        assert persoane[0].getIdEntitate() == "1"

        try:
            self.repository.adauga(persoana)
        except DuplicateError:
            assert True
    def test_modifica(self):
        persoana_noua1 = Persoana("1", "Maria", "asd")
        persoana_noua2 = Persoana("10", "Ionut", "bsd")
        self.repository.modifica(persoana_noua1)

        persoane = self.repository.entitati()
        assert persoane[0].getNume() == "Maria"

        try:
            self.repository.modifica(persoana_noua2)
        except KeyError:
            assert True

    def test_sterge(self):
        self.repository.sterge("1")

        assert len(self.repository.getAll()) == 0

        try:
            self.repository.sterge("!")
        except KeyError:
            assert True

    def test_str_DuplicateError(self):
        self.assertTrue(self.duplicateError.__str__() == f'DuplicateError: mesaj')

    def tearDown(self) -> None:
        pass

#DOMENIU EVENIMENT+ENTITATE
from unittest import TestCase
class TestEntitate(TestCase):
    def setUp(self):
        from domeniu.entitate import Entitate
        self.entitate = Entitate(1)

    def test_id(self):
        self.assertTrue(self.entitate.getIdEntitate() == 1)

class TestEveniment(TestCase):
    def setUp(self):
        from domeniu.eveniment import Eveniment
        self.eveniment = Eveniment("101", "14.12.2022", "2 ore", "SesiuneaDeNoapte")

    def test_id(self):
        self.assertTrue(self.eveniment.getIdEntitate() == "101", "Id-ul evenimentului trebuie sa fie 101!")
        self.eveniment.setIdEntitate("102")
        self.assertTrue(self.eveniment.getIdEntitate() == "102", "Id-ul evenimentului trebuie sa fie 102!")

    def test_data(self):
        self.assertTrue(self.eveniment.getData() == "14.12.2022", "Data evenimentului trebuie sa fie 14.12.2022")
        self.eveniment.setData("17.12.2022")
        self.assertTrue(self.eveniment.getData() == "17.12.2022", "Data evenimentului trebuie sa fie 17.12.2022")

    def test_timp(self):
        self.assertTrue(self.eveniment.getTimp() == "2 ore", "Timpul evenimentului trebuie sa fie de 2 ore")
        self.eveniment.setTimp("3 ore")
        self.assertTrue(self.eveniment.getTimp() == "3 ore", "Timpul evenimentului trebuie sa fie de 3 ore")

    def test_descriere(self):
        self.assertTrue(self.eveniment.getDescriere() == "SesiuneaDeNoapte", "Descrierea evenimentului trebuie sa fie SesiuneaDeNoapte")
        self.eveniment.setDescriere("SesiuneaDeZi")
        self.assertTrue(self.eveniment.getDescriere() == "SesiuneaDeZi", "Descrierea evenimentului trebuie sa fie SesiuneaDeZi")

    def test_str(self):
        self.assertTrue(self.eveniment.__str__() == f"id: {self.eveniment.getIdEntitate()}, data: {self.eveniment.getData()}, timp: {self.eveniment.getTimp()}, descriere: {self.eveniment.getDescriere()}")

#DOMENIU PERSOANE
from unittest import TestCase

class testPersoana(TestCase):
    def setUp(self):
        from domeniu.persoana import Persoana
        self.persoana = Persoana("1", "Ana", "Aleea Rasinari")

    def test_id(self):
        self.assertTrue(self.persoana.getIdEntitate() == "1", "Id-ul persoanei trebuie sa fie 1")
        self.persoana.setIdEntitate('2')
        self.assertTrue(self.persoana.getIdEntitate() == '2', "Id-ul persoanei trebuie sa fie 2")

    def test_nume(self):
        self.assertTrue(self.persoana.getNume() == "Ana", "Numele persoanei trebuie sa fie Ana")
        self.persoana.setNume("Ioana")
        self.assertTrue(self.persoana.getNume() == "Ioana", "Numele persoanei trebuie sa fie Ioana")

    def test_adresa(self):
        self.assertTrue(self.persoana.getAdresa() == "Aleea Rasinari", "Adresa persoanei trebuie sa fie Aleea Rasinari")
        self.persoana.setAdresa("Albac")
        self.assertTrue(self.persoana.getAdresa() == "Albac", "Adresa persoanei trebuie sa fie Albac")

    def test_str(self):
        self.assertTrue(self.persoana.__str__() == f"id: {self.persoana.getIdEntitate()}, nume: {self.persoana.getNume()}, adresa: {self.persoana.getAdresa()}")


#DOMENIU INSCRIERE
from unittest import TestCase
import unittest

class testPersoanaEveniment(TestCase):
    def setUp(self):
        from domeniu.persoanaEveniment import PersoanaEveniment
        self.persoanaEveniment = PersoanaEveniment('1', '2', '3')

    def test_idInscriere(self):
        self.assertTrue(self.persoanaEveniment.getIdEntitate() == '1', "Id-ul inscrierii trebuie sa fie 1")
        self.persoanaEveniment.setIdEntitate('101')
        self.assertTrue(self.persoanaEveniment.getIdEntitate() == '101', "Id-ul inscrierii trebuie sa fie 101")

    def test_idPersoana(self):
        self.assertTrue(self.persoanaEveniment.getIdPersoana() == '2', "Id-ul persoanei trebuie sa fie 2")
        self.persoanaEveniment.setIdPersoana('202')
        self.assertTrue(self.persoanaEveniment.getIdPersoana() == '202', "Id-ul persoanei trebuie sa fie 202")

    def test_idEveniment(self):
        self.assertTrue(self.persoanaEveniment.getIdEveniment() == '3', "Id-ul evenimentului trebuie sa fie 3")
        self.persoanaEveniment.setIdEveniment('303')
        self.assertTrue(self.persoanaEveniment.getIdEveniment() == '303', "Id-ul evenimentului trebuie sa fie 303")

    def test_str(self):
        self.assertTrue(self.persoanaEveniment.__str__() == f'id: {self.persoanaEveniment.getIdEntitate()}, idPersoana: {self.persoanaEveniment.getIdPersoana()}' \
                f' idEveniment: {self.persoanaEveniment.getIdEveniment()}')


#SERVICE TEST
import unittest
from domeniu.exceptii.duplicateError import DuplicateError

class testPersoanaService(unittest.TestCase):
    def setUp(self):
        from repository.repository import Repository
        from service.persoanaService import PersoanaService
        from service.evenimentService import EvenimentService
        from service.persoanaEvenimentService import PersoanaEvenimentService

        persoanaRepository = Repository()
        persoanaEvenimentRepository = Repository()
        evenimentRepository = Repository()

        self.evenimentService = EvenimentService(evenimentRepository, persoanaEvenimentRepository)
        self.inscriereService = PersoanaEvenimentService(persoanaEvenimentRepository, persoanaRepository, evenimentRepository)
        self.persoanaService = PersoanaService(persoanaRepository, persoanaEvenimentRepository)

        self.persoanaService.adauga("1", "Ana", "Albacoi")
        self.persoanaService.adauga("2", "Ana1", "Albacoi")
        self.persoanaService.adauga("3", "Ana2", "Albacoi")

        self.evenimentService.adauga("1", "asd1", "asd11", "asd")
        self.evenimentService.adauga("2", "asd2", "asd22", "asd")
        self.evenimentService.adauga("3", "asd3", "asd33", "asd")

        self.inscriereService.adaugaInscriere("1", "1", "1")
        self.inscriereService.adaugaInscriere("2", "1", "2")
        self.inscriereService.adaugaInscriere("3", "1", "3")
        self.inscriereService.adaugaInscriere("4", "2", "1")
        self.inscriereService.adaugaInscriere("5", "2", "2")

    def test_adaugaPersoana(self):
        persoane = self.persoanaService.getAllPersoane()

        assert len(persoane) == 3
        assert (persoane[0].getIdEntitate()) == "1"

        """try:
            self.persoanaService.adauga("1", "Maria", "ASDSDD")
            assert False
        except DuplicateError:
            assert True"""

    def test_modificaPersoana(self):
        id = "1"
        nume = "Ioana"
        adresa = "Albac"
        self.persoanaService.modifica(id, nume, adresa)

        persoane = self.persoanaService.getAllPersoane()
        assert len(persoane) == 3
        assert persoane[0].getNume() == "Ioana"
        assert persoane[0].getIdEntitate() == "1"
        assert persoane[0].getAdresa() == "Albac"


    def test_stergePersoana(self):
        self.persoanaService.sterge("1")
        persoane = self.persoanaService.getAllPersoane()

        assert len(persoane) == 2

    def test_persoaneLaCeleMaiMulteEvenimente(self):
        lista = self.persoanaService.persoaneLaCeleMaiMulteEvenimente()
        assert len(lista) == 1


class testInscriere(unittest.TestCase):
    def setUp(self):
        from service.persoanaEvenimentService import PersoanaEvenimentService
        from service.persoanaService import PersoanaService
        from service.evenimentService import EvenimentService
        from repository.repository import Repository

        inscriereRepository = Repository()
        persoanaRepository = Repository()
        evenimentRepository = Repository()

        self.inscriereService = PersoanaEvenimentService(inscriereRepository, persoanaRepository, evenimentRepository)
        self.persoanaService = PersoanaService(persoanaRepository, inscriereRepository)
        self.evenimentService = EvenimentService(evenimentRepository, inscriereRepository)

        self.persoanaService.adauga("1", "Ana", "Albac")
        self.persoanaService.adauga("2", "Bogdan", "Tatarilor")
        self.evenimentService.adauga("1", "11.01.2023", "2 ore", "Untold!")
        self.inscriereService.adaugaInscriere("1", "1", "1")
        self.inscriereService.adaugaInscriere("2", "2", "1")

    def test_adaugaInscriere(self):
        inscrieri = self.inscriereService.getAllInscrieri()
        assert len(inscrieri) == 2

        try:
            self.inscriereService.adaugaInscriere("3", "55", "1")
        except KeyError:
            assert True

        try:
            self.inscriereService.adaugaInscriere("3", "1", "55")
        except KeyError:
            assert True

        try:
            self.inscriereService.adaugaInscriere("3", "1", "1")
        except DuplicateError:
            assert True

    def test_persoaneInscriseLaEveniment(self):
        assert len(self.inscriereService.persoaneInscriseLaEveniment("1")) == 2

        try:
            self.inscriereService.persoaneInscriseLaEveniment("10")
        except KeyError:
            assert True

    def test_stergeInscriere(self):
        self.inscriereService.stergeInscriere("1", "1")
        inscrieri = self.inscriereService.getAllInscrieri()
        assert len(inscrieri) == 1

class testEvenimentService(unittest.TestCase):
    def setUp(self):
        from service.evenimentService import EvenimentService
        from service.persoanaService import PersoanaService
        from repository.repository import Repository
        from service.persoanaEvenimentService import PersoanaEvenimentService

        persoanaRepository = Repository()
        evenimentRepository = Repository()
        persoanaEvenimentRepository = Repository()

        self.persoanaService = PersoanaService(persoanaRepository, persoanaEvenimentRepository)
        self.evenimentService = EvenimentService(evenimentRepository, persoanaEvenimentRepository)
        self.inscriereService = PersoanaEvenimentService(persoanaEvenimentRepository, persoanaRepository, evenimentRepository)

        self.persoanaService.adauga("1", "Ana", "Albac")
        self.persoanaService.adauga("2", "Bogdan", "Tatarilor")

        self.evenimentService.adauga("1", "01.01.2023", "3 ore", "Untold!")
        self.evenimentService.adauga("2", "12.01.2023", "4 ore", "NeverSea!")

        self.inscriereService.adaugaInscriere("1", "1", "1")
        self.inscriereService.adaugaInscriere("2", "1", "2")
        self.inscriereService.adaugaInscriere("3", "2", "2")


    def test_adaugaEveniment(self):
        self.evenimentService.adauga("3", "09.01.2023", "2 ore", "NeverSea!")
        evenimente = self.evenimentService.getAllEvenimente()
        assert len(evenimente) == 3

    def test_stergeEveniment(self):
        self.evenimentService.sterge("1")
        evenimente = self.evenimentService.getAllEvenimente()
        assert len(evenimente) == 1

    def test_modificaEveniment(self):
        self.evenimentService.modifica("1", "05.01.2023", "2.5 ore", "Untold!!!")
        evenimente = self.evenimentService.getAllEvenimente()

        assert evenimente[0].getIdEntitate() == "1"
        assert evenimente[0].getData() == "05.01.2023"
        assert evenimente[0].getTimp() == "2.5 ore"
        assert evenimente[0].getDescriere() == "Untold!!!"

    def test_ordoneazaEvenimenteDupaNrParticipanti(self):
        assert len(self.evenimentService.ordoneazaEvenimenteDupaNrParticipanti()) == 2

    def tearDown(self) -> None:
        pass

