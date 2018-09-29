![](https://raw.githubusercontent.com/rafafrdz/Leap-Year/master/ejercicio.png)

* Python

```python
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
```

* Scala

  ```scala
  object numerosTyping extends App {
    println("Elige un numero: ")
    var num = readInt()
    var array = new ArrayBuffer[Int]()
    while (num != 0) {
      array += num
      println("Elige un numero: ")
      num = readInt()
    }
    val maximo = array.sorted.reverse(0)
    val minimo = {
      array=array.sorted
      array(0)
    }
    val cont = array.length
    var suma = 0.0
    for (a<-array) suma +=a
    print("Máximo = " + maximo + ", Mínimo = " + minimo + ", Promedio = " + (suma/cont) )
  }
  ```


