from units.joueur import Joueur
import os


class BatailleNavale:

    def __init__(self):
        start = input("Démarrez le jeu ? (oui ou non) -----> ")
        if start in ["oui", "Oui", "OUI"]:
            self.play_pvp()
        else:
            print("Une prochaine fois peut-être...")

    def play_pvp(self):
        nom_joueur = input("Joueur 1, quel est votre nom ? -----> ")
        j1 = Joueur(nom_joueur)
        nom_joueur2 = input("\n\nJoueur 2, quel est votre nom ? -----> ")
        j2 = Joueur(nom_joueur2)
        j1.recuperer_nom_ennemi(nom=nom_joueur2)
        j2.recuperer_nom_ennemi(nom=nom_joueur)

        print(j1.nom)
        j1.placement_flotte()
        self.clear_screen()

        print(j2.nom)
        j2.placement_flotte()
        self.clear_screen()

        drapeau = True
        while drapeau is True:
            j1.tir(j2)
            if self.flotte_coule(j2) is True:
                self.message_victorieux(j1, j2)
                drapeau = False
            else:
                self.clear_screen()

                j2.tir(j1)
                if self.flotte_coule(j1) is True:
                    self.message_victorieux(j2, j1)
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
