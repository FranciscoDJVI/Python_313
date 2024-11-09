from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def turn(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def speed(self):
        pass

    
class Taxi(Car):

    def turn(self):
        return "Encendido"
    
    def turn_off(self):
        return "Apagado"
    
    def speed(self):
        return "Acelero"


taxi = Taxi()
taxi.turn()
taxi.turn_off()
taxi.speed()
