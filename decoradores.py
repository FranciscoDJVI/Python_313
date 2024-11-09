def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Es una operacion matematica")
        return func(*args, **kwargs)
    return wrapper


def positvo(func):
    def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not result >0:
                print("El resultado es un numero negativo")
            else:
                print("El resultado es un numero positivo")
            return result
    return wrapper

@positvo
@decorador
def verficar_operacion():
    num= 3
    num_2 = 7
    square  = num - num_2
    print(f"El resultado de la operacion es: {square}")
    return square

verficar_operacion()