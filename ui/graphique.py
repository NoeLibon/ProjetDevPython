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
        for x in range(10):
            for y in range(10):
                case = Frame(self.terrain_ennemi, bg='#03224c')
                case.grid(row=x, column=y)
                case_par_defaut = Label(case, text='.', font=('Courrier', 15), bg='#03224c', fg='white', width=4,
                                        height=2)
                case_par_defaut.pack(expand=YES)

    def initialiser_mon_terrain(self):
        for x in range(10):
            for y in range(10):
                case = Frame(self.mon_terrain, bg='#03224c')
                case.grid(row=x, column=y)
                case_par_defaut = Label(case, text='~', font=('Courrier', 15), bg='#03224c', fg='white', width=4,
                                        height=2)
                case_par_defaut.pack(expand=YES)

    def identifier_bateau_col(self, ligne, col, taille):
        for _ in range(taille):
            case = Frame(self.mon_terrain, bg='#03224c')
            case.grid(row=ligne, column=col)
            case_bateau = Label(case, text='B', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
            case_bateau.pack(expand=YES)
            col = col + 1

    def identifier_bateau_ligne(self, ligne, col, taille):
        for _ in range(taille):
            case = Frame(self.mon_terrain, bg='#03224c')
            case.grid(row=ligne, column=col)
            case_bateau = Label(case, text='B', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
            case_bateau.pack(expand=YES)
            ligne = ligne + 1

    def identifier_case_manquee(self, ligne, col):
        case = Frame(self.terrain_ennemi, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='O', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def identifier_case_touchee_chez_ennemi(self, ligne, col):
        case = Frame(self.terrain_ennemi, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='X', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def identifier_case_touchee_chez_moi(self, ligne, col):
        case = Frame(self.mon_terrain, bg='#03224c')
        case.grid(row=ligne, column=col)
        case_touchee = Label(case, text='X', font=('Courrier', 15), bg='#03224c', fg='white', width=4, height=2)
        case_touchee.pack(expand=YES)

    def lancer(self):
        self.fenetre.mainloop()
