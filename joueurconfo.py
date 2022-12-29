import random
from units.grille import Grille
from units.terrainennemi import TerrainEnnemi
from units.bateau import Bateau
from ui.graphique import UserInterface
import os
from units.erreur import invalidInputNum
from units.erreur import invalidInputOri
from units.erreur import invalidPostion
from units.erreur import invalidCooCiblee


class Joueur:
    navires = {"Porte-avions": 5, "Croiseur": 4, "Contre-torpilleur": 3, "Sous-marin": 2}

    def __init__(self, nom, tab):
        self.nom = nom
        self.nom_ennemi = ''
        self.grille = Grille()
        self.terrain_ennemi = TerrainEnnemi()
        self.flotte = []
        self.tab = tab
        self.emplacements = {'v': [], 'h': [], 'o': [], 'x': {'ennemi': [], 'moi': []}}
        self.compteurj1 = 0
        self.compteurj2 = 0
        self.count5 = 0
        self.count4 = 0
        self.count3 = 0
        self.count2 = 0

    def apercu_ocean(self):
        self.terrain_ennemi.apercu_terrain_ennemi()
        self.grille.apercu_grille()

    def placement5(self):
        global ori_PA, abs_PA, oor_PA
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_PA = int(self.tab[0])
                    oor_PA = int(self.tab[1])
                    if not 0 <= abs_PA <= 9 or not 0 <= oor_PA <= 9:
                        raise invalidInputNum

                except invalidInputNum:
                    print("abs ou coo hors norme")
                    self.count5 += 1

                try:
                    ori_PA = self.tab[2]
                    if ori_PA not in ["v", "V", "h", "H"]:
                        raise invalidInputOri

                except invalidInputOri:
                    print("orientation incorrect")
                    ori_PA = "v"

                if self.count5 >= 1:
                    abs_PA = random.randint(0, 9)
                    oor_PA = random.randint(0, 9)

                try:
                    if ori_PA in ["v", "V"]:
                        if self.grille.placement_valide_ligne(abs_PA, oor_PA, 5):
                            self.grille.placement_bateau_ligne(abs_PA, oor_PA, 5)
                            bateau = Bateau("Porte-avions", 5)
                            bateau.positionnement_vertical(abs_PA, oor_PA)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count5 += 1

                try:
                    if ori_PA in ["h", "H"]:
                        if self.grille.placement_valide_col(abs_PA, oor_PA, 5):
                            self.grille.placement_bateau_col(abs_PA, oor_PA, 5)
                            bateau = Bateau("Porte-avions", 5)
                            bateau.positionnement_horizontal(abs_PA, oor_PA)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count5 += 1
                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                print("Entrez un numéro...\n")
                self.count5 += 1

    def placement4(self):
        global ori_Cr, abs_Cr, oor_Cr
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Cr = int(self.tab[3])
                    oor_Cr = int(self.tab[4])
                    while not 0 <= abs_Cr <= 9 or not 0 <= oor_Cr <= 9:
                        raise invalidInputNum

                except invalidInputNum:
                    print("abs ou coo hors norme")
                    self.count4 += 1

                try:
                    ori_Cr = self.tab[5]
                    if ori_Cr not in ["v", "V", "h", "H"]:
                        raise invalidInputOri

                except invalidInputOri:
                    print("orientation incorrect")
                    ori_Cr = "v"

                if self.count4 >= 1:
                    abs_Cr = random.randint(0, 9)
                    oor_Cr = random.randint(0, 9)

                try:
                    if ori_Cr in ["v", "V"]:
                        if self.grille.placement_valide_ligne(abs_Cr, oor_Cr, 4):
                            self.grille.placement_bateau_ligne(abs_Cr, oor_Cr, 4)
                            bateau = Bateau("Croiseur", 4)
                            bateau.positionnement_vertical(abs_Cr, oor_Cr)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count4 += 1

                try:
                    if ori_Cr in ["h", "H"]:
                        if self.grille.placement_valide_col(abs_Cr, oor_Cr, 4):
                            self.grille.placement_bateau_col(abs_Cr, oor_Cr, 4)
                            bateau = Bateau("Croiseur", 4)
                            bateau.positionnement_horizontal(abs_Cr, oor_Cr)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count4 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                print("Entrez un numéro...\n")
                self.count4 += 1

    def placement3(self):
        global ori_Ct, abs_Ct, oor_Ct
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Ct = int(self.tab[6])
                    oor_Ct = int(self.tab[7])
                    while not 0 <= abs_Cr <= 9 or not 0 <= oor_Cr <= 9:
                        raise invalidInputNum

                except invalidInputNum:
                    print("abs ou coo hors norme")
                    self.count3 += 1

                try:
                    ori_Ct = self.tab[8]
                    if ori_Ct not in ["v", "V", "h", "H"]:
                        raise invalidInputOri

                except invalidInputOri:
                    print("orientation incorrect")
                    ori_Ct = "v"

                if self.count3 >= 1:
                    abs_Ct = random.randint(0, 9)
                    oor_Ct = random.randint(0, 9)

                try:
                    if ori_Ct in ["v", "V"]:
                        if self.grille.placement_valide_ligne(abs_Ct, oor_Ct, 3):
                            self.grille.placement_bateau_ligne(abs_Ct, oor_Ct, 3)
                            bateau = Bateau("Contre-torpilleur", 3)
                            bateau.positionnement_vertical(abs_Ct, oor_Ct)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count3 += 1

                try:
                    if ori_Ct in ["h", "H"]:
                        if self.grille.placement_valide_col(abs_Ct, oor_Ct, 3):
                            self.grille.placement_bateau_col(abs_Ct, oor_Ct, 3)
                            bateau = Bateau("Contre-torpilleur", 3)
                            bateau.positionnement_horizontal(abs_Ct, oor_Ct)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count3 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                print("Entrez un numéro...\n")
                self.count3 += 1

    def placement2(self):
        global ori_Sm, abs_Sm, oor_Sm
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Sm = int(self.tab[9])
                    oor_Sm = int(self.tab[10])
                    while not 0 <= abs_Sm <= 9 or not 0 <= oor_Sm <= 9:
                        raise invalidInputNum

                except invalidInputNum:
                    print("abs ou coo hors norme")
                    self.count2 += 1

                try:
                    ori_Sm = self.tab[11]
                    if ori_Sm not in ["v", "V", "h", "H"]:
                        raise invalidInputOri

                except invalidInputOri:
                    print("orientation incorrect")
                    ori_Sm = "v"

                if self.count2 >= 1:
                    abs_Sm = random.randint(0, 9)
                    oor_Sm = random.randint(0, 9)

                try:
                    if ori_Sm in ["v", "V"]:
                        if self.grille.placement_valide_ligne(abs_Sm, oor_Sm, 2):
                            self.grille.placement_bateau_ligne(abs_Sm, oor_Sm, 2)
                            bateau = Bateau("Sous-marin", 2)
                            bateau.positionnement_vertical(abs_Sm, oor_Sm)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count2 += 1

                try:
                    if ori_Cr in ["h", "H"]:
                        if self.grille.placement_valide_col(abs_Sm, oor_Sm, 2):
                            self.grille.placement_bateau_col(abs_Sm, oor_Sm, 2)
                            bateau = Bateau("Sous-marin", 2)
                            bateau.positionnement_horizontal(abs_Sm, oor_Sm)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            raise invalidPostion
                except invalidPostion:
                    print("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count2 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                print("Entrez un numéro...\n")
                self.count2 += 1

    def coup_enregistre(self, ligne, col):
        for bateau in self.flotte:
            if (ligne, col) in bateau.coo:
                bateau.coo.remove((ligne, col))
                if bateau.verif_etat():
                    self.flotte.remove(bateau)

    def tir(self, cible, tableau):
        self.apercu_ocean()
        try:
            ligne = int(tableau[0])
            col = int(tableau[1])
            try:
                if self.grille.verif_ligne(ligne) and self.grille.verif_col(col):
                    if cible.grille[ligne, col] == "B":
                        cible.grille[ligne, col] = "X"
                        cible.coup_enregistre(ligne, col)
                        self.terrain_ennemi[ligne, col] = "X"
                        self.emplacements['x']['ennemi'].append((ligne, col))
                        cible.emplacements['x']['moi'].append((ligne, col))

                    else:
                        try:
                            if self.terrain_ennemi.terrain_ennemi[ligne][col] == "O" or \
                                    self.terrain_ennemi.terrain_ennemi[ligne][col] == "X":
                                raise invalidCooCiblee
                            else:
                                self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"
                                self.emplacements['o'].append((ligne, col))
                        except invalidCooCiblee:
                            print("Coordonnées déjà ciblées....Regardez votre carte!")

                else:
                    raise invalidCooCiblee
            except invalidCooCiblee:
                print("Ne visez pas la Lune, entrez des coordonnées valides...")


        except ValueError:
            print("Vous devez entrer des coordonnées....\n")
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
