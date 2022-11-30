class Grille:

    def __init__(self, longueur=10, hauteur=10):
        self.grille = [["~" for _ in range(longueur)] for _ in range(hauteur)]

    def __getitem__(self, case):
        ligne, col = case
        return self.grille[ligne][col]

    def __setitem__(self, case, value):
        ligne, col = case
        self.grille[ligne][col] = value

    def apercu_grille(self):
        for ligne in self.grille:
            print(" ".join(ligne))

    def verif_col(self, ligne):
        try:
            if self.grille[ligne]:
                # self.terrain_ennemi[ligne]
                return True
        except IndexError:
            return False

    def verif_ligne(self, col):
        try:
            if self.grille[0][col]:
                return True
        except IndexError:
            return False

    def placement_valide_col(self, ligne, col, taille):

        valide_coo = []

        for i in range(taille):

            if self.verif_col(col) and self.verif_ligne(ligne):
                if self.grille[ligne][col] == "~":
                    valide_coo.append((ligne, col))
                    col = col + 1
                else:
                    col = col + 1
            else:
                return False

        if taille == len(valide_coo):
            return True
        else:
            return False

    def placement_valide_ligne(self, ligne, col, taille):

        valide_coo = []

        for i in range(taille):

            if self.verif_ligne(ligne) and self.verif_col(col):
                if self.grille[ligne][col] == "~":
                    valide_coo.append((ligne, col))
                    ligne = ligne + 1
                else:
                    ligne = ligne + 1
            else:
                return False

        if taille == len(valide_coo):
            return True
        else:
            return False

    def placement_bateau_col(self, ligne, col, taille):
        for i in range(taille):
            self.grille[ligne][col] = "B"
            col = col + 1

    def placement_bateau_ligne(self, ligne, col, taille):
        for i in range(taille):
            self.grille[ligne][col] = "B"
            ligne = ligne + 1
