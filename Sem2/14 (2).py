import math

class Figure:
    def __init__(self, numOfSides, isSquere):
        self.numOfSides = numOfSides
        self.isSquere = isSquere

class Square(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def SquareArea(self, lenghtOfSide):
        if lenghtOfSide <=0:
            print("Co to za herezja!")
        else:
            area = lenghtOfSide * lenghtOfSide
            return area

    def SquerePerimeter(self, lenghtOfSide):
        if lenghtOfSide <=0:
            print("Co to za herezja!")
        else:
            perimeter = 4 * lenghtOfSide
            return perimeter
class Rectangle(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def RectangleArea(self, lenghtOfSideA, lenghtOfSideB):
        if lenghtOfSideA <=0 or lenghtOfSideB <=0:
            print("Co to za herezja!")
        else:
            area = lenghtOfSideA * lenghtOfSideB
            return area

    def RecranglePerimeter(self, lenghtOfSideA, lenghtOfSideB):
        if lenghtOfSideA <=0 or lenghtOfSideB <=0:
            print("Co to za herezja!")
        else:
            permimeter = 2 * lenghtOfSideA + 2 * lenghtOfSideB
            return permimeter

class Triangle(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def TriangleArea(self, base, heigh):
        if base <=0 or heigh <=0:
            print("Co to za herezja!")
        else:
            area = base * heigh * 0.5
            return area

class Trapeze(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def TrapezeArea(self, baseA, baseB, heigh):
        if baseA <=0 or baseB <=0 or heigh <= 0:
            print("Co to za herezja!")
        else:
            area = 0.5 * (baseA + baseB) * heigh
            return area

class Diamond(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def DiamondArea(self, diagonalA, diagonalB):
        if diagonalA <=0 or diagonalB <=0:
            print("Co to za herezja!")
        else:
            area = diagonalA * diagonalB * 0.5
            return area

    def DiagonalPerimeter(self, side):
        if side <=0:
            print("Co to za herezja!")
        else:
            perimeter = 4 * side
            return perimeter

class Circle(Figure):
    def __init__(self, numOfSides, isSquere):
        super().__init__(numOfSides, isSquere)

    def CircleeArea(self, radius):
        if radius <=0:
            print("Co to za herezja!")
        else:
            area = radius**2 * math.pi
            return area

    def CirclePerimeter(self, radius):
        if radius <=0:
            print("Co to za herezja!")
        else:
            permieter = radius*2*math.pi
            return permieter

testowyKwadrat = Square(4, False)
print(testowyKwadrat.SquareArea(5))
print(testowyKwadrat.SquerePerimeter(5))

testoweKolo = Circle(0, True)
print(testoweKolo.CircleeArea(6))
print(testoweKolo.CirclePerimeter(6))


