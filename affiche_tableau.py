def affiche_tableau(t, n):
    for i in range(n):
        print(f"{i}:{t[i]}")

tab = [1, 2, 3, 4]
taille = 4
affiche_tableau(tab, taille)