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
        cooPA = input("abs")
        cooPa2 = input("oor")
        oriPA = input("v h")
        self.placej1.extend((cooPA, cooPa2, oriPA))

        print("Veuillez placer votre Croiseur")
        cooCr = input("abs")
        cooCr2 = input("oor")
        oriCr = input("v h")
        self.placej1.extend((cooCr, cooCr2, oriCr))

        print("Veuillez placer votre Contre-torpilleurs")
        cooCt = input("abs")
        cooCt2 = input("oor")
        oriCt = input("v h")
        self.placej1.extend((cooCt, cooCt2, oriCt))

        print("Veuillez placer votre Sous-marin")
        cooSm = input("abs")
        cooSm2 = input("oor")
        oriSm = input("v h")
        self.placej1.extend((cooSm, cooSm2, oriSm))

        j1 = Joueur(nom_joueur, self.placej1)

        nom_joueur2 = input("\n\nJoueur 2, quel est votre nom ? -----> ")
        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        print("Veuillez placer votre Porte-avions")
        cooPAj2 = input("abs")
        cooPa2j2 = input("oor")
        oriPAj2 = input("v h")
        self.placej2.extend((cooPAj2, cooPa2j2, oriPAj2))

        print("Veuillez placer votre Croiseur")
        cooCrj2 = input("abs")
        cooCr2j2 = input("oor")
        oriCrj2 = input("v h")
        self.placej2.extend((cooCrj2, cooCr2j2, oriCrj2))

        print("Veuillez placer votre Contre-torpilleur")
        cooCtj2 = input("abs")
        cooCt2j2 = input("oor")
        oriCtj2 = input("v h")
        self.placej2.extend((cooCtj2, cooCt2j2, oriCtj2))

        print("Veuillez placer votre Sous-marin")
        cooSmj2 = input("abs")
        cooSm2j2 = input("oor")
        oriSmj2 = input("v h")
        self.placej2.extend((cooSmj2, cooSm2j2, oriSmj2))

        j2 = Joueur(nom_joueur2, self.placej2)
        j1.recuperer_nom_ennemi(nom=nom_joueur2)
        j2.recuperer_nom_ennemi(nom=nom_joueur)

        print(j1.nom)
        j1.placement5()
        os.system('cls')
        self.clear_screen()

        j1.placement4()
        os.system('cls')
        self.clear_screen()

        j1.placement3()
        os.system('cls')
        self.clear_screen()

        j1.placement2()
        os.system('cls')
        self.clear_screen()

        print(j2.nom)
        j2.placement5()
        os.system('cls')
        self.clear_screen()

        j2.placement4()
        os.system('cls')
        self.clear_screen()

        j2.placement3()
        os.system('cls')
        self.clear_screen()

        j2.placement2()
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


