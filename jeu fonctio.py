from bataille_navale import Bataille_navale
from bataille_navale_solo import Mode_solo


def jeu():
    print("\n\n*********************")
    print("Bienvenue! Vous vous préparez à jouer à la bataille navale")
    print("**********************\n")

    print("\n 1) Multijoueur")
    print("\n 2) 1 joueur")

    drapeau = True

    while drapeau:
        try:
            mode = int(input("\n\nChoisissez votre mode de jeu en entrant en ligne de commande le numéro du mode souhaité ----> "))
            if mode == 1:
                drapeau = False
                Bataille_navale()
            elif mode == 2:
                drapeau = False
                Mode_solo()
            else:
                continue
        except ValueError:
            print("Veillez choisir un chiffre renseigné à l'écran")


jeu()