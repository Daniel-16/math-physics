import math
choice = input("Please Choose Class \n Math \n Physics")


class Math:
    def exponential(self, number, exponent):
        pass
    def squareRoot(self, number):
        pass
    def modulus(self, num1, num2):
        mod = int(num1) % int(num2)
        return mod
    def twoDimVector(self, num1, num2):
        magnitude = math.sqrt(num1**2 + num2**2)        
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

maths = Math()
phy = Physics()


if choice.lower() == "math":
    func = input("Choose Function \n Exponenetial \n SquareRoot \n Modulus \n Two Dimensional Vector \n ")
    if func.lower().replace(" ","") == "exponential":
        exponent = int(input("Base number: "))
        power  = int(input("Power: "))
        print(maths.exponential())
    elif func.lower().replace(" ","") == "squareroot":
        number = int(input("Number to square: "))
    elif func.lower().replace(" ","") == "modulus":
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        maths.modulus(num1,num2)
    elif func.lower().replace(" ","") == "twodimensionalvector":
    
    elif func.lower().replace(" ","") == "threedimensionalvector":
    
     

elif choice.lower() == 'physics':
   func = input("Choose  Function \n Velocity \n Energy \n Workdone \n Power \n Force ")
