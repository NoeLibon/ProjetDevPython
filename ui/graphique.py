from tkinter import *


class UserInterface:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('Bataille navale')
        self.fenetre.config(background='#03224c')

        self.titre = Label(self.fenetre, text='Bataille navale', font=('Courrier', 40), bg='#03224c', fg='white')
        self.titre.pack()

        self.grilles = Frame(self.fenetre, background='#03224c')
        self.grilles.pack(expand=YES)

        self.ennemi = Frame(self.grilles)
        self.ennemi.grid(row=0, column=0)

        self.joueur = Frame(self.grilles)
        self.joueur.grid(row=0, column=1)

        self.terrain_ennemi = Frame(self.grilles, borderwidth=1)
        self.terrain_ennemi.grid(row=1, column=0)

        self.mon_terrain = Frame(self.grilles, borderwidth=1)
        self.mon_terrain.grid(row=1, column=1)

    def afficher_nom_ennemi(self, nom):
        nom_ennemi = Label(self.ennemi, text=nom, font=('Courrier', 25), bg='#03224c', fg='white')
        nom_ennemi.pack(expand=YES)

    def afficher_mon_nom(self, nom):
        mon_nom = Label(self.joueur, text=nom, font=('Courrier', 25), bg='#03224c', fg='white')
        mon_nom.pack(expand=YES)

    def initialiser_terrain_ennemi(self):
        """
        Crée une succession de cases afin de créer une grille pour le terrain ennemi

        PRE : self est un objet de type UserInterface
        POST : crée une grille de taille 10x10 cases contenant "."
        """
        for x in range(10):
            for y in range(10):
                case = Frame(self.terrain_ennemi, bg='#03224c')
                case.grid(row=x, column=y)
                case_par_defaut = Label(case, text='.', font=('Courrier', 15), bg='#03224c', fg='white', width=4,
                                        height=2)
                case_par_defaut.pack(expand=YES)

    def initialiser_mon_terrain(self):
        """
        Crée une succession de cases afin de créer une grille pour le terrain du joueur

        PRE : self est un objet de type UserInterface
        POST : crée une grille de taille 10x10 cases contenant "~"
        """
        for x in range(10):
            for y in range(10):
                case = Frame(self.mon_terrain, bg='#03224c')
                case.grid(row=x, column=y)
                case_par_defaut = Label(case, text='~', font=('Courrier', 15), bg='#03224c', fg='white', width=4,
                                        height=2)
                case_par_defaut.pack(expand=YES)

    def identifier_bateau_col(self, ligne, col, taille):
        """
        Alloue des cases pour le placement d'un bateau horizontal

        PRE : self est un objet de type UserInterface, ligne et col sont des entiers nuls ou positifs, taille est un
        entier positif non nul
        POST : remplace une case contenant "~" par une case contenant "B" aux coordonnées ligne
        et col donnés en paramètre + remplace celles à droite aussi juqu'à atteindre la taille donnée en paramètre
        """
        for _ in range(taille):
            case = Frame(self.mon_terrain, bg='#03224c')
            case.grid(row=ligne, column=col)
            case_bateau = Label(case, text='B', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
            case_bateau.pack(expand=YES)
            col = col + 1

    def identifier_bateau_ligne(self, ligne, col, taille):
        """
        Alloue des cases pour le placement d'un bateau vertical

        PRE : self est un objet de type UserInterface, ligne et col sont des entiers nuls ou positifs, taille est un
        entier positif non nul
        POST : remplace une case contenant "~" par une case contenant "B" aux coordonnées ligne
        et col donnés en paramètre + remplace celles en-dessous aussi juqu'à atteindre la taille donnée en paramètre
        """
        for _ in range(taille):
            case = Frame(self.mon_terrain, bg='#03224c')
            case.grid(row=ligne, column=col)
            case_bateau = Label(case, text='B', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
            case_bateau.pack(expand=YES)
            ligne = ligne + 1

    def identifier_case_manquee(self, ligne, col):
        """
        Crée une case à l'endroit où un tir a été effectué et manqué chez l'ennemi

        PRE : self est un objet de type UserInterface, ligne et col sont des entiers nuls ou positifs
        POST : remplace une case contenant "." par une case contenant "O" aux coordonnées ligne et col donnés
        en paramètres
        """
        case = Frame(self.terrain_ennemi, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='O', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def identifier_case_touchee_chez_ennemi(self, ligne, col):
        """
        Crée une case à l'endroit où un tir a été effectué et touché chez l'ennemi

        PRE : self est un objet de type UserInterface, ligne et col sont des entiers nuls ou positifs
        POST : remplace une case contenant "." par une case contenant "X" aux coordonnées ligne et col donnés
        en paramètres
        """
        case = Frame(self.terrain_ennemi, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='X', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def identifier_case_touchee_chez_moi(self, ligne, col):
        """
        Crée une case à l'endroit où un tir a été effectué et manqué sur le terrain du joueur

        PRE : self est un objet de type UserInterface, ligne et col sont des entiers nuls ou positifs
        POST : remplace une case contenant "~" par une case contenant "X" aux coordonnées ligne et col donnés
        en paramètres
        """
        case = Frame(self.mon_terrain, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='X', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def lancer(self):
        self.fenetre.mainloop()
