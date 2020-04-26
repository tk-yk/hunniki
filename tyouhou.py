#四角形の面積
#高さ*幅

#対角線の長さ
#ルートa2 + b2
import math

class Rectangle:
    def __init__(self , height , width):
        self.height = height
        self.width = width

    def area(self):
        return f"{self.width * self.height:.2f}"

    def diagonal(self):
        return f"{math.sqrt((self.height**2)+(self.width**2)):.2f}"


rectangle1 = Rectangle(height =5, width =6)
print(rectangle1.area())
print(rectangle1.diagonal())

rectangle2 = Rectangle(height = 3, width =3)
print(rectangle2.area())
print(rectangle2.diagonal())

