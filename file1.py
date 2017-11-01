height = float(input("Wprowadź wzrost w metrach: "))
weight = float(input("Wprowadź wagę w kilogramach: "))

bmi = weight / (height**2) #oblicz BMI
print("Twoje BMI wynosi: %6.2f " % bmi)
if bmi < 20:
    print("Niedowaga")
elif bmi <25:
    print ("Wszystko ok")
elif bmi < 30:
    print("Nadwaga")
else: print("Otylosc")