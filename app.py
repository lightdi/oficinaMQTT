from flask import Flask, render_template, jsonify, request, redirect, url_for
import threading
import paho.mqtt.client as mqtt

# ====== CONFIGURAÇÕES DO BROKER MQTT ======
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "chat/oficina"



mensagens = []


estado = "Desconectado"

client = mqtt.Client()

# ====== CALLBACKS MQTT ======
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT")
        client.subscribe(MQTT_TOPIC)
        estado = "Conectado"
    else:
        estado = "Desconectado"
        print(f"❌ Falha na conexão (código {rc})")

def on_message(client, userdata, msg):
    
    try:
        mensagem = msg.payload.decode()
        print(f"📩 Mensagem recebida no tópico {msg.topic}: {mensagem}")
        mensagens.append(mensagem)
    except Exception as e:
        print(f"❌ Erro ao processar mensagem: {e}")

# ====== THREAD DO MQTT ======
def mqtt_thread():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

#====== FLASK APP ======
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", estado=estado, mensagens=mensagens)

@app.route("/dados")
def get_dados():
    return jsonify(mensagens)

@app.route("/enviar", methods=["POST"])
def enviar_mensagem():
    mensagem = request.form.get('message')

    try:
        # Usa o client global para publicar a mensagem
        client.publish(MQTT_TOPIC, mensagem)
        print(f"🚀 Mensagem publicada no tópico {MQTT_BROKER}: {mensagem}")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"❌ Erro ao publicar mensagem: {e}")
        return redirect(url_for('index'))
      
    

# ====== MAIN ======
if __name__ == "__main__":
    t = threading.Thread(target=mqtt_thread)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=5000, debug=True)