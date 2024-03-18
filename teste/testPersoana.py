from domeniu.persoana import Persoana

def testPersoana():
    persoana = Persoana("1", "ana", "albac")

    assert persoana.getIdEntitate() == "1"
    assert persoana.getNume() == "ana"
    assert persoana.getAdresa() == "albac"

def testPersoanaSetteri():
    persoana = Persoana("1", "ana", "albac")

    persoana.setIdEntitate("2")
    assert persoana.getIdEntitate() == '2'

    persoana.setNume("paul")
    assert persoana.getNume() == "paul"

    persoana.setAdresa("rasinari")
    assert persoana.getAdresa() == "rasinari"
