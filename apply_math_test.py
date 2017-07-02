import random
correct = 0
number_question = 0
stop = False
while not stop:
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    a=int(raw_input("how much is {}+{}?:".format(x,y)))
    if a==x+y:
        print('correct, congratulations!')
        correct = correct + 1
    else:
        print('sorry, it is not correct. The correct answer is {}.'.format(x+y))
    number_question = number_question + 1
    print('you got {} out of {} correct'.format(correct, number_question))
    answer=raw_input("do you want to continue y/n: ")
    print(answer)
    if answer=='n' or answer=='N':
        stop = True
