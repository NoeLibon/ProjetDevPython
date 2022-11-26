class Terrain_ennemi:

    def __init__(self, longueur=10, hauteur=10):
        self.terrain_ennemi = [["." for i in range(longueur)] for i in range(hauteur)]

    def __getitem__(self, case):
        ligne, col = case
        return self.terrain_ennemi[ligne][col]

    def __setitem__(self, case, value):
        ligne, col = case
        self.terrain_ennemi[ligne][col] = value

    def aprecu_terrain_ennemi(self):
        for ligne in self.terrain_ennemi:
            print(" ".join(ligne))
