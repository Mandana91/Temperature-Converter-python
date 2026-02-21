print("1-cilsius")
print("2-fahrenheit")

choice=input("yek add bezan:")
if choice=="1":
    cilsius=float(input("dama be c"))
    fahrenheit = (cilsius * 9/5) + 32
    print("natije santigrad be farenhait" , fahrenheit)

elif choice=="2":
    
    fahrenheit  = float(input(" dama b f "))
cilsius = (fahrenheit - 32) * 5/9
print("natije farenhait be silisius" ,cilsius)


