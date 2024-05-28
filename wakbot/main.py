import lib
import time

def contar_hasta(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)



if __name__ == "__main__":
    contar_hasta(5)
    lib.recorrido_herb_camp()
