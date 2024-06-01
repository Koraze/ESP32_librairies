
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
