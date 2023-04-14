import time

print('-=-'*12)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*12)

a1 = float(input('Primeiro lado de um triângulo: '))
a2 = float(input('Segundo lado de um triângulo: '))
a3 = float(input('Terceiro lado de um triângulo: '))

ordem = [a1, a2, a3]
ordem = sorted(ordem)

print('CALCULANDO...')
time.sleep(1)

if ordem[0] + ordem[1] > a3:
    print('Esse triângulo pode existir!')
else:
    print('kkkkkk triângulo impossível mané.')