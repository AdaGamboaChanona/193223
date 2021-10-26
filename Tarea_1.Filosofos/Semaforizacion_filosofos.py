import threading
import time

tenedorArray = [1,1,1,1,1]

class TenedorFilosofo(threading.Thread):
    
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  (self.filosofosNum + 1) % 5
        
        
    def hilosFilosofos(self):
            
        print(f'Filosofo iniciando {self.filosofosNum}')
        time.sleep(2)
        
        
        self.tenedores[self.filosofosNum].acquire()
        print(f'Filosofo {self.filosofosNum} recoge tenedor del lado izquierdo')
        time.sleep(2)
        
        
        self.tenedores[self.datoTemporal].acquire()
        print(f'Filosofo {self.filosofosNum} recoge tenedor del lado derecho')
        time.sleep(2)
        
        print(f'Filosofo {self.filosofosNum} deja tenedor izquierdo')
        self.tenedores[self.datoTemporal].release()
        time.sleep(0.5)
        
        print(f'Filosofo {self.filosofosNum} deja tenedor derecho')
        self.tenedores[self.filosofosNum].release()
        time.sleep(0.5)
            
            
    def run(self):
        self.hilosFilosofos()


if __name__ == '__main__':
    for i in range(0,5):
        tenedorArray[i] = threading.BoundedSemaphore(2)

    for i in range(0,5):
        total = TenedorFilosofo(tenedorArray, i)
        total.start()
        time.sleep(3)