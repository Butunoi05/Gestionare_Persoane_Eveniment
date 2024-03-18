from repository.repository import Repository


class PersoanaRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_persoana_by_id(self, id):
        for i in range(0, len(self._lista)):
            persoana_curent = self._lista[i]
            if persoana_curent.get_id() == id:
                return persoana_curent
        return -1