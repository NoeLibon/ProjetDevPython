from modes.bataille_navale import BatailleNavale
from units.ordi import Ordi
from units.joueur import Joueur


class ModeSolo(BatailleNavale):

    def __init__(self):
        start = input("Démarrez le jeu ? (oui ou non) -----> ")
        if start in ["oui", "Oui", "OUI"]:
            self.play_solo()
        else:
            print("Une prochaine fois peut-être...")

    def play_solo(self):
        nom_joueur = input("Quel est le nom du joueur ? -----> ")
        j = Joueur(nom_joueur)
        o = Ordi()
        j.recuperer_nom_ennemi(o.nom)

        print(j.nom)
        j.placement_flotte()
        self.clear_screen()

        print("L'ordinateur positionne ses navires...")
        o.ordi_flotte()
        self.clear_screen()

        drapeau = True
        while drapeau is True:
            j.tir(o)
            if self.flotte_coule(o) is True:
                self.message_victorieux(j, o)
                sqlite_file = (r"db.sqlite")
                connection = sqlite3.connect(sqlite_file)
                cursor = connection.cursor()
                sql = "CREATE TABLE IF NOT EXISTS " + "db" + "(id integer PRIMARY KEY AUTOINCREMENT, result char not null)"
                cursor.execute(sql)
                sql = "INSERT INTO " + "db" + "(result) VALUES (\"self.message_victorieux(j, o)\")"
                cursor.execute(sql)

                connection.commit()
                cursor.close()
                drapeau = False
            else:
                self.clear_screen()

                o.frappe_ennemie(j)
                if self.flotte_coule(j) is True:
                    self.message_victorieux(o, j)
                    sqlite_file = (r"db.sqlite")
                    connection = sqlite3.connect(sqlite_file)
                    cursor = connection.cursor()
                    sql = "CREATE TABLE IF NOT EXISTS " + "db" + "(id integer PRIMARY KEY AUTOINCREMENT, result char not null)"
                    cursor.execute(sql)
                    sql = "INSERT INTO " + "db" + "(result) VALUES (\"self.message_victorieux(o, j)\")"
                    cursor.execute(sql)

                connection.commit()
                cursor.close()
                    drapeau = False
                else:
                    self.clear_screen()
        print("\nMerci d'avoir joué!")
