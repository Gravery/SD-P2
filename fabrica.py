import paho.mqtt.client as paho
import sys


class Fabrica:
    def __init__(self, identificacao, produtos):
        self.identificacao = identificacao
        self.produtos = produtos
        self.client = paho.Client()
        self.client.connect('broker.mqttdashboard.com', 1883)

    #Realiza a subscribe da fábrica no canal de seu id
    def subscribe(self):
        self.client.subscribe(f'fabrica/[{self.identificacao}]', qos=1)
        print(f'Subscribe Fabrica {self.identificacao}')

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: " +str(mid)+ " " + str(granted_qos))

    #Ao receber sinal do CD faz o crédito de produtos
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        print("Sinal de refill recebido")
        print(f'Reabastecendo produto {str(msg.payload)} para o CD')

    #Loop para ouvir requisições de produtos do CD
    def listen(self):
        self.client.on_message = self.on_message
        self.client.loop(0.01)


    