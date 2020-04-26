import math




#円の面積の求め方
#radius * radius / 3.14
#円周の求め方
#2 * radius * 3.14



# 半径１の円
class Circle:
    def __init__(self, radius ):
        self.radius = radius

    def area(self):
        return f"{self.radius ** 2 * math.pi:.2f}"


    def perimeter(self):
        return f"{2 * self.radius * math.pi:.2f}"


circle1 = Circle(radius=1)
print(circle1.area()) # 3.14
print(circle1.perimeter()) # 6.28

# 半径３の円
circle3 = Circle(radius=3)
print(circle3.area()) # 28.27
print(circle3.perimeter()) # 1 8.85



