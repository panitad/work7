sce = int(input("ระบุคะแนน: "))
if sce >= 80:
    grde = "A"
elif 70 <= sce <= 79:
    grde = "B"
elif 60 <= sce <= 69:
    grde = "C"
elif 50 <= sce <= 59:
    grde = "D"
else:
    grde = "F"
print(f"เกรด {grde}")
