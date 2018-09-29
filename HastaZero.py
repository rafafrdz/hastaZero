def hastaZero():
    print("Teclee algún número entero:")
    num = int(input())
    (max, min) = (num, num)
    (ac, cont) = (num, 1)
    while (num != 0):
        print("Teclee otro número entero:")
        num = int(input())
        if (num < min): min = num
        if (num > max): max = num
        ac += num
        cont += 1
    cont -= 1
    print("La media aritmetica de todos los números que ha tecleado es: " + str(ac / cont))
    print("El número máximo que ha tecleado es: " + str(max))
    print("El número mínimo que ha tecleado es: " + str(min))
