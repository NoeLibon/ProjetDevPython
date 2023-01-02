from units.joueurconfo import Joueur
import os


class BatailleNavale:

    def __init__(self):
        self.placej1 = []
        self.placej2 = []
        self.tircooj1 = []
        self.tircooj2 = []
        start = input("Démarrez le jeu ? (oui ou non) -----> ")
        if start in ["oui", "Oui", "OUI"]:
            self.play_pvp()
        else:
            print("Une prochaine fois peut-être...")

    def play_pvp(self):
        nom_joueur = input("Joueur 1, quel est votre nom ? -----> ")
        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        print("Veuillez placer votre Porte-avions")
        coo_Porte_Avion = input("abs ----->")
        coo_Porte_Avion2 = input("oor ----->")
        ori_Porte_Avion = input("v ou h ---->")
        self.placej1.extend((coo_Porte_Avion, coo_Porte_Avion2, ori_Porte_Avion))

        print("Veuillez placer votre Croiseur")
        coo_Croiseur = input("abs ----->")
        coo_Croiseur2 = input("oor ----->")
        ori_Croiseur = input("v ou h ----->")
        self.placej1.extend((coo_Croiseur, coo_Croiseur2, ori_Croiseur))

        print("Veuillez placer votre Contre-torpilleur")
        coo_Contre_Torpilleur = input("abs ----->")
        coo_Contre_Torpilleur2 = input("oor ----->")
        ori_Contre_Torpilleur = input("v ou h ----->")
        self.placej1.extend((coo_Contre_Torpilleur, coo_Contre_Torpilleur2, ori_Contre_Torpilleur))

        print("Veuillez placer votre Sous-marin")
        coo_Sous_Marin = input("abs ----->")
        coo_Sous_Marin2 = input("oor ----->")
        ori_Sous_Marin = input("v h ----->")
        self.placej1.extend((coo_Sous_Marin, coo_Sous_Marin2, ori_Sous_Marin))

        j1 = Joueur(nom_joueur, self.placej1)

        nom_joueur2 = input("\n\nJoueur 2, quel est votre nom ? -----> ")
        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        print("Veuillez placer votre Porte-avions")
        coo_Porte_Avionj2 = input("abs ----->")
        coo_Porte_Avion2j2 = input("oor ----->")
        ori_Porte_Avionj2 = input("v ou h ---->")
        self.placej2.extend((coo_Porte_Avionj2, coo_Porte_Avion2j2, ori_Porte_Avionj2))

        print("Veuillez placer votre Croiseur")
        coo_Croiseurj2 = input("abs ----->")
        coo_Croiseur2j2 = input("oor ----->")
        ori_Croiseurj2 = input("v ou h ----->")
        self.placej2.extend((coo_Croiseurj2, coo_Croiseur2j2, ori_Croiseurj2))

        print("Veuillez placer votre Contre-torpilleur")
        coo_Contre_Torpilleur = input("abs ----->")
        coo_Contre_Torpilleur2 = input("oor ----->")
        ori_Contre_Torpilleur = input("v ou h ----->")
        self.placej2.extend((coo_Contre_Torpilleurj2, coo_Contre_Torpilleur2j2, ori_Contre_Torpilleurj2))

        print("Veuillez placer votre Sous-marin")
        coo_Sous_Marinj2 = input("abs ----->")
        coo_Sous_Marin2j2 = input("oor ----->")
        ori_Sous_Marinj2 = input("v h ----->")
        self.placej2.extend((coo_Sous_Marinj2, coo_Sous_Marin2j2, ori_Sous_Marinj2))

        j2 = Joueur(nom_joueur2, self.placej2)
        j1.recuperer_nom_ennemi(nom=nom_joueur2)
        j2.recuperer_nom_ennemi(nom=nom_joueur)

        print(j1.nom)
        j1.placement_Porte_Avion()
        os.system('cls')
        self.clear_screen()

        j1.placement_Croiseur()
        os.system('cls')
        self.clear_screen()

        j1.placement_Contre_Torpilleur()
        os.system('cls')
        self.clear_screen()

        j1.placement_Sous_Marin()
        os.system('cls')
        self.clear_screen()

        print(j2.nom)
        j2.placement_Porte_Avion()
        os.system('cls')
        self.clear_screen()

        j2.placement_Croiseur()
        os.system('cls')
        self.clear_screen()

        j2.placement_Contre_Torpilleur()
        os.system('cls')
        self.clear_screen()

        j2.placement_Sous_Marin()
        os.system('cls')
        self.clear_screen()

        drapeau = True
        while drapeau is True:
            print(j1.nom)
            tir1j1 = input("coo à cibler")
            tir2j1 = input("coo à cibler2")
            self.tircooj1.extend((tir1j1, tir2j1))
            j1.tir(j2, self.tircooj1)
            self.tircooj1.pop()
            self.tircooj1.pop()
            if self.flotte_coule(j2) is True:
                self.message_victorieux(j1, j2)

                sqlite_file = (r"db.sqlite")
                connection = sqlite3.connect(sqlite_file)
                cursor = connection.cursor()
                sql = "CREATE TABLE IF NOT EXISTS " + "db" + "(id integer PRIMARY KEY AUTOINCREMENT, result char not null)"
                cursor.execute(sql)
                sql = "INSERT INTO " + "db" + "(result) VALUES (\"self.message_victorieux(j1, j2)\")"
                cursor.execute(sql)

                connection.commit()
                cursor.close()
                drapeau = False
            else:
                self.clear_screen()

                print(j2.nom)
                tir1j2 = input("coo à cibler")
                tir2j2 = input("coo à cibler2")
                self.tircooj2.extend((tir1j2, tir2j2))
                j2.tir(j1, self.tircooj2)
                self.tircooj2.pop()
                self.tircooj2.pop()
                if self.flotte_coule(j1) is True:
                    self.message_victorieux(j2, j1)
                    sqlite_file = (r"db.sqlite")
                    connection = sqlite3.connect(sqlite_file)
                    cursor = connection.cursor()
                    sql = "CREATE TABLE IF NOT EXISTS " + "db" + "(id integer PRIMARY KEY AUTOINCREMENT, result char not null)"
                    cursor.execute(sql)
                    sql = "INSERT INTO " + "db" + "(result) VALUES (\"self.message_victorieux(j2, j1)\")"
                    cursor.execute(sql)

                    connection.commit()
                    cursor.close()
                    drapeau = False
                else:
                    self.clear_screen()
        print("\nMerci d'avoir joué!")

    @staticmethod
    def message_victorieux(gagnant, perdant):
        print("\n\n\n*****************************************")
        print("La flotte de %s a été coulée, %s a gagné!" % (perdant.nom, gagnant.nom))
        print("*****************************************")

    @staticmethod
    def clear_screen():
        os.system('cls')

    @staticmethod
    def flotte_coule(joueur):
        nbr_bateau = 0
        for grille_ligne in joueur.grille.grille:
            for case in grille_ligne:
                if case == "B":
                    nbr_bateau += 1
        if nbr_bateau == 0:
            return True
        else:
            return False


