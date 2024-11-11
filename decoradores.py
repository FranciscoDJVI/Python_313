import time

def decorador(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int: 
            print(f"Es una operacion matematica")
        else:
            print(f"La operación es de tipo {type(result)}")
        return result
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


def duration(func):
    def wrapper(*args, **Kwargs):
        
        inicio = time.time()

        result = func(*args, **Kwargs)

        fin = time.time()

        total_time = fin - inicio

        print(f"Tiempo de ejecución {total_time}s")
        return result
    return wrapper

@duration
@positvo
@decorador
def verficar_operacion():
    
    num= 3
    num_2 = 7
    square  = num + num_2
    print(f"El resultado de la operacion es: {square}")
    return square

@decorador
def order_list():
     
    nums = [1,4,67]
    result = sorted(nums)
    print(result)
    return result

verficar_operacion()
order_list()