import random
import threading
from time import sleep
from loja import Loja
from CD import CD

lojas = [Loja(i) for i in range(20)]

run = 1

#Loop de débito das lojas que fará todo o sistema rodar
while run:

    for loja in lojas:
        yn = random.randint(0, 1)
        sleeptime = random.randint(1, 20) / 100

        if (yn):
            loja.loop()
            sleep(sleeptime)
