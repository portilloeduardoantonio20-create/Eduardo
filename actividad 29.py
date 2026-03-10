año = int(input("Ingresa el año del que deseas saber si febrero tiene 29 dias \ningresa el año: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(f"El {año} tiene 29 días en febrero")
else:
    print(f"El {año} tiene 28 días en febrero")