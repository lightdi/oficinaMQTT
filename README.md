# oficinaMQTT


Criando a imagem docker
docker build -t meu-mosquitto .

Executando o container

docker run -d \
  --name mosquitto \
  -p 1883:1883 \
  meu-mosquitto

# oficinaMQTT

## Criando a imagem Docker

```sh
docker build -t meu-mosquitto .


docker run -d \
  --name mosquitto \
  -p 1883:1883 \
  meu-mosquitto