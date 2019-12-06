import os
from buscador import buscador

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + "/"
    print("Iniciando busca")
    with open(path + 'buscador/key.txt', 'r') as keyfile:
        key = keyfile.read()
        if(key[-1] == '\n'):
            key = key[:-1]
        print("Buscando pela palavra: %s" % (key))
        buscador.buscaTwts.iniciaBusca(key, 10, path)

if __name__ == "__main__":
    main()
