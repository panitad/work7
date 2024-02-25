wkg = float(input("น้ำหนัก (กิโลกรัม): "))
hem = float(input("ส่วนสูง (เมตร): "))
bmi = wkg / (hem**2)
print(f"BMI คือ {bmi:.1f}")
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")
