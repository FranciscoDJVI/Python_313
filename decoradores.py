

def decorador(self, func):
    def wrapper(*args, **kwargs):
        square = self.num ** self.num_2
    return wrapper

@decorador
def verficar_operacion(result: int):
    print(f"Es una operacion matematica {result}")