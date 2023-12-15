"""
trie en place un tableau tab d'entiers dans l'ordre croissant. Pour cela, on parcout tab pour k de 1 à len(tab) - 1
A l'étape k: 
- tab[:k] est trié ;
- on insère tab[k] au bon indice pour qu'après insertion tab[:k+1] soit rangé dans l'ordre croissant ;
"""