from turtle import *
import math
import random

class Polygon:
    side: int
    size: int
    def __init__(self, side, size):
        self.side = side
        self.size = size
    def lb_perimeter(self):
        return self.side * self.size
    def lb_apotheme(self):
        return round(self.size / 2 * math.tan(180.0 / self.side * math.pi / 180), 2)
    def lb_area(self):
        return 1 / 2 * self.lb_perimeter() * self.lb_apotheme()
def lb_draw_poly(colored, side, size):
 color(colored)
 for i in range(side):
     forward(size)
     right(360 / side)
    
bgcolor('black')
tab_color = ['red', 'blue', 'yellow', 'white', 'green', 'purple', 'orange', 'turquoise']
poly = Polygon(int(input('Side\'s number : ')), int(input('Side\'s size : ')))

lb_draw_poly(random.choice(tab_color), poly.side, poly.size)
print(f'Perimeter : {poly.lb_perimeter()}px')
print(f'Area : {poly.lb_area()}px²')

done()