class Bateau:

    def __init__(self, modele, taille):
        self.modele = modele
        self.taille = taille
        self.coo = []

    def positionnement_vertical(self, ligne, col):
        for i in range(self.taille):
            self.coo.append((ligne, col))
            ligne = ligne + 1

    def positionnement_horizontal(self, ligne, col):
        for i in range(self.taille):
            self.coo.append((ligne, col))
            col = col + 1

    def verif_etat(self):
        if not self.coo:
            return True
        else:
            return False
