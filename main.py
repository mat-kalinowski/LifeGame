import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from ipywidgets import interact


def nowa_plansza(H, W, pola=None):
    if H > 0 and W > 0 and H % 1 == 0 and W % 1 == 0:
        plansza = np.zeros((H, W), dtype=float)

        if pola:
            for pair in pola:
                if pair[0] < H and pair[1] < W:
                    plansza[pair[0], pair[1]] = 1
        else:
            print('blad')
            return None

        return plansza


def sasiedzi(plansza, i, j):
    point = plansza[i, j]
    plansza = plansza[max(0, i-1):i+2, max(0, j-1): j+2]
    s_num = np.count_nonzero(plansza, None)

    if point > 0:
        s_num = max(0, s_num - 1)

    return s_num


def krok(plansza):
    obecna_plansza = deepcopy(plansza)

    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            neigh_num = sasiedzi(plansza, i, j)

            if neigh_num == 3 and plansza[i, j] == 0:
                obecna_plansza[i, j] = 1
            elif neigh_num < 2 and plansza[i, j] > 0:
                obecna_plansza[i, j] = 0
            elif neigh_num > 3 and plansza[i, j] > 0:
                obecna_plansza[i, j] = 0
            elif plansza[i, j] > 0:
                obecna_plansza[i, j] /= 2

    return obecna_plansza


def symulacja(plansza, n=100):
    lista = [deepcopy(plansza)]
    for i in range(n):
        lista.append(krok(lista[-1]))

    return lista


szybowiec = nowa_plansza(50, 50, [(25, 30), (25, 31), (25, 32), (26, 30), (27, 31)])
leci = symulacja(szybowiec, 100)


@interact(n=(0, 100))
def animuj(n=0):
    plt.matshow(leci[n])

