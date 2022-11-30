class TerrainEnnemi:

    def __init__(self, longueur=10, hauteur=10):
        self.terrain_ennemi = [["." for _ in range(longueur)] for _ in range(hauteur)]

    def __getitem__(self, case):
        ligne, col = case
        return self.terrain_ennemi[ligne][col]

    def __setitem__(self, case, value):
        ligne, col = case
        self.terrain_ennemi[ligne][col] = value

    def apercu_terrain_ennemi(self):
        for ligne in self.terrain_ennemi:
            print(" ".join(ligne))
