from bataille_navale import BatailleNavale
from ordi import Ordi
from joueur import Joueur


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
        j.placement_flotte()
        self.clear_screen()

        o = Ordi()
        print("L'ordinateur positionne ses navires...")
        o.ordi_flotte()
        self.clear_screen()

        drapeau = True
        while drapeau is True:
            j.tir(o)
            if self.flotte_coule(o) is True:
                self.message_victorieux(j, o)
                drapeau = False
            else:
                self.clear_screen()

                o.frappe_ennemie(j)
                if self.flotte_coule(j) is True:
                    self.message_victorieux(o, j)
                    drapeau = False
                else:
                    self.clear_screen()
        print("\nMerci d'avoir joué!")
