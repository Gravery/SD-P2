import paho.mqtt.client as paho

class CD:
    def __init__(self):
        self.client = paho.Client()
        self.pid = [0] * 210  #[0] = A(100 unidades) [1] = B(60 unidades) [2] = C(20 unidades)...
        self.fabricas = [] #3 produtos cada sendo A, B, C
        self.lojas = []   #20 lojas com todos os 210 produtos
        self.msg = [' '] * 2

        self.fill_products()
        self.sub_and_connect()

    #Inicializa o centro de distribuição cheio
    def fill_products(self):
        for i in range(210):
            if (i % 3 == 0):
                self.pid[i] = 100 * 5
            elif (i % 3 == 1):
                self.pid[i] = 60 * 5
            else:
                self.pid[i] = 20 * 5

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
            if (self.pid[pid] >= 50 * 5):
                return 'green'
            if (self.pid[pid] >= 25 * 5):
                return 'yellow'
            return 'red'
        elif (tipo == 1):
            if (self.pid[pid] >= 30 * 5):
                return 'green'
            if (self.pid[pid] >= 15 * 5):
                return 'yellow'
            return 'red'
        else:
            if (self.pid[pid] >= 10 * 5):
                return 'green'
            if (self.pid[pid] >= 5 * 5):
                return 'yellow'
            return 'red'

    #Faz a requisição de um produto para a fabrica
    def refill(self, pid):
        id_fab = int(pid / 3)
        if (pid % 3 == 0):
            quant = (100 * 5)
        elif (pid % 3 == 1):
            quant = (60 * 5)
        else:
            quant = (20 * 5)

        print(f'Requisitando reposição de Produto {pid}')
        self.client.publish(f'fabrica/[{id_fab}]', pid)
        self.pid[pid] += quant

    #Função de recebimento de mensagem mqtt
    def on_message(self, client, userdata, msg):
            print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
            self.msg[0] = msg.topic.split('/')[1]
            self.msg[1] = msg.payload

            loja = self.msg[0]
            pid = int(self.msg[1])

            print(f'Loja {loja} teve produto {pid} reestocado')

            self.restock_store(pid)
            sinal = self.control_products(pid)
            print(f'Sinal do produto {pid} no CD: {sinal}')
            if (sinal == 'red'):
                self.refill(pid)

    #Ouve mensagens dos canais inscritos
    def listen(self):
            self.client.on_message = self.on_message
            self.client.loop_forever()
            
        
