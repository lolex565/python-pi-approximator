import math
from random import random


class point:
    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.origin_dist = float(math.sqrt(self.x_cord * self.x_cord + self.y_cord * self.y_cord))
        self.in_circle = bool()


points_in_circle = 0
points_in_square = 0
point_number = int(input("how many points to generate to calculate the approximation of pi: "))
print_output = str(input("do you want to print all the point cords and other variables while calculating(Yes/No): "))
point_list = []
for x in range(point_number):
    point_list.append(point(random(), random()))
    if print_output == "yes" or  print_output == "Yes" or print_output == "Y" or print_output == "y":
        print("x cord of the %i point is: %.2f" % (x + 1, point_list[x].x_cord))
        print("y cord of the %i point is: %.2f" % (x + 1, point_list[x].y_cord))
        print("distance from the origin of the %i point is: %.2f" % (x + 1, point_list[x].origin_dist))
    if point_list[x].origin_dist <= 1:
        point_list[x].in_circle = True
        if print_output == "yes" or  print_output == "Yes" or print_output == "Y" or print_output == "y":
            print("the %i point is in circle" % (x + 1))
        points_in_circle += 1
    else:
        point_list[x].in_circle = False
        if print_output == "yes" or  print_output == "Yes" or print_output == "Y" or print_output == "y":
            print("the %i point is not in circle" % (x + 1))
    points_in_square +=1
pi_approx = float(4 * points_in_circle / points_in_square)
pi_imported = float(math.pi)
pi_error = float(pi_approx - pi_imported)
pi_error_in_percent = float(pi_error / pi_imported * 100)
if pi_error_in_percent < 0:
    pi_error_in_percent = float(-pi_error_in_percent)
print("You used {} points to generate pi approximation,the calculated approximation is: {} \nPi imported from python math library is equal to {} \nThe error was equal to {}, and in percent it was equal to {}%".format(point_number, pi_approx, pi_imported, pi_error, pi_error_in_percent))