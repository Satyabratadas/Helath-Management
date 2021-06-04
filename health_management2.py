import datetime
user = "yes"
while(user == "yes"):
    def getdate():
        return datetime.datetime.now
    
    def take(t):
        if(t==1):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                value=input("type here\n")
                with open("Sayak_food.txt","a") as p:
                    p.write(str([str(getdate())]) + ": "+value+"\n")
                    print("successfully written")
            elif(x==2):
                value = input('text here: \n')
                with open('Sayak_excersize.txt',"a") as p:
                    p.write(str([str(getdate())])+": " +value+"\n")
                    print("add successful")
        
        elif(t==2):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                value=input("type here\n")
                with open("Saswata_food.txt","a") as p:
                    p.write(str([str(getdate())]) + ": "+value+"\n")
                    print("successfully written")
            elif(x==2):
                value = input('text here: \n')
                with open('Saswata_excersize.txt',"a") as p:
                    p.write(str([str(getdate())])+": " +value+"\n")
                    print("add successful")
        
        elif(t==3):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                value=input("type here\n")
                with open("Soubhik_food.txt","a") as p:
                    p.write(str([str(getdate())]) + ": "+value+"\n")
                    print("successfully written")
            elif(x==2):
                value = input('text here: \n')
                with open('Soubhik_excersize.txt',"a") as p:
                    p.write(str([str(getdate())])+": " +value+"\n")
                    print("add successful")
        
        elif(t==4):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                value=input("type here\n")
                with open("Rambo_food.txt","a") as p:
                    p.write(str([str(getdate())]) + ": "+value+"\n")
                    print("successfully written")
            elif(x==2):
                value = input('text here: \n')
                with open('Rambo_excersize.txt',"a") as p:
                    p.write(str([str(getdate())])+": " +value+"\n")
                    print("add successful")
                    
        else:
            print("Enter the valid input (1(Sayak)) (2(Saswata)) (3(Soubhik)) (4(Rambo)): ")
    
    def retrive(t):
        if(t==1):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                with open('Sayak_food.txt') as p:
                    for i in p:
                        print(i,end="")
            elif(x==2):
                with open('Sayak_excersize.txt') as p:
                    for i in p:
                        print(i,end="")
        
        elif(t==2):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                with open('Saswata_food.txt') as p:
                    for i in p:
                        print(i,end="")
            elif(x==2):
                with open('Saswata_excersize.txt') as p:
                    for i in p:
                        print(i,end="")

        elif(t==3):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                with open('Soubhik_food.txt') as p:
                    for i in p:
                        print(i,end="")
            elif(x==2):
                with open('Soubhik_excersize.txt') as p:
                    for i in p:
                        print(i,end="")

        elif(t==4):
            x = int(input("choose 1 for food 2 for excersize \n"))
            if(x==1):
                with open('Rambo_food.txt') as p:
                    for i in p:
                        print(i,end="")
            elif(x==2):
                with open('Rambo_excersize.txt') as p:
                    for i in p:
                        print(i,end="")
        
        else:
            print("enter valid input (Sayak,Saswata,Soubhik,Rambo): ")

    if __name__ == "__main__":
        print("Health Management System")
        a = int(input("Choose 1 for log the data and 2 for retrive the data: "))
        if(a==1):
            b = int(input("1 for Sayak 2 for Saswata 3 for Soubhik 4 for Rambo: "))  # add more user if you wnat as your wish then take part will increase like t==1,2,3..n and retrive part also increase
            take(b)
        else:
            b = int(input("1 for Sayak 2 for Saswata 3 for Soubhik 4 for Rambo: "))
            retrive(b)
    user = input("enter yes to continue:  ")