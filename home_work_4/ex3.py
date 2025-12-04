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
    
    def contains(self, point: Point):
        min_x = min(self.bottom_left.x, self.top_right.x)
        max_x = max(self.bottom_left.x, self.top_right.x)
        min_y = min(self.bottom_left.y, self.top_right.y)
        max_y = max(self.bottom_left.y, self.top_right.y)
        
        return (min_x <= point.x <= max_x and
                min_y <= point.y <= max_y)
    