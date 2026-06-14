import random

print('dez vezes randomicos')
for x in range(10):
    print(random.random())
print('\n'*2)
print('10 flutuantes randomicos - uniform')
for x in range(10):
    print(random.uniform(15,25))
print('\n'*2)

print('10 no range fazendo sample numa lista')
for x in range(10):
    print(random.sample(range(1,101),6))

print('\n'*2 )

print('agora é um shuffle')
a= list(range(1,11))
random.shuffle(a)
print(a)
print('\n'*2)
print('agora é um randint')
for x in range(10):
    print(' %d\r' % random.randint(1,100))

          
