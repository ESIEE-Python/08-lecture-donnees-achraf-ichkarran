#### Imports et définition des variables globales
"""L'objectif est d'écrire une fonction de lecture des données contenues 
dans un fichier et diverses fonctions manipulant des listes numériques."""
import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,mode='r',encoding='utf8') as f:
        s=f.readlines()
        l=list(s)
    f.close()

    return l

def get_list_k(data, k):
    """Args:
        data (list):le contenue du fichier (filename)
        k (int):numero de la kieme ligne

    Returns:
        list: kieme ligne
    """
    return data[k]

def get_first(l):
    """Args:
        l(list)

    Returns:
        int:premier element de la liste
    """
    return l[0]

def get_last(l):
    """Args:
        l(list)

    Returns:
        int:dernier element de la liste
    """
    return l[-1]

def get_max(l):
    """Args:
        l(list)

    Returns:
        int:plus grand element de la liste
    """
    return max(l)

def get_min(l):
    """Args:
        l(list)

    Returns:
        int:plus petit element de la liste
    """
    return min(l)

def get_sum(l):
    """Args:
        l(list)

    Returns:
        int:somme des elements elements de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
if __name__ == "__main__":
    main()
