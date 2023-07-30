key=str(95486321)
m=int(0)
while True:
    message= str(input("Enter your text: "))

    
    if len(message)!= 8:    
        print("the text need to be in 8 characters")
        
    else:
        for i in range (8):

            m+=(ord(message[i]))
            result=m*key[i]
            num=str(m)+""
        def encrypte(x, key):
            result=x*int(key[1])+int((key[5]+key[0] +key[6] +key[7] ))*int(key[4])**2
            print(f"Your word  encypted is: {result}")
        encrypte(m, key)
        break
    

    

    