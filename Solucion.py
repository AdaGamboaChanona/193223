import time
import threading
import logging
import queue
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def agarrar_tenedores(num_filosofo):
    return f'Al filosofo {num_filosofo} le toca tomar los 2 tenedores'
        
def comer(num_filosofo):
    return f'El filosofo {num_filosofo} empieza a comer'
        
def terminar_comida(num_filosofo):
    return f'El filosofo {num_filosofo} termina su comida y ahora'

def mostrar_resultados(cola):
    while not cola.empty():
        num_filosofo = cola.get()
        lock.acquire()
        logging.info(agarrar_tenedores(num_filosofo))
        logging.info(comer(num_filosofo))
        logging.info(terminar_comida(num_filosofo))
        lock.release()
        cola.task_done()
        time.sleep(0.2)
        
if __name__=='__main__':
    queue=queue.Queue()
    filosofos=int(input('Ingrese el numero de filosofos que quieran comer: '))
    for i in range(filosofos):
        queue.put(i+1)
    logging.info('Los filosofos ya se sentaron en la mesa')

    with ThreadPoolExecutor(max_workers=3) as executor:
        for _ in range(executor._max_workers):
            executor.submit(mostrar_resultados,queue)
            
            