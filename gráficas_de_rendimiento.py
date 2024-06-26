# -*- coding: utf-8 -*-
"""gráficas de rendimiento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IOH86VvmGZ8_d8ahJ-qCWjBcAgNj1YlV

# Taller de rendimiento

*   Juan David Rincon Poveda
*   Juan Felipe Morales Espitia
*   Juan Felipe Fernandez Barrero

Importe de librerias
"""

import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd
import seaborn as sns

"""Función para calcular promedio de las columnas"""

def calcular_promedio(lista):
    if not lista:
        return 0  # Retorna 0 si la lista está vacía para evitar una división por cero
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

"""Función para calcular desviación estandar"""

def calcular_desviacion_estandar(lista):
    if not lista:
        return 0  # Retorna 0 si la lista está vacía
    return statistics.stdev(lista)

"""# Matriz 200x200

1 hilo
"""

# Datos de la matriz 200x200 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [408382, 436670, 463628, 492915, 520007, 546220, 572906, 600125, 628163, 653721, 679407, 706374, 732213, 758351, 784613, 811985, 838714, 865487, 892646, 918819, 944836, 971284, 997022, 1023613, 50491, 77241, 104811, 131394, 156915, 182990]

promedio200_1 = calcular_promedio(y)
des_est200_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 200x200 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 200x200 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y =[197818, 213115, 228128, 244510, 258961, 274684, 288999, 303825, 319573, 334777, 349301, 364295, 378777, 393238, 407727, 422172, 436524, 451333, 465852, 479890, 494418, 509330, 524020, 547734, 562742, 577503, 592315, 607355, 621409, 635840]

promedio200_2 = calcular_promedio(y)
des_est200_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 200x200 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 200x200 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [649199, 662592, 676099, 685493, 694699, 704110, 713814, 727884, 737131, 750003, 763189, 776741, 789988, 804129, 813757, 823256, 831979, 845783, 859294, 872289, 885558, 895452, 905206, 915001, 924153, 937675, 947198, 956694, 969672, 979550]

promedio200_4 = calcular_promedio(y)
des_est200_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 200x200 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 200x200 para 8 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [988014, 999230, 8541, 19674, 27989, 39070, 46930, 57596, 65454, 74654, 84124, 94285, 105156, 115794, 124199, 132441, 143500, 151519, 160083, 171137, 180028, 190910, 201573, 209680, 218210, 228215, 238555, 248345, 256210, 266815]

promedio200_8 = calcular_promedio(y)
des_est200_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 200x200 para 8 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Matriz 400x400

1 hilo
"""

# Datos de la matriz 400x400 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [645050, 832032, 1020551, 206185, 392524, 578961, 769492, 955861, 1142788, 329798, 515400, 701312, 889214, 1074204, 259903, 447599, 637271, 822503, 1007936, 194267, 387150, 573397, 759950, 947020, 1137838, 326737, 512603, 700255, 887813, 700255]

promedio400_1 = calcular_promedio(y)
des_est400_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 400x400 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 400x400 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [987397, 1086756, 185070, 285244, 383396, 481375, 579188, 676817, 775932, 874267, 973095, 1070914, 168314, 266088, 363983, 463434, 561979, 660382, 757566, 858160, 956597, 1055256, 155085, 253628, 352209, 451356, 548719, 646112, 744606, 841792]

promedio400_2 = calcular_promedio(y)
des_est400_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 400x400 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 400x400 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [896670, 950915, 1004533, 58881, 113270, 167674, 222551, 277386, 331139, 386502, 477481, 532791, 587602, 641158, 695838, 749850, 805694, 859633, 913578, 966692, 1021162, 77089, 132631, 186838, 240991, 295620, 350039, 405078, 460028, 515224]

promedio400_4 = calcular_promedio(y)
des_est400_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 400x400 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 400x400 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [568168, 622623, 676022, 727503, 784104, 838177, 891460, 943713, 995705, 47302, 99813, 154758, 207614, 263743, 315213, 367034, 420360, 471632, 524887, 576207, 628095, 683139, 734440, 788296, 840065, 893313, 945405, 998682, 52261, 105891]

promedio400_8 = calcular_promedio(y)
des_est400_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 400x400 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Matriz 800x800

1 hilo
"""

