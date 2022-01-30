# menu-navigator
while True :
    print("1 home")
    print("2 about")
    print("3 contact")
    print("4 exit")
    command= input()

    if int(command)==1:
     print("home")
    elif int(command)==2:
     print("about")
    elif int(command)==3:
     print("contact")
    elif int(command)==4:
     break
    else:
     print("wrong menu id")
     print('--------')
