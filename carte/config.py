from machine import unique_id
ESP32_ID = ''.join('{:02x}'.format(b) for b in unique_id())

# Liste des routeurs sur lesquels se connecter
WIFI_ROUTEURS = {
    'SSID_1' : ['motdepasse', 'ip', 'masque', 'passerelle', 'dns'],
    'SSID_2' : ['motdepasse'],
}
WIFI_CONNECT = True
REPL_CONNECT = False

# Parametres broker MQTT
MQTT_HOST = None
MQTT_PORT = None
MQTT_USER = None
MQTT_PW   = None
