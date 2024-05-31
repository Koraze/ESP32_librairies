# Cette librairie ne renvoie le résultat de la fonction à surveiller
# que si elle est différente.

from tools.dt import DT

class Watch():
    def __init__(self, callback, payload, dt=100):
        self.__callback = callback
        self.__payload  = payload
        self.__dt       = DT(dt)
        self.__last     = None
        self.__new      = False
        
    def update(self):
        if self.__dt.remaining() <= 0 :
            if not self.__new :
                now = self.__callback()
                if now != self.__last :
                    self.__last = now
                    self.__new  = True
                    
    def get_new_value(self):
        if self.__new :
            self.__new = False
            return self.__payload % self.__last
        return None
            

# Fonctions tests - Exemples d'usage
def exemple(pin) :
    from machine  import Pin
    button_a = Pin(pin, Pin.IN)

    # La fonction a surveiller est 'button_a.value'
    watch_pin = Watch(button_a.value, "bouton %d")
    while True:
        watch_pin.update()                  # mise à jour
        message = watch_pin.get_new_value() # renvoi résultat si différent
        if message :
            print(message)


# Exemple d'utilisation
# Un bouton poussoir sur la broche 39 (modifiable) est nécessaire ici
if __name__ == '__main__':
    exemple(pin = 39)   # cliquez sur le bouton connecté à la broche 39
