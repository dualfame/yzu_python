# BMI

h = float(input("身高"))
w = float(input("體重"))
BMI = w / (h/100)**2
print(BMI)
print("身高= %s 體重= %s  BMI= %.2f" % (h, w, BMI))