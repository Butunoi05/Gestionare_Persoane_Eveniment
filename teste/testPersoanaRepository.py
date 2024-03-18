from domeniu.persoana import Persoana
from repository.repository import Repository

def testAdaugaPersoanaRepository():
    persoanaRepository = Repository()
    persoana = Persoana("1", "ana", "Albac", "2")

    persoanaRepository.adauga(persoana)

    persoane = persoanaRepository.getAll()
    assert len(persoane) == 1
    assert persoane[0].getIdPersoana() == '1'

    try:
        persoanaRepository.adauga(persoana)
        assert False
    except KeyError:
        ...

def testModificaPersoanaRepository():
    persoanaRepository = Repository()
    persoana = Persoana("1", "ana", "albac", "2")
    persoanaNou1 = Persoana("1", "paul", "albac", "2")
    persoanaNou2 = Persoana("2", "ion", "sapca", "2")
    persoanaRepository.adauga(persoana)

    persoanaRepository.modifica(persoanaNou1)

    persoane = persoanaRepository.getAll()
    assert persoane[0].getNume() == "paul"

    try:
        persoanaRepository.modifica(persoanaNou2)
        assert False
    except KeyError:
        ...

def testStergePersoanaRepository():
    persoanaRepository = Repository()
    persoana = Persoana("1", "ana", "albac", "2")
    persoanaRepository.adauga(persoana)

    persoanaRepository.sterge("1")

    assert len(persoanaRepository.getAll()) == 0

    try:
        persoanaRepository.sterge("!")
        assert False
    except KeyError:
        ...