import math
choice = input("Please Choose Class \n Math \n Physics \n")


class Math:
    def exponential(self, number, exponent):
        self.exponential = number ^ exponent
        return self.exponential
    def squareRoot(self, number):
        self.squareRoot = math.sqrt(number)
        return self.squareRoot
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
        self.workDone = force * distance
        return self.workDone
    def power(self, current, volt):
        self.power = current * volt
        return self.power
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
        print(maths.squareRoot(number))
    elif func.lower().replace(" ","") == "modulus":
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print(maths.modulus(num1,num2))
    elif func.lower().replace(" ","") == "twodimensionalvector":
       num1 =  int(input("First vector : "))
       num2 = int(input("Second Vector: "))
       print(maths.twoDimVector(num1,num2))
    elif func.lower().replace(" ","") == "threedimensionalvector":
       num1 =  int(input("First vector : "))
       num2 = int(input("Second Vector: "))
       num3 = int(input("Third Vector: "))
       print(maths.threeDimVector(num1,num2,num3))
    
elif choice.lower() == 'physics':
    func = input("Choose  Function \n Velocity \n Energy \n Workdone \n Power \n Force ")
    if func.lower().replace(" ","") == "velocity":
        distance = int(input("distance: "))
        time  = int(input("time: "))
        print(phy.velocity(distance,time))
    elif func.lower().replace(" ","") == "energy":
        mass = int(input("Mass: "))
        print(phy.energy(mass))
    elif func.lower().replace(" ","") == "workdone":
        force = int(input("Force: "))
        dist = int(input("Distance: "))
        print(phy.workDone(force,distance))
    elif func.lower().replace(" ","") == "power":
       current =  int(input("Current: "))
       volt = int(input("Voltage: "))
       print(phy.power(current,volt))
    elif func.lower().replace(" ","") == "force":
       mass =  int(input("Mass: "))
       acc = int(input("Acceleration: "))
       print(phy.force(mass,acc))


