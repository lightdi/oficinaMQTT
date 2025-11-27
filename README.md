# oficinaMQTT

## Criando a imagem Docker

```sh
docker build -t imagem-mosquitto .


docker run -d \
  --name mosquitto \
  -p 1883:1883 \
  imagem-mosquitto