# Datos de la matriz 800x800 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [1797334, 2488857, 2154824, 1852930, 2584034, 2286890, 1977594, 2655267, 2356995, 2047033, 1782307, 2449285, 2154938, 1858809, 2529704, 2219177, 1924507, 2661773, 2355903, 2036163, 1725842, 2430550, 2154285, 1883374, 2578336, 2296076, 2011975, 1727558, 2406289, 2095573]

promedio800_1 = calcular_promedio(y)
des_est800_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 800x800 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 800x800 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [976884, 1868336, 1747184, 1610648, 1475424, 1341849, 1217965, 1106435, 995230, 878509, 1755289, 1631265, 1503063, 1386858, 1258149, 1144137, 1028212, 890449, 1777208, 1661332, 1549049, 1418064, 1303983, 1189901, 1064553, 941293, 1837712, 1709994, 1598178, 1485131]

promedio800_2 = calcular_promedio(y)
des_est800_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 800x800 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 800x800 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [937806, 1375865, 823265, 1275872, 726089, 1183810, 660317, 1166885, 611431, 1066440, 682655, 1156946, 610489, 1083225, 539219, 996992, 460136, 913939, 1364288, 813188, 1269478, 726836, 1203203, 671454, 1127110, 586254, 1033568, 486080, 936935, 1420675]

promedio800_4 = calcular_promedio(y)
des_est800_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 800x800 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 800x800 para 8 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [915525, 1419066, 917163, 1416266, 908808, 1399452, 889555, 1376835, 868623, 1361958, 851657, 1346314, 838743, 1327607, 820270, 1310098, 801635, 1295839, 788830, 1282273, 783781, 1282655, 776501, 1271347, 776235, 1276073, 775007, 1269218, 767710, 1265948]

promedio800_8 = calcular_promedio(y)
des_est800_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 800x800 para 8 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Matriz 1000x1000

1 hilo
"""

# Datos de la matriz 1000x1000 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [4347635, 4363652, 4444464, 4460802, 4545509, 4435979, 4429584, 4365720, 4440810, 4408192, 4355500, 4291189, 4301783, 4153895, 3985503, 3957063, 4872030, 4746340, 4763688, 4720077, 4757555, 4737810, 4639927, 4633787, 4426714, 4343179, 4280602, 4257345, 4230283, 4018335]

promedio1000_1 = calcular_promedio(y)
des_est1000_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 800x800 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 1000x1000 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [2059269, 2101263, 2179432, 2306237, 2353533, 2417238, 2466422, 2484811, 2532064, 2578142, 2682854, 2728491, 2780112, 2845935, 2896587, 2952043, 3052442, 2139627, 2261972, 2317319, 2402537, 2422972, 2533186, 2644521, 2684385, 2793775, 2865599, 2915344, 2963340, 3033222]

promedio1000_2 = calcular_promedio(y)
des_est1000_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 1000x1000 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 1000x1000 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [1107749, 1132781, 1170445, 1209524, 1249889, 1297907, 1323543, 1365788, 1416182, 1443883, 1457866, 1490663, 1607978, 1635167, 1692248, 1715540, 1753750, 1854229, 1881919, 1901886, 1936250, 1952664, 2003870, 1022833, 1037099, 1068474, 1083342, 1179439, 1213873, 1230723]

promedio1000_4 = calcular_promedio(y)
des_est1000_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 1000x1000 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 1000x1000 para 8 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [1300116, 1364406, 1431179, 1497763, 1569660, 1624543, 1679793, 1745444, 1822558, 1886647, 1954997, 2023403, 1090905, 1152418, 1223291, 1296531, 1352605, 1415754, 1484550, 1553309, 1634320, 1703442, 1767539, 1822685, 1900654, 1972533, 2027162, 1096614, 1150639, 1226229]

promedio1000_8 = calcular_promedio(y)
des_est1000_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 1000x1000 para 8 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Matriz 2000x2000

1 hilo
"""

# Datos de la matriz 2000x2000 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [46448851, 46693102, 46527963, 47465110, 47014082, 46611007, 47290865, 46732152, 47375706, 47164833, 47131817, 46718124, 48230244, 47039379, 46763302, 47045670, 46964733, 46889183, 47375194, 46982704, 46696696, 47823450, 47414837, 47143516, 47099423, 46443897, 47233162, 46756443, 47965873, 46131157]

