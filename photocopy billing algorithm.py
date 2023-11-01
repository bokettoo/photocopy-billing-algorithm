num = int(input("enter the number of papers "))
if num <= 10: 
    print("the total is ",float(num*0.30))
elif num<= 30 :
    print ("the total is ",float((num-10)*0.25+(10*0.30)))
elif num >30 :
    print ("the total is ", float((num-30)*0.20+(10*0.30)+(20*0.25)))