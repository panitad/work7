inme = float(input("รายได้: "))
if inme >= 15000 and inme < 20000:
    type = "บัตร Sliver"
elif inme < 100000:
    type = "บัตร Gold"
else:
    type = "บัตร Platinum"
print(f"สามารถทำ{type} ได้")
