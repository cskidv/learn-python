import random
command = ''
while command<>'[exit]':
    command=raw_input("enter command:")
    if command=='[say]':
        store_say=raw_input("say what?:")
        print(store_say)
    elif command=='[rand]':
        x=raw_input("from where?:")
        y=raw_input("to where?:")
        while int(y)<int(x):
            y=raw_input("y need to be bigger than {}, re-enter to where?:".format(x))
            
        r = random.randint(int(x),int(y))
        print("random number is: {}".format(r))
    elif command=='[exit]':
        print('exiting...')
    else:
        print("unknown command! try [say], [rand], or [exit]")   
