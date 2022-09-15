import random
import paho.mqtt.client as paho

class Loja:
    def __init__(self, id):
        self.client = paho.Client()
        self.pid = [0] * 210  #[0] = A(100 unidades) [1] = B(60 unidades) [2] = C(20 unidades)...
        self.msg = ' '
        self.id_loja = id

        self.fill_products()
        self.connect()

    #Inicializa o centro de distribuição cheio
    def fill_products(self):
        for i in range(210):
            if (i % 3 == 0):
                self.pid[i] = 100
            elif (i % 3 == 1):
                self.pid[i] = 60
            else:
                self.pid[i] = 20

    #Conecta no broker e inscreve nos canais das 20 lojas
    def connect(self):
        self.client.connect('broker.mqttdashboard.com', 1883)

    #Retorna o sinal dependendo da quantidade de produtos disponiveis
    def control_products(self, pid):
        tipo = pid % 3

        if (tipo == 0):
            if (self.pid[pid] >= 50):
                return 'green'
            if (self.pid[pid] >= 25):
                return 'yellow'
            return 'red'
        elif (tipo == 1):
            if (self.pid[pid] >= 30):
                return 'green'
            if (self.pid[pid] >= 15):
                return 'yellow'
            return 'red'
        else:
            if (self.pid[pid] >= 10):
                return 'green'
            if (self.pid[pid] >= 5):
                return 'yellow'
            return 'red'

    #Faz a requisição de um produto para a fabrica
    def refill(self, pid):
        if (pid % 3 == 0):
            quant = 100
        elif (pid % 3 == 1):
            quant = 60
        else:
            quant = 20

        self.client.publish(f'loja/[{self.id_loja}]', pid)
        self.pid[pid] += quant


    #Loop
    def loop(self):
        produto = random.randint(0, 209)
        quant = random. randint(1, 19)

        print(f'{quant} unidades adquirida do produto {produto} na loja {self.id_loja}')
        self.pid[produto] -= quant

        sinal = self.control_products(produto)
        print(f'Sinal produto {produto}: {sinal}')
        if (sinal == 'red'):
            print(f'Loja {self.id_loja} requisitando reabastecimento de produto {produto}')
            self.refill(produto)
    
            
        
