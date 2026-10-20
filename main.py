# 20.10.2026
# Laura Happo
# Tehtävä 7.1
# Kolmepistekäännös

# 20.10.2026
# Laura Happo
# Tehtävä 7.1
# FoCarin tarvittavat funktiot

# Tehojen / nopeuden määrittely - luvut alle 24000 eivät pyöritä moottoreita
# 25% = 16383
# 50% = 32767
# 75% = 49150
# 100% = 65535

# Suuntien määritys
# 0 taaksepäin
# 1 eteenpäin

# Kirjastojen lisäys ja määritykset
from machine import Pin, PWM
from time import sleep

# Moottori A (oikea)  
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)
# Moottori B (vasen)
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Luodaan led olio
led = Pin("LED", Pin.OUT)

# Määritä focarissa tarvittavat funktiot
def kaannyVasen(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def kaannyOikea(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def eteenpain(suuntaO, suuntaV, nopeus, aika):
    # Eteenpäin
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def taaksepain(suuntaO, suuntaV, nopeus, aika):
    # Pakita
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def kaannyPaikalla(suuntaO, suuntaV, nopeus, aika):
    # Käännös
    m1.value(suuntaO)
    m2.value(suuntaV)
    # Liike
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

def stop(nopeus, aika):
    sleep(aika)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    # Odota yksi sekunti moottoreiden pysähtymistä
    sleep(1)

def vilkutaLed(paalla, pois):
    # Vilkutetaan lediä halutusti
    while True:
        led.on()
        sleep(paalla)
        led.off()
        sleep(pois)

# Kolmepistekäännös
# Odota hetki ennen ajoa
sleep(10)

# Aja eteenpäin metri
eteenpain(1, 1, 32767, 4)
stop(0, 1)

# Käänny oikealle
kaannyOikea(0, 1, 32767, 3)
stop(0, 1)

# Peruuta
taaksepain(0, 0, 32767, 4)
stop(0, 1)

# Käänny oikealle
kaannyOikea(0, 1, 32767, 3)
stop(0, 1)

# Aja lähtöpisteeseen
eteenpain(1, 1, 32767, 4)
stop(0, 1)