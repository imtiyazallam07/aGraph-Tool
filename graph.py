from math import sqrt
from matplotlib import markers, pyplot


def point(point1):
    if(len(point1) != 2):
        print('Traceback: Invalid data (2 parameters required)')
    pyplot.figure("Point")
    pyplot.grid()
    pyplot.plot([point1[0]], [point1[1]], marker="o", markersize=5)
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def line(point):
    pyplot.figure("Line")
    pyplot.plot(point[0], point[1], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def midpoint(point):
    pyplot.figure("Midpoint")
    x = (point[0][0] + point[1][0]) / 2.0
    y = (point[0][1] + point[1][1]) / 2.0
    pyplot.plot(x, y, marker='o')
    pyplot.plot([point[0][0], point[1][0]], [
                point[0][1], point[1][1]], marker='o')
    pyplot.title('Midpoint: (' + str(x) + ', ' + str(y) + ')')
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.grid()
    pyplot.show()


def trisect(point):
    pyplot.figure("Trisect")
    x = (point[0][0] + point[1][0] * 2) / 3.0
    y = (point[0][1] + point[1][1] * 2) / 3.0
    pyplot.plot(x, y, marker='o')
    x1 = (point[0][0]*2 + point[1][0]) / 3.0
    y1 = (point[0][1]*2 + point[1][1]) / 3.0
    pyplot.plot(x1, y1, marker='o')
    pyplot.plot([point[0][0], point[1][0]], [
                point[0][1], point[1][1]], marker='o')
    pyplot.title('2 points after trisection: (' + str(x) + ', ' +
                 str(y) + '), (' + str(x1) + ', ' + str(y1) + ')')
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.grid()
    pyplot.show()


def split(point):
    pyplot.figure("Section")
    x = (point[0][0] * point[2][1] + point[1][0] *
         point[2][0]) / (point[2][1] + point[2][0])
    y = (point[0][1] * point[2][1] + point[1][1] *
         point[2][0]) / (point[2][1] + point[2][0])
    pyplot.plot(x, y, marker='o')
    pyplot.plot([point[0][0], point[1][0]], [
                point[0][1], point[1][1]], marker='o')
    pyplot.title('Point: (' + str(x) + ', ' + str(y) + ')')
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.grid()
    pyplot.show()


def distance(point):
    pyplot.figure("Length")
    d = sqrt(((point[1][0] - point[0][0]) ** 2) +
             ((point[1][1] - point[1][0]) ** 2))
    pyplot.title("Length: " + str(d))
    pyplot.plot(point[0], point[1], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def slope(point):
    pyplot.figure("Slope")
    s = (point[1][1] - point[0][1])/(point[1][0] - point[0][0])
    pyplot.title("Slope: " + str(s))
    pyplot.plot(point[0], point[1], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()

def perpendicular(point):
    pyplot.figure("Slope of perpendicular")
    s = (point[1][1] - point[0][1])/(point[1][0] - point[0][0])
    s = -1 / s
    pyplot.title("Slope of perpendicular: " + str(s))
    pyplot.plot(point[0], point[1], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()
