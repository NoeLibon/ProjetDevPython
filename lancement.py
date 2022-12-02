from modes.bataille_navale import BatailleNavale
from modes.bataille_navale_solo import ModeSolo


def jeu():
    print("\n\n*********************")
    print("Bienvenue! Vous vous préparez à jouer à la bataille navale")
    print("**********************\n")

    print("\n 1) Multijoueur")
    print("\n 2) 1 joueur")
    print("\n 3) mode rafale")
    print("\n 4) score")
    print("\n 5) instructions")
    print("\n 6) Quitter le jeu")

    drapeau = True

    while drapeau:
        try:
            mode = int(input("\n\nChoisissez votre mode de jeu en entrant en ligne de commande le numéro du mode "
                             "souhaité ----> "))
            if mode == 1:
                drapeau = False
                BatailleNavale()
            elif mode == 2:
                drapeau = False
                ModeSolo()
                        elif mode == 3:
                drapeau = False
                Mode_rafale()
            elif mode == 4:
                drapeu = False
                Score()
            elif mode == 5:
                drapeau = False
                Aide()
            elif mode == 6:
                break
            else:
                continue
        except ValueError:
            print("Veillez choisir un chiffre renseigné à l'écran")

if __name__ == "__main__":
    jeu()
