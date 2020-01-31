#coding: utf-8


# file create
with open('Temp.txt', 'w') as f:
    print('Msg1', file=f)
with open('Humi.txt', 'w') as f:
    print('Msg2', file=f)
with open('Press.txt', 'w') as f:
    print('Msg3', file=f)
