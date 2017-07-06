import random

command = ''
while command != '[exit]':
    command = raw_input("enter command:")
    if command == '[say]':
        message = raw_input("say what?:")
        print(message)
        
    elif command == '[rand]':
        x = int(raw_input("from where?:"))
        y = int(raw_input("to where?:"))
        while y < x:
            y = int(raw_input(
                "error! needs to be bigger than {}. try again:".format(x))
            )           
        r = random.randint(x, y)
        print("{}".format(r))
        
    elif command == '[add]':
        x = int(raw_input("add what?"))
        y = int(raw_input("to what?"))
        print(x + y)
        
    elif command == '[exit]':
        print('exiting...')
        
    else:
        print("unknown command!")  
