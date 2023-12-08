from fonctions import *


if __name__ == '__main__':
    exo = int(input("Saisir le numéro de l'exercice: "))
    if exo == 1:
        x =carre(5)
        print("le carre de {0} est {1} ".format(5,x))
    elif exo == 2:
        L = [1, 2, 3]
        add_list(L,6)
        print(L)
    elif exo == 3:
        afficher_val(0, 10)

    elif exo == 4:
        deb = int(input("Saisir deb : "))
        fin = int(input("Saisir fin : "))
        while fin < deb:
            fin = int(input("fin doit etre superieur à deb : "))

        pas = int(input("Saisir votre pas : "))
        bornes(deb, fin, pas)

    else:
        print("Ce numéro d'exercice n'existe pas")

