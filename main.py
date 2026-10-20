# 20.10.2026
# Laura Happo
# Tehtävä 7.1
# Kolmepistekäännös

# Tarvittavat funktiot
from focar import eteenpain
from focar import taaksepain
from focar import stop
from focar import kaannyOikea

# Kolmepistekäännös
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