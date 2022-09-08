import paho.mqtt.client as paho

from subscriber import on_message

class CD:
    def __init__(self):
        self.client = paho.Client()
        self.pid = []  #[0] = A(100 unidades) [1] = B(60 unidades) [2] = C(20 unidades)...
        self.fabricas = [] #3 produtos cada sendo A, B, C
        self.lojas = []   #20 lojas com todos os 210 produtos
        self.msg = ' '

        self.fill_products()
        self.sub_and_connect()

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
    def sub_and_connect(self):
        self.client.connect('broker.mqttdashboard.com', 1883)

        for i in range(20):
            self.client.subscribe(f'loja/[{i}]', qos=1)

    #Função que subtrai do CD a qunatidade a ser enviada para loja
    def restock_store(self, pid):
        if (pid % 3 == 0):
            self.pid[pid] -= 100
        elif (pid % 3 == 1):
            self.pid[pid] -= 60
        else:
            self.pid[pid] -= 20

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
        id_fab = int(pid / 3)
        if (pid % 3 == 0):
            quant = 100
        elif (pid % 3 == 1):
            quant = 60
        else:
            quant = 20

        self.client.publish(f'fabrica/[{id_fab}]', pid)
        self.pid[pid] += quant

    #Função de recebimento de mensagem mqtt
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        self.msg[0] = msg.topic.split('/')[1]
        self.msg[1] = msg.payload

    #Ouve mensagens dos canais inscritos
    def listen(self):
        self.client.on_message = on_message

        loja = self.msg[0]
        pid = int(self.msg[1])

        self.restock_store(pid)
        sinal = self.control_products(pid)
        if (sinal == 'red'):
            self.refill(pid)
            
        
