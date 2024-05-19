from machine import unique_id
ESP32_ID = ''.join('{:02x}'.format(b) for b in unique_id())

# Liste des routeurs sur lesquels se connecter
WIFI_ROUTEURS = {
    'SSID_1' : ['motdepasse', 'ip', 'masque', 'passerelle', 'dns'],
    'SSID_2' : ['motdepasse'],
}
WIFI_CONNECT  = False
REPL_CONNECT  = False

# Parametres broker MQTT
ha_mqtt_port = 
ha_mqtt_name = 
ha_mqtt_user = 
ha_mqtt_pw   = 

def ha_mqtt_find_ip():
    import usocket
    ip = usocket.getaddrinfo('....local', 0)
    return ip[0][4][0]
