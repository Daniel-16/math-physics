import math
class Math:
    def exponential(self, number, exponent):
        pass
    def squareRoot(self, number):
        pass
    def modulus(self, num1, num2):
        mod = int(num1) % int(num2)
        return mod
    def twoDimVector(self, num1, num2):
        magnitude = math.sqrt(num1**2 + num2)        
        return magnitude
    def threeDimVectors(self, num1, num2, num3):
        pass
class Physics:
    def velocity(self, distance, time):
        pass
    def energy(self, mass):
        speedOfLight = 3.0 * 10**8
        energy = int(mass) * speedOfLight
        return energy
    def workDone(self, force, distance):
        pass
    def power(self, current, volt):
        pass
    def force(self, mass, acceleration):
        pass