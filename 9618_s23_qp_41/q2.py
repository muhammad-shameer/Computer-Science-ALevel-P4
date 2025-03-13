class Vehicle():
    '''
    self.__ID string
    self.__MaxSpeed integer
    self.__IncreaseAmount integer
    self.__CurrentSpeed integer
    self.__HorizontalPosition
    '''
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0
    
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP
    
    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print(f"Current Position: {self.__HorizontalPosition}")
        print(f"Current Speed: {self.__CurrentSpeed}")

class Helicopter(Vehicle):
    '''
    VerticalPosition integer
    VerticalChange integer
    MaxHeight integer
    '''
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        Vehicle.__init__(self, ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight
    
    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange

        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))

        if Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self))

        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))
    
    def OutputCurrentPosition(self):
        print(f"Current Position: {Vehicle.GetHorizontalPosition(self)}")
        print(f"Current Speed: {Vehicle.GetCurrentSpeed(self)}")
        print(f"Current Vertical Position: {self.__VerticalPosition}")


def main():
    Car = Vehicle("Tiger", 100, 20)
    Heli = Helicopter("Lion", 350, 40, 3, 100)

    Car.IncreaseSpeed()
    Car.IncreaseSpeed()

    Car.OutputCurrentPosition()

    Heli.IncreaseSpeed()
    Heli.IncreaseSpeed()

    Heli.OutputCurrentPosition()

if __name__ == "__main__":
    main()    