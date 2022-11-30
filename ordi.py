from joueur import Joueur
from bateau import Bateau
import random


class Ordi(Joueur):

    def __init__(self):
        super().__init__(self)
        self.name = "Ordinateur"

    def ordi_flotte(self):
        positions = ["v", "h"]

        for bateau, taille in self.navires.items():

            drapeau = True
            while drapeau:
                ligne = random.randint(0, 9)
                col = random.randint(0, 9)
                orientation = random.choice(positions)

                if orientation == "v":
                    if self.grille.placement_valide_ligne(ligne, col, taille):
                        self.grille.placement_bateau_ligne(ligne, col, taille)
                        bateau = Bateau(bateau, taille)
                        bateau.positionnement_vertical(ligne, col)
                        self.flotte.append(bateau)
                        drapeau = False

                    else:
                        ligne = ligne + 2

                elif orientation == "h":
                    if self.grille.placement_valide_col(ligne, col, taille):
                        self.grille.placement_bateau_col(ligne, col, taille)
                        bateau = Bateau(bateau, taille)
                        bateau.positionnement_horizontal(ligne, col)
                        self.flotte.append(bateau)
                        drapeau = False

                    else:
                        col = col + 2

                else:
                    continue

    def frappe_ennemie(self, cible):
        ligne = random.randint(0, 9)
        col = random.randint(0, 9)

        if self.terrain_ennemi.terrain_ennemi[ligne][col] == ".":
            input("...Ciblage en cours....%s, %s" % (ligne, col))

            if cible.grille.grille[ligne][col] == "B":
                print("Touché!")
                cible.grille.grille[ligne][col] = "X"
                cible.coup_enregistre(ligne, col)
                self.terrain_ennemi.terrain_ennemi[ligne][col] = "X"
                self.emplacements['x']['moi'].append((ligne, col))

            else:
                print("Raté....recalibrage du canon")
                self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"

        else:
            self.frappe_ennemie(cible)
