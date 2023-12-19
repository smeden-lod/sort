import random
import time

def trandom(l):
    listrandom=[]
    for _ in range(l):
        listrandom.append(random.randint(0, 10000))
    return listrandom

def imini(t: list[int]) -> int:
    """
    t est un tableau non vide d'entiers
    renvoie le premier indice de la valeur minimale dans t
    >>> assert imini([37, 5, 18, 5, 41]) == 1
    >>> assert imini([3, 5, 18, 15]) == 0
    >>> assert imini([3, 5, 18, 15, 1]) == 4
    """
    m = t[0]
    ind_m = 0
    i = 0
    for i, x in enumerate(t):
        if x < m:
            m = x
            ind_m = i
    return ind_m

def swap(t: list[int], i: int, j: int) -> None:
    """
    t est un tableau non vide d'entiers avec au moins deux valeurs
    i, j des int tels que 0 <= i < len(t) et 0 <= j <len(t)
    si on note t' la valeur de t après exécution
    t'[i] = t[j]
    t'[j] = t[i]
    >>> ta = [7, 1, 3]
    >>> swap(ta, 0, 1)
    >>> assert  ta == [1, 7, 3]
    """
    temp = t[i]
    t[i] = t[j]
    t[j] = temp

def tri_selection(t):
    """
    >>> t = [7, 42, 87, 123, 2, 7, 5]
    >>> tri_selection(t)
    >>> t = [2, 5, 7, 7, 42, 87, 123]
    """
    for k in range(len(t)): # répéter autant de fois que la taille de t
        i = imini(t[k:]) # renvoie l'indice du min dans t[k:]
        swap(t, k, i + k) # l'indice de cette val dans t est i + k (décalage)
    return t

time1=time.time()
print(tri_selection(trandom(10000)))
time2=time.time()
tempexec = time2 - time1
print(round(tempexec, 3), "secondes")

tempexec_str = "%.8f\n" % (tempexec)
f = open("log.txt", "a")
f.write(tempexec_str)
f.close()