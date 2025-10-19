FROM eclipse-mosquitto:openssl

# 2. Copia o arquivo de configuração
# Copia o 'mosquitto.conf' local para o diretório de configuração
# exato que o Mosquitto usa dentro do contêiner.
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

EXPOSE 1883
