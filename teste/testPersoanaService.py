from repository.repository import Repository
from service.persoanaService import PersoanaService

def testAdaugaPersoanaService():
    persoanaRepository = Repository()
    persoanaService = PersoanaService(persoanaRepository)
    persoanaService.adauga("1", "ana", "albac", "2")

    persoane = persoanaService.getAllPersoane()
    assert len(persoane) == 1
    assert persoane[0].getIdPersoana() == '1'

    try:
        persoanaService.adauga("1", "ion", "rasinari", "2")
        assert False
    except KeyError:
        ...

def testModificaAngajatService():
    angajatRepository = Repository()
    angajatService = PersoanaService(angajatRepository)

    angajatService.adauga("1", "ana", "albac", "2")
    angajatService.modifica("1", "paul", "albac", "2")

    angajati = angajatService.getAllPersoane()
    assert angajati[0].getNume() == "paul"

    try:
        angajatService.modifica("2", "ion", "rasinari", "2")
        assert False
    except KeyError:
        ...

def testStergePersoanaService():
    persoanaRepository = Repository()
    persoanaService = PersoanaService(persoanaRepository)
    persoanaService.adauga("1", "ana", "albac", "2")

    persoanaService.sterge("1")

    angajati = persoanaService.getAllPersoane()
    assert len(angajati) == 0

    try:
        persoanaService.sterge("1")
        assert False
    except KeyError:
        ...
