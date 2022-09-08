from logging import exception
import paho.mqtt.client as paho
import threading
import sys

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " +str(mid)+ " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))    

def background():
    while True:
        if input() == '1':
            new_sub = input('Tópico para inscrever [TOPICO/#]:')
            client.subscribe(new_sub, qos=1)
            print(f'Inscrito com sucesso em {new_sub}!')

        if input() == '2':
            new_connect = input('[ENDEREÇO] [PORT]')
            split = new_connect.split(' ', 1)
            if len(split) != 2:
                print('Entrada inválida, conecte novamente')
            else:
                try:
                    client.connect(split[0], int(split[1]))
                    print(f'Conectado a {split[0]} na porta {split[1]}')
                except:
                    print('Falha na conexão! Timed out.')


        if input() == '0':
            print('Desconectando e terminando aplicação...')
            client.disconnect()
            sys.exit()

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883)
client.subscribe('teste/#', qos=1)

threading1 = threading.Thread(target=background)
threading1.daemon = True
threading1.start()

client.loop_forever()