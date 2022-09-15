import paho.mqtt.client as paho
import sys


class Fabrica:
    def __init__(self, identificacao, produtos):
        self.identificacao = identificacao
        self.produtos = produtos
        self.client = paho.Client()

    def subscribe(self):
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.connect('broker.mqttdashboard.com', 1883)
        self.client.subscribe(f'fabrica/[{self.identificacao}]', qos=1)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: " +str(mid)+ " " + str(granted_qos))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        print("Sinal de refill recebido")
