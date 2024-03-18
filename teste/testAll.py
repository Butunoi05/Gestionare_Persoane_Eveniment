from teste.testPersoana import testPersoana, testPersoanaSetteri
from teste.testPersoanaRepository import testAdaugaPersoanaRepository, testModificaPersoanaRepository, testStergePersoanaRepository
from teste.testPersoanaService import testAdaugaPersoanaService, testStergePersoanaService, testModificaAngajatService

def testAll():
    testPersoana()
    testPersoanaSetteri()

    testAdaugaPersoanaRepository()
    testModificaPersoanaRepository()
    testStergePersoanaRepository()

    #testAdaugaPersoanaService()
    #testModificaAngajatService()
    #testStergePersoanaService()