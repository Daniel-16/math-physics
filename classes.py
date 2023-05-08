import math

class Math:
    def exponential(self, number, exponent):
        self.exponential = number ^ exponent
        return self.exponential
    def squareRoot(self, number):
        self.squareRoot = math.sqrt(number)
        return self.squareRoot
    def modulus(self, num1, num2):
        pass
    def twoDimVector(self, num1, num2):
        pass
    def threeDimVectors(self, num1, num2, num3):
        pass
class Physics:
    def velocity(self, distance, time):
        pass
    def energy(self, mass):
        pass
    def workDone(self, force, distance):
        self.workDone = force * distance
        return self.workDone
    def power(self, current, volt):
        self.power = current * volt
        return self.power
    def force(self, mass, acceleration):
        pass

physicsOperation = Physics()
current = int(input("Enter the Current in Ampere I "))
volt = int(input("Enter the amount of Voltage V "))
print(f'The Power of the value entered is {physicsOperation.power(current, volt)}')
