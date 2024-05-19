# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)


# Librairies
from network  import WLAN, STA_IF
from time     import sleep
from config   import *


# Fonction : recherche de routeurs proche
def scan():
    print()
    available = station.scan()
    print("routeurs visibles proches")
    if len(available) == 0 :
        print("None")
    else :
        for i in available :
            print("  - ", i)

    
# Fonction : Comportement si connecté
def connected() :
    if station.isconnected() == True:
        print("Connexion etablie")
        print("  - ", hostname, *station.ifconfig())
        return True
    return False


# Fonction : déconnexion
def disconnect():
    if connected() :
        station.disconnect()
    station.active(False)


# Fonction : connexion
def connect(routeurs=WIFI_ROUTEURS):
    # Activation du WiFi
    station.active(True)
    print()
    
    # Si déjà connecté
    if connected():
        return True
    
    # Si non encore connecté
    for k, v in routeurs.items():
        ip0  = '0.0.0.0'
        ssid = k
        mdp  = v[0]
        
        # Initialisation des paramètres de connexion
        try :
            station.ifconfig("dhcp")
            if len(v) == 5 :
                ip, subnet, gateway, dns = v[1:5]
                if ip != ip0 :
                    station.ifconfig((ip[i], subnet[i], gateway[i], dns[i]))
        
        # Si erreur, une connexion est surement déjà établie
        except :
            if connected():
                return True
        
        # Connexion et attente
        print("Connexion a", ssid, "...", end="")
        station.connect(ssid, mdp)
        for i in range(10):
            sleep(1) # élément bloquant
            print(".", end="")
            
            # Si connexion établie
            if connected() :
                return True
            
    # Si aucune connexion n'est établie
    print("Connexion impossible")


########### Partie a modifier ########### 
station  = WLAN(STA_IF)    # Création de l'objet "Station Wi-Fi"
hostname = 'esp32-' + ESP32_ID[8:]

if WIFI_CONNECT :
    station.active(True)  # Activation du WiFi
    station.config(dhcp_hostname = hostname)
    scan()                # Scan des routeurs proches
    connect()             # Connexion aux routeurs indiqués dans "routeurs"
    if REPL_CONNECT :
        import webrepl
        webrepl.start()
else :
    disconnect()          # Deconnexion