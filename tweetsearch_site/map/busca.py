
from buscador import buscador

def main():
    print("Iniciando busca")
    with open('buscador/key.txt', 'r') as keyfile:
        key = keyfile.read()
        if(key[-1] == '\n'):
            key = key[:-1]
        print("Buscando pela palavra: %s" % (key))
        buscador.buscaTwts.iniciaBusca(key, 10)

if __name__ == "__main__":
    main()
