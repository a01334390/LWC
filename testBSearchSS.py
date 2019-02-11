from estructuras import *

def ucs(g, s, m):  
    frontera = ColaPriorizada()
    frontera.put(0, s)
    anteriores = {}
    anteriores[s] = None
    acumulado = {}
    acumulado[s] = 0

    while not frontera.esVacia():
        actual = frontera.get()
        if actual == m:
            break
        for vecino in g.vecinos(actual):
            costo = acumulado[actual] + g.costo(actual, vecino)
            if vecino not in acumulado or costo < acumulado[vecino]:
                acumulado[vecino] = costo
                frontera.put(costo, vecino)
                anteriores[vecino] = actual
    return acumulado, acumulado[actual]


def main():
    g = Grafo()
    with open('espana.txt') as f:
        for l in f:
            (c1, c2, c) = l.split(',')
            g.aAristaPeso(c1, c2, c)
    print(ucs(g, 'Coruna', 'Vigo'))

if __name__ == '__main__':
    main()
