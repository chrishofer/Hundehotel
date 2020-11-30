from typing import List


class Hund:
    """ Hund stellt einen Gast für unser Hundehotel dar

        langbeschreibung
        über mehrere
        zeilen
    """

    def __init__(self, name: str, alter: int, allergie_liste: List[str]):
        """ Initialisiert ein Hundeobjekt

        Parameters
        ----------
        name : str
            Hundename
        alter : int
            Hundealter
        allergie_liste : list of str
            Allergische Zutaten in einer Liste
        """
        self.name = name  #: str: Hundename
        self.alter = alter  #: int: Alter des Hundes
        self.allergie_liste = allergie_liste  #: list of str: Nahrungsmittel auf die Hund allergisch reagiert

    def __str__(self):
        """ Liefert String Repräsentation eines Hundeobjektes

        Returns
        -------
            String Darstellung des Hundes
        """
        return f'Hund(Name:{self.name} Alter:{self.alter} Allergien:{self.allergie_liste} )'

    def ist_allergisch(self, allergen: str) -> bool:
        """ Überprüft ob Hund allergisch auf ein Lebensmittel ist

        Parameters
        ----------
        allergen : str
            Zu überprüfendes Allergen
        Returns
        -------
            True falls Hund darauf allergisch ist; sonst False
        """
        return allergen in self.allergie_liste


# Schneller Testcode den ich nur hier zum rum probieren verwenden
if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 10, ['semmel', 'extrawurst'])
    print(rex)
    print(rex.ist_allergisch("semmel"))
    print(rex.ist_allergisch("brot"))
