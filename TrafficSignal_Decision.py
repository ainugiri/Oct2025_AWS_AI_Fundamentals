def signal(color):
    if color == 'yelow':
        print('Slow down')
    elif color == 'red':
        print ('Stop')
    elif color == 'green':
        print("Moe ahead")

signalcolor = input("Color: ")
signal(signalcolor)