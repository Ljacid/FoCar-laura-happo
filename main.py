# 20.10.2026
# Laura Happo
# Tehtävä 7.1
# Kolmepistekäännös

from focar import lisaaKirjastot
from focar import maaritaMoottorit
from focar import eteenpain
from focar import taaksepain
from focar import stop
from focar import kaannyOikea

# Lisää kirjastot ja määritä moottorit
lisaaKirjastot
maaritaMoottorit

# Aja eteenpäin metri
eteenpain(1, 1, 32767, 4)
stop(0, 1)

# Kolmepistekäännös
# Käänny oikealle ja aja eteenpäin
kaannyOikea(0, 1, 32767, 3)
eteenpain(1, 1, 32767, 4)
stop(0, 1)

# Käänny oikealle ja peruuta
kaannyOikea(0, 1, 32767, 3)
taaksepain(0, 0, 32767, 4)
stop(0, 1)

# Käänny oikealle ja aja eteenpäin
kaannyOikea(0, 1, 32767, 3)
eteenpain(1, 1, 32767, 4)
stop(0, 1)

# Käänny oikealle ja aja lähtöpisteeseen
kaannyOikea(0, 1, 32767, 3)
eteenpain(1, 1, 32767, 4)
stop(0, 1)