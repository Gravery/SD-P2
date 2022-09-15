import random
import threading
from time import sleep
from loja import Loja
from CD import CD

lojas = [Loja(i) for i in range(20)]

run = 1
'''cd = CD()

threading1 = threading.Thread(target=cd.listen)
threading1.daemon = True
threading1.start()'''

while run:
    for loja in lojas:
        yn = random.randint(0,1)
        sleeptime = random.randint(1,20) / 10
        if (yn):
            loja.loop()
            sleep(sleeptime)
