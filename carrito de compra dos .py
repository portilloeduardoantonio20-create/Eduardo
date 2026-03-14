productos = []
precios = []

while True:

    print("CESTA DE COMPRA ")
    print("1: Agregar producto")
    print("2: Mostrar cesta")
    print("3: Eliminar producto")
    print("4: Calcular total")
    print("5: Renunciar")
    
    valor = input("Elije una opcion: ")
    
    if valor == "1":
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        
        productos.append(nombre)
        precios.append(precio)
        
        print("El producto a sido agregado al carrito")
        
    elif valor == "2":
        
        if len(productos) == 0:
            print("La cesta esta vacia")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}- {productos[i]} $ {precios[i]}")
                
    elif valor == "3":
        
        if len(productos) == 0:
            print("No ay productos que eliminar")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}- {productos[i]} $ {precios[i]}")
                
            eliminar = int(input("Ingrese el numero del producto que deseas eliminar: "))
            
            productos.pop(eliminar - 1)
            precios.pop(eliminar - 1)
            
            print("El producto seleccionado a sido eliminado")
            
    elif valor == "4":
        
        total = 0
        
        for precio in precios:
            total = total + precio
            
        print(f"El total de tus productos a pagar es: ${total}")
        
    elif valor == "5":
        print("Espero te aya sido de ayudua")
        break
        
    else:
        print("opcion no valida")