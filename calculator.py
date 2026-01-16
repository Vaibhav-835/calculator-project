try:
    n1=int(input("enter number 1: "))
    n2=int(input("enter number 2: "))
    operation=input("choose operation +,-,*,/ : ")


    match operation:
        case '+' :
            print("your performed operation is + \nresult =",n1+n2)
        case '-' :
            print("your performed operation is - \nresult =",n1-n2)
        case '*' :
            print("your performed operation is * \nresult =",n1*n2)
        case '/' :
            if(n2==0):
                print("undefined")
            else:
                print("your performed operation is / \nresult =",n1/n2)
        case _:
            print("Invalid operation")
except ValueError:
    print("Please enter only numbers for n1 and n2.")
            
