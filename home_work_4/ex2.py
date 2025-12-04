from home_work_4.ex1 import Point

class Rectangle:
    def __init__(self, bottom_left: Point, top_right: Point):
        self.bottom_left = bottom_left
        self.top_right = top_right
    
    def width(self):
        return abs(self.top_right.x - self.bottom_left.x)
    
    def height(self):
        return abs(self.top_right.y - self.bottom_left.y)
    
    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return 2 * (self.width() + self.height())
    