from units.grille import Grille
from units.terrainennemi import TerrainEnnemi
from units.bateau import Bateau
from ui.graphique import UserInterface
import os


class Joueur:
    navires = {"Porte-avions": 5, "Croiseur": 4, "Contre-torpilleur": 3, "Sous-marin": 2}

    def __init__(self, nom):
        self.grille = Grille()
        self.terrain_ennemi = TerrainEnnemi()
        self.nom = nom
        self.nom_ennemi = ''
        self.flotte = []
        self.emplacements = {'v': [], 'h': [], 'o': [], 'x': {'ennemi': [], 'moi': []}}

    def placement_flotte(self):
        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        self.apercu_ocean()
        for bateau, taille in self.navires.items():

            drapeau = True
            while drapeau:
                try:
                    print("Veuillez placer votre %s" % bateau)
                    ligne = int(input("Choisissez une ligne -----> "))
                    col = int(input("Choisissez une colonne -----> "))
                    orientation = str(input("Verical ou horizontal "
                                            "(tapez v pour vertical ou h pour horizontal -----> "))

                    if orientation in ["v", "V"]:
                        if self.grille.placement_valide_ligne(ligne, col, taille):
                            self.grille.placement_bateau_ligne(ligne, col, taille)
                            self.emplacements['v'].append((ligne, col, taille))
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_vertical(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper la même case, réessayez!")

                    elif orientation in ["h", "H"]:
                        if self.grille.placement_valide_col(ligne, col, taille):
                            self.grille.placement_bateau_col(ligne, col, taille)
                            self.emplacements['h'].append((ligne, col, taille))
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_horizontal(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper la même case, réessayez!")

                    else:
                        continue

                    input()
                    os.system('cls')
                    self.apercu_ocean()

                except ValueError:
                    print("Entrez un numéro...\n")

    def apercu_ocean(self):
        self.terrain_ennemi.apercu_terrain_ennemi()
        print("|                 |")
        self.grille.apercu_grille()
        self.afficher_interface_graphique()

    def coup_enregistre(self, ligne, col):
        for bateau in self.flotte:
            if (ligne, col) in bateau.coo:
                bateau.coo.remove((ligne, col))
                if bateau.verif_etat():
                    self.flotte.remove(bateau)
                    print("le %s de %s a été coulé!" % (bateau.modele, self.nom))

    def tir(self, cible):
        self.apercu_ocean()
        try:
            print("\n%s Entrez les coordonnées à cibler..." % self.nom)
            ligne = int(input("Choisissez une ligne -----> "))
            col = int(input("Choisissez une colonne -----> "))

            if self.grille.verif_ligne(ligne) and self.grille.verif_col(col):
                if cible.grille[ligne, col] == "B":
                    print("Touché!!!")
                    cible.grille[ligne, col] = "X"
                    cible.coup_enregistre(ligne, col)
                    self.terrain_ennemi[ligne, col] = "X"
                    self.emplacements['x']['ennemi'].append((ligne, col))
                    cible.emplacements['x']['moi'].append((ligne, col))

                else:
                    if self.terrain_ennemi.terrain_ennemi[ligne][col] == "O":
                        print("Coordonnées déjà ciblées....Regardez votre carte!")
                        self.tir(cible)
                    else:
                        print("Manqué...")
                        self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"
                        self.emplacements['o'].append((ligne, col))

            else:
                print("Ne visez pas la Lune, entrez des coordonnées valides...")
                self.tir(cible)

        except ValueError:
            print("Vous devez entrer des coordonnées....\n")
            self.tir(cible)
        input()
        os.system('cls')
        self.apercu_ocean()

    def afficher_interface_graphique(self):
        ui = UserInterface()
        ui.afficher_nom_ennemi(nom=self.nom_ennemi)
        ui.afficher_mon_nom(nom=self.nom)
        ui.initialiser_terrain_ennemi()
        ui.initialiser_mon_terrain()

        if self.emplacements['v']:
            for emplacement in self.emplacements['v']:
                ui.identifier_bateau_ligne(ligne=emplacement[0], col=emplacement[1], taille=emplacement[2])
        if self.emplacements['h']:
            for emplacement in self.emplacements['h']:
                ui.identifier_bateau_col(ligne=emplacement[0], col=emplacement[1], taille=emplacement[2])
        if self.emplacements['o']:
            for emplacement in self.emplacements['o']:
                ui.identifier_case_manquee(ligne=emplacement[0], col=emplacement[1])
        if self.emplacements['x']['ennemi']:
            for emplacement in self.emplacements['x']['ennemi']:
                ui.identifier_case_touchee_chez_ennemi(ligne=emplacement[0], col=emplacement[1])
        if self.emplacements['x']['moi']:
            for emplacement in self.emplacements['x']['moi']:
                ui.identifier_case_touchee_chez_moi(ligne=emplacement[0], col=emplacement[1])

        print(self.emplacements)

        ui.lancer()

    def recuperer_nom_ennemi(self, nom):
        self.nom_ennemi = nom
