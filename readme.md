
# Initialisation de votre carte

Installez le microgiciel micropython correspondant à votre carte dans cette dernière. Vous pouvez trouver des versions de MicroPython :
- Dans le dossier `firmware` de ce répertoire (pas forcément à jour)
- Dans le site officiel [micropython](https://micropython.org) 

  

# Connexion à votre borne WiFi

Une fois le microgiciel installé et la carte redémarrée :
1. Créez à la racine de votre carte les fichiers `boot.py` et `config.py`
2. Copiez-y le contenu des fichiers de même nom dans le dossier `carte`
3. Adaptez le contenu de `config.py` :
   - Renseignez dans `WIFI_ROUTEURS` les paramètres de votre borne WiFi
   - Remplacez `WIFI_CONNECT = False` par `WIFI_CONNECT = True`
4. Redémarrez la carte

  

# Librairies MicroPython

## Installation du client MQTT (basé sur les librairies de fizista)
```python
import mip
mip.install("github:Koraze/ESP32_librairies/mip/bridge_mqtt.json")
```

## Installation des modules i2c (basé sur le travail d'Adafruit)
Les modules actuelement adaptés sont :
- ina219
- max17048

```python
# Remplacez xxxx par le nom du module (exemple ina219)
import mip
mip.install("github:Koraze/ESP32_librairies/mip/module_xxxx.json")
```
