import paho.mqtt.client as paho
import time


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect('broker.mqttdashboard.com', 1883)
client.loop_start()

while True:
    publish_message = input('[Topico/Subtopico] [Mensagem]')
    if publish_message == '0':
        break

    if (len(publish_message.split(' ', 1)) == 2):
        split = publish_message.split(' ', 1)
        (rc, mid) = client.publish(split[0], split[1], qos=1)
        time.sleep(2)
    else:
        print('Formato inválido! Tente novamente.')