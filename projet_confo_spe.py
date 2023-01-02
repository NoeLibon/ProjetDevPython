import random
import sys

from units.grille import Grille
from units.terrainennemi import TerrainEnnemi
from units.bateau import Bateau
from ui.graphique import UserInterface
import os
from units.erreur import InvalidInputNum
from units.erreur import InvalidInputOri
from units.erreur import InvalidPostion
from units.erreur import InvalidCooCiblee


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

    def placement_Porte_Avion(self):

        """PRE : parcours et prend éléments d'indice 0 à 2 du tableau donné en paramètre lors de la création de
        l'objet joueur. Les deux premiers éléments sont des int compris entre 0 et 9
        et le troisième est un string entre v ou h.

        POST : Un Porte-Avion (tableau de 5 coordonnées) est ajouté dans le tableau flotte
         affiche en console la position du bateau sur la grille.
        Permet le placement des bateaux si les méthodes de placement renvoient TRUE. (Si la case existe)
        Si un problème de positionnement survient, l'utilisateur verra son Porte-Avion placé avec des coo aléatoires.

        RAISE : ValueError si aucune données n'est introduite
        InvalidInputNum si les données introduites sont trop grandes ou trop petites
        InvalidInputOri si l'orientation donnée n'est pas comprise dans ["v", "V", "h", "H"]
        InvalidPosition si deux bateaux occupent la même case ou si le bateau dépasse de la grille
        Les erreurs sont directement attrapés et un message adéquat est donné au stderr"""

        global ori_PA, abs_PA, oor_PA
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_PA = int(self.tab[0])
                    oor_PA = int(self.tab[1])
                    if not 0 <= abs_PA <= 9 or not 0 <= oor_PA <= 9:
                        raise InvalidInputNum

                except InvalidInputNum:
                    sys.stderr.write("abs ou coo hors norme")
                    self.count5 += 1

                try:
                    ori_PA = self.tab[2]
                    if ori_PA not in ["v", "V", "h", "H"]:
                        raise InvalidInputOri

                except InvalidInputOri:
                    sys.stderr.write("orientation incorrect")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count5 += 1
                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                sys.stderr.write("Entrez un numéro...\n")
                self.count5 += 1

    def placement_Croiseur(self):

        """PRE : parcours et prend les éléments d'indice 3 à 5 du tableau donné en paramètre lors de la création de
        l'objet joueur. Les éléments 4 et 5 sont des int compris entre 0 et 9
        et le sixième est un string entre v ou h.

        POST : Un Croiseur (tableau de 4 coordonnées) est ajouté dans le tableau flotte
        affiche en console la position du bateau sur la grille.
        Permet le placement des bateaux si les méthodes de placement renvoient TRUE. (Si la case existe)
        Si un problème de positionnement survient, l'utilisateur verra son Croiseur  placé avec des coo aléatoires.

        RAISE : ValueError si aucune données n'est introduite
        InvalidInputNum si les données introduites sont trop grandes ou trop petites
        InvalidInputOri si l'orientation donnée n'est pas comprise dans ["v", "V", "h", "H"]
        InvalidPosition si deux bateaux occupent la même case ou si le bateau dépasse de la grille
        Les erreurs sont directement attrapés et un message adéquat est donné au stderr"""

        global ori_Cr, abs_Cr, oor_Cr
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Cr = int(self.tab[3])
                    oor_Cr = int(self.tab[4])
                    while not 0 <= abs_Cr <= 9 or not 0 <= oor_Cr <= 9:
                        raise InvalidInputNum

                except InvalidInputNum:
                    sys.stderr.write("abs ou coo hors norme")
                    self.count4 += 1

                try:
                    ori_Cr = self.tab[5]
                    if ori_Cr not in ["v", "V", "h", "H"]:
                        raise InvalidInputOri

                except InvalidInputOri:
                    sys.stderr.write("orientation incorrect")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count4 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                sys.stderr.write("Entrez un numéro...\n")
                self.count4 += 1

    def placement_Contre_Torpilleur(self):

        """PRE : parcours et prend les éléments d'indice 6 à 8 du tableau donné en paramètre lors de la création de
        l'objet joueur. Les éléments 6 et 7 sont des int compris entre 0 et 9
        et l'élément 8 est un string entre v ou h.

        POST : Un Contre-Torpilleur (tableau de 3 coordonnées) est ajouté dans le tableau flotte
        affiche en console la position du bateau sur la grille.
        Permet le placement des bateaux si les méthodes de placement renvoient TRUE. (Si la case existe)
        Si un problème de positionnement survient, l'utilisateur verra son Porte-Avion placé avec des coo aléatoires.

        RAISE : ValueError si aucune données n'est introduite
        InvalidInputNum si les données introduites sont trop grandes ou trop petites
        InvalidInputOri si l'orientation donnée n'est pas comprise dans ["v", "V", "h", "H"]
        InvalidPosition si deux bateaux occupent la même case ou si le bateau dépasse de la grille
        Les erreurs sont directement attrapés et un message adéquat est donné au stderr"""

        global ori_Ct, abs_Ct, oor_Ct
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Ct = int(self.tab[6])
                    oor_Ct = int(self.tab[7])
                    while not 0 <= abs_Cr <= 9 or not 0 <= oor_Cr <= 9:
                        raise InvalidInputNum

                except InvalidInputNum:
                    sys.stderr.write("abs ou coo hors norme")
                    self.count3 += 1

                try:
                    ori_Ct = self.tab[8]
                    if ori_Ct not in ["v", "V", "h", "H"]:
                        raise InvalidInputOri

                except InvalidInputOri:
                    sys.stderr.write("orientation incorrect")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count3 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                sys.stderr.write("Entrez un numéro...\n")
                self.count3 += 1

    def placement_Sous_Marin(self):

        """PRE : parcours et prend les éléments d'indice 9 à 11 du tableau donné en paramètre lors de la création de
        l'objet joueur. Les éléments 9 et 10 sont des int compris entre 0 et 9
        et l'élément 11 est un string entre v ou h.

        POST : Un Sous-Marin (tableau de 2 coordonnées) est ajouté dans le tableau flotte
        affiche en console la position du bateau sur la grille.
        Permet le placement des bateaux si les méthodes de placement renvoient TRUE. (Si la case existe)
        Si un problème de positionnement survient, l'utilisateur verra son Porte-Avion placé avec des coo aléatoires.

        RAISE : ValueError si aucune données n'est introduite
        InvalidInputNum si les données introduites sont trop grandes ou trop petites
        InvalidInputOri si l'orientation donnée n'est pas comprise dans ["v", "V", "h", "H"]
        InvalidPosition si deux bateaux occupent la même case ou si le bateau dépasse de la grille
        Les erreurs sont directement attrapés et un message adéquat est donné au stderr"""

        global ori_Sm, abs_Sm, oor_Sm
        drapeau = True
        while drapeau:
            try:
                try:
                    abs_Sm = int(self.tab[9])
                    oor_Sm = int(self.tab[10])
                    while not 0 <= abs_Sm <= 9 or not 0 <= oor_Sm <= 9:
                        raise InvalidInputNum

                except InvalidInputNum:
                    sys.stderr.write("abs ou coo hors norme")
                    self.count2 += 1

                try:
                    ori_Sm = self.tab[11]
                    if ori_Sm not in ["v", "V", "h", "H"]:
                        raise InvalidInputOri

                except InvalidInputOri:
                    sys.stderr.write("orientation incorrect")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
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
                            raise InvalidPostion
                except InvalidPostion:
                    sys.stderr.write("deux bateaux occupent la même case ou dépassent de la grille")
                    self.count2 += 1

                os.system('cls')
                self.apercu_ocean()

            except ValueError:
                sys.stderr.write("Entrez un numéro...\n")
                self.count2 += 1

    def coup_enregistre(self, ligne, col):

        """PRE : une ligne et une colonne en paramètre pour une coordonée.
        POST : si la coo correspont à celle d'un bateau, l'enlève du tableau de coordonnées.
        Si bateau n'a plus de coo, le retire de la flotte."""

        for bateau in self.flotte:
            if (ligne, col) in bateau.coo:
                bateau.coo.remove((ligne, col))
                if bateau.verif_etat():
                    self.flotte.remove(bateau)

    def tir(self, cible, tableau):

        """PRE : l'id de la personne à cibler(l'ordi (o) ou j1 ou j2) puis deux valeurs d'un tableau donné en paramètre
        pour determiner case à cibler. Si coordonnées déja ciblées ou inexistantes, répete le tir.

        POST : si un bateau adverse est touché, change la valeur de la case du tableau de tableau en X, O si raté
        Permet le tir si les méthodes de vérification renvoient TRUE. (case existe)

        Raise : ValueError si aucune donnée n'est introduite
        InvalidCooCiblee si le joueur vise en dehors de la grille ou si il tire deux fois au même endroit
        InvalidCooCiblee si autre chose qu'un int entre 0 et 9 est donné. (exclu string, float, negatif et boolean)"""

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
                                raise InvalidCooCiblee
                            else:
                                self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"
                                self.emplacements['o'].append((ligne, col))
                        except InvalidCooCiblee:
                            sys.stderr.write("Coordonnées déjà ciblées....Regardez votre carte!")

                else:
                    raise InvalidCooCiblee
            except InvalidCooCiblee:
                sys.stderr.write("Ne visez pas la Lune, entrez des coordonnées valides...")

        except ValueError:
            sys.stderr.write("Vous devez entrer des coordonnées....\n")
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

        ui.lancer()

    def recuperer_nom_ennemi(self, nom):
        self.nom_ennemi = nom