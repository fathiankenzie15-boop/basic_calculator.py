def kalkulator(angka1, angka2, operasi):
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "-":
        return angka1 - angka2
    elif operasi == "*":
        return angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            return "Tidak dapat dibagi dengan nol"
        return angka1 / angka2
    else:
        return "Operasi tidak dikenali"

print(kalkulator(10, 5, "+"))
print(kalkulator(10, 5, "-"))
print(kalkulator(10, 5, "*"))
print(kalkulator(10, 5, "/"))
print(kalkulator(10, 0, "/"))
print(kalkulator(10, 5, "%"))