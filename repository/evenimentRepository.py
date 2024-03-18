from repository.repository import Repository
#from repository.RepositoryException import *


class EvenimentRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_eveniment_dupa_nume(self, nume_eveniment):
        for i in range(0, len(self._lista)):
            eveniment_curenta = self._lista[i]
            if eveniment_curenta.get_nume() == nume_eveniment:
                return eveniment_curenta
        return -1