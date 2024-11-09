def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Es una operacion matematica")
        return func(*args, **kwargs)
    return wrapper

@decorador
def verficar_operacion():
    num= 3
    num_2 = 3
    square  = num * num_2
    print(f"El resultado de la operacion es: {square}")

verficar_operacion()