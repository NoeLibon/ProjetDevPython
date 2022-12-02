from bataille_navale import Bataille_navale
from ordi import Ordi
from joueur import Joueur
import sqlite3


class Mode_rafale(Bataille_navale):

    def __init__(self):
        start = input("Démarrez le jeu ? (oui ou non) -----> ")
        if start in ["oui", "Oui", "OUI"]:
            self.play()
        else:
            print("Une prochaine fois peut-être...")

    def play(self):
        nom_joueur1 = input("Quel est le nom du joueur ? -----> ")
        j1 = Joueur(nom_joueur1)
        j1.placement_flotte()
        j1.apercu_ocean()
        self.clear_screen()

        nom_joueur2 = input("\n\nJoueur 2, quel est votre nom ? -----> ")
        j2 = Joueur(nom_joueur2)
        j2.placement_flotte()
        j2.apercu_ocean()
        self.clear_screen()

        drapeau = True
        while drapeau is True:
            j1.tir_rafalej1(j2)
            if self.flotte_coule(j2) is True:
                self.message_victorieux(j1, j2)

                sqlite_file = (r"C:\Users\32498\sqlite3\data.db")
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

                j2.tir_rafalej2(j1)
                if self.flotte_coule(j1) is True:
                    self.message_victorieux(j2, j1)

                    sqlite_file = (r"C:\Users\32498\sqlite3\data.db")
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