promedio2000_1 = calcular_promedio(y)
des_est2000_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 2000x2000 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 2000x2000 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [22594342, 22821370, 22729553, 22714748, 22453932, 22504080, 22415128, 22415008, 22156571, 22093770, 21876666, 22760589, 22660531, 22524458, 22275195, 21979136, 21675873, 22413820, 22426736, 22261486, 22251583, 21982380, 21808923, 23188003, 22145665, 21907294, 22746200, 22918914, 22648164, 22629936]

promedio2000_2 = calcular_promedio(y)
des_est2000_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 2000x2000 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 2000x2000 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [11819190, 11769601, 11904786, 12106418, 11159769, 11261661, 11330764, 11373150, 11483005, 11629427, 11874793, 11972045, 10996667, 11043441, 11414951, 11415960, 11558656, 11589311, 11737740, 11958873, 11083031, 11147973, 11324498, 11444340, 11647652, 13284886, 13492387, 11600665, 11625390, 11806023]

promedio2000_4 = calcular_promedio(y)
des_est2000_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 2000x2000 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 2000x2000 para 8 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [11148180, 10414628, 10728809, 10949230, 10230446, 10491473, 10711215, 10933059, 10286858, 10576599, 10899157, 11238382, 10549542, 10837668, 11123973, 10324464, 10623378, 10916147, 11158107, 10476249, 10756762, 10954283, 10250358, 10603147, 10971209, 10207535, 10390003, 10749323, 11017244, 10316207]

promedio2000_8 = calcular_promedio(y)
des_est2000_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 2000x2000 para 8 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Matriz 4000x4000

1 hilo
"""

# Datos de la matriz 4000x4000 para 1 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [497989016, 489678485, 493213885, 507635001, 496804757, 502122744, 520606941, 498281717, 496839718, 501091033, 495313782, 498406269, 496869984, 502316156, 501652956, 494720608, 497099126, 495016889, 497958673, 493000630, 487541462, 495920546, 497499777, 499280553, 498250998, 498797635, 502328454, 495739227, 499391685, 508595527]

promedio4000_1 = calcular_promedio(y)
des_est4000_1 = calcular_desviacion_estandar(y)

plt.bar(x, y)
plt.title('Matriz 4000x4000 para 1 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""2 hilos"""

# Datos de la matriz 4000x4000 para 2 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [22594342, 22821370, 22729553, 22714748, 22453932, 22504080, 22415128, 22415008, 22156571, 22093770, 21876666, 22760589, 22660531, 22524458, 22275195, 21979136, 21675873, 22413820, 22426736, 22261486, 22251583, 21982380, 21808923, 23188003, 22145665, 21907294, 22746200, 22918914, 22648164, 22629936]

promedio4000_2 = calcular_promedio(y)
des_est4000_2 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='red')
plt.title('Matriz 4000x4000 para 2 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""4 hilos"""

# Datos de la matriz 4000x4000 para 4 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [102301624, 105339726, 106839816, 106083809, 106342807, 106126588, 106179448, 106516895, 109000805, 106008706, 106335108, 106516057, 106021910, 105287423, 106424895, 109113616, 109174873, 108244956, 106485187, 108686432, 106382296, 106222638, 106645186, 109680907, 106708501, 106902851, 106421691, 106392397, 105851562, 105670829]

promedio4000_4 = calcular_promedio(y)
des_est4000_4 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='green')
plt.title('Matriz 4000x4000 para 4 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""8 hilos"""

# Datos de la matriz 4000x4000 para 8 hilo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [101209185, 97640880, 98483080, 97346867, 99436300, 96475697, 99544041, 97678684, 95485987, 98229322, 99801798, 96881747, 96761676, 97096695, 97408719, 96693122, 97847702, 96754139, 96902218, 97264730, 98179787, 97195496, 97623730, 97761131, 97413586, 97263803, 98371704, 97422219, 97170237, 97203875]

promedio4000_8 = calcular_promedio(y)
des_est4000_8 = calcular_desviacion_estandar(y)

plt.bar(x, y, color='purple')
plt.title('Matriz 4000x4000 para 8 hilo')
plt.xlabel('Iteración')
plt.ylabel('Milisegundos')
plt.show()

"""# Comparación de rendimiento en base a hilos

Gráfica matriz 200x200
"""

x = [1, 2, 4, 8]
promedio_1 = [promedio200_1, promedio200_2, promedio200_4, promedio200_8]
desviacion_estandar_1 = [des_est200_1, des_est200_2, des_est200_4, des_est200_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [700000, 500000, 750000, 250000]
desviacion_estandar_2 = [400000, 200000, 200000, 300000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='red')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='orange')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color='purple')
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='pink')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 200x200')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()

"""Gráfica matriz 400x400"""

x = [1, 2, 4, 8]
promedio_1 = [promedio400_1, promedio400_2, promedio400_4, promedio400_8]
desviacion_estandar_1 = [des_est400_1, des_est400_2, des_est400_4, des_est400_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [650000, 500000, 690000, 300000]
desviacion_estandar_2 = [400000, 200000, 200000, 220000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='blue')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='cyan')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color="#007819")
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='#49FF00')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 400x400')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()

"""Gráfica matriz 800x800"""

x = [1, 2, 4, 8]
promedio_1 = [promedio800_1, promedio800_2, promedio800_4, promedio800_8]
desviacion_estandar_1 = [des_est800_1, des_est800_2, des_est800_4, des_est800_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [2000000, 1300000, 1500000, 700000]
desviacion_estandar_2 = [1000000, 200000, 710000, 400000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='#87007E')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='#FF8CF7')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color="red")
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='#F5A9A9')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 800x800')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()

"""Gráfica matriz 1000x1000"""

x = [1, 2, 4, 8]
promedio_1 = [promedio1000_1, promedio1000_2, promedio1000_4, promedio1000_8]
desviacion_estandar_1 = [des_est1000_1, des_est1000_2, des_est1000_4, des_est1000_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [3500000, 2000000, 2200000, 1200000]
desviacion_estandar_2 = [1000000, 200000, 900000, 600000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='#3100A2')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='#7AB6FE')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color="#FF0046")
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='#FF99B5')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 1000x1000')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()

"""Gráfica matriz 2000x2000"""

x = [1, 2, 4, 8]
promedio_1 = [promedio2000_1, promedio2000_2, promedio2000_4, promedio2000_8]
desviacion_estandar_1 = [des_est2000_1, des_est2000_2, des_est2000_4, des_est2000_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [40000000, 18000000, 20000000, 10000000]
desviacion_estandar_2 = [5000000, 300000, 1000000, 900000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='#888204')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='gold')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color="#E95800")
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='#FFC099')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 2000x2000')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()

"""Gráfica matriz 4000x4000"""

x = [1, 2, 4, 8]
promedio_1 = [promedio4000_1, promedio4000_2, promedio4000_4, promedio4000_8]
desviacion_estandar_1 = [des_est4000_1, des_est4000_2, des_est4000_4, des_est4000_8]

# Datos de ejemplo para el segundo SO
promedio_2 = [400000000, 18000000, 200000000, 60000000]
desviacion_estandar_2 = [5000000, 500000, 1000000, 1000000]

# Configuración para las barras
width = 0.2  # Ancho de las barras

# Posiciones para las barras
x_indices = np.arange(len(x))

# Crear la gráfica de barras
fig, ax = plt.subplots()

# Dibujar las barras para el primer SO
bar1 = ax.bar(x_indices - width, promedio_1, width, label='Promedio SO1', color='#005C01')
bar2 = ax.bar(x_indices, desviacion_estandar_1, width, label='Desviación Estándar SO1', color='#15CB00')

# Dibujar las barras para el segundo SO
bar3 = ax.bar(x_indices + width, promedio_2, width, label='Promedio SO2', color="teal")
bar4 = ax.bar(x_indices + 2*width, desviacion_estandar_2, width, label='Desviación Estándar SO2', color='#36FF9D')

# Añadir etiquetas y título
ax.set_title('Promedio y Desviación Estándar de tiempo de Matriz 4000x4000')
ax.set_xlabel('# Hilos')
ax.set_ylabel('Milisegundos')
ax.set_xticks(x_indices + width / 2)
ax.set_xticklabels(x)
ax.legend()

# Mostrar la gráfica
plt.show()