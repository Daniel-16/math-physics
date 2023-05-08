class Math:
    def exponential(self, number, exponent):
        pass
    def squareRoot(self, number):
        pass
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
        pass
    def power(self, current, volt):
        self.power = current * volt
        return self.power
    def force(self, mass, acceleration):
        pass

physicsOperation = Physics()
current = int(input("Enter the Current in Ampere I "))
volt = int(input("Enter the amount of Voltage V "))
print(f'The Power of the value entered is {physicsOperation.power(current, volt)}')