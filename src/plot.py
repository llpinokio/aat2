from collections import OrderedDict
from utils import readkps
import json
import matplotlib.pyplot as plt
import numpy as np

with open("result.json") as f:
	result=json.load(f,object_pairs_hook=OrderedDict)

kps=readkps("../instancias")
xs=np.array([kp.name for kp in kps])
ys=np.array([kp.w for kp in kps])
plt.ylabel(u'W')
plt.xlabel(u'Nome do arquivo')
plt.title(u"W de todas as instâncias")
plt.xticks(rotation=90, ha='right')
plt.plot(xs,ys)
plt.show()

xs=np.array(list(result.keys()))
ys=np.array(list(elem["t"] for elem in result.values()))
plt.ylabel(u'Tempo de execução')
plt.xticks(rotation=90, ha='right')
plt.xlabel(u'Nome do arquivo')
plt.title(u"Tempo de excução para todas as instâncias")
plt.plot(xs,ys)
plt.show()

xs=np.array(list(result.keys()))
ys=np.array(list(elem["it"] for elem in result.values()))
plt.ylabel(u"Número de chamadas recursivas")
plt.xticks(rotation=90, ha='right')
plt.xlabel(u'Nome do arquivo')
plt.title(u"Número de chamadas recursivas para todas as instâncias")
plt.plot(xs,ys)
plt.show()

