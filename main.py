from repository.evenimentFileRepository import EvenimentFileRepository
from repository.inscriereFileRepository import InscriereFileRepository
from repository.persoanaFileRepository import persoanaFileRepository
from repository.repository import Repository
from service.persoanaService import PersoanaService
from service.persoanaEvenimentService import PersoanaEvenimentService
from service.evenimentService import EvenimentService
from teste.testAll import testAll
from ui.consola import Consola

def main():
    #testAll()

    persoanaRepository = persoanaFileRepository("persoane")
    evenimentRepository = EvenimentFileRepository("evenimente")
    persoanaEvenimentRepository = InscriereFileRepository("inscrieri", persoanaRepository, evenimentRepository)

    persoanaService = PersoanaService(persoanaRepository, persoanaEvenimentRepository)
    evenimentService = EvenimentService(evenimentRepository, persoanaEvenimentRepository)
    persoanaEvenimentService = PersoanaEvenimentService(persoanaEvenimentRepository, persoanaRepository, evenimentRepository)

    consola = Consola(persoanaService, evenimentService, persoanaEvenimentService)

    """
    persoana1 = Persoana(1, "Ana", "Aleea Godeanu")
    persoana2 = Persoana(2, "Ioana", "Aurel Vlaicu")
    persoana3 = Persoana(3, "Andrei", "Ploiesti")

    persoanaRepository.adauga(persoana1)
    persoanaRepository.adauga(persoana2)
    persoanaRepository.adauga(persoana3)
    """

    consola.meniu()

main()