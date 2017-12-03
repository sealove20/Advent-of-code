from itertools import cycle
lista = ['1221']
i = 0
nova = []
# separa a lista de itens em uma nova lista de números individuais
var = lista[i]
for i in range(len(var)):
    nova.append(int(var[i:i+1]))
print(nova)

pool = cycle(nova)
soma = 0
print(type(pool))
i=0
for item in pool:
    if nova[i] == nova[i+1]:
        soma += nova[i]
    if i == len(nova):
        print('oi')
    i+=1;
