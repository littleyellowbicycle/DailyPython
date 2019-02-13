import random, string
f = open('action_code.txt', 'w')
num = 200
chars = string.ascii_letters + string.digits
length = 7
for i in range(num):
    s = [random.choice(chars) for i in range(10)]
    f.write(' '.join(s) + '\n')
f.close()