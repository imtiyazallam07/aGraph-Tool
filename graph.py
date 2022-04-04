from math import sqrt
from matplotlib import markers, pyplot


def point(point1):
    if not point1:
        return
    pyplot.figure("Point")
    pyplot.grid()
    pyplot.plot([point1[0]], [point1[1]], marker="o", markersize=5)
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def line(point):
    if not point:
        return
    pyplot.figure("Line")
    pyplot.plot([point[0][0], point[1][0]], [
                point[0][1], point[1][1]], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def midpoint(point):
    if not point:
        return
    pyplot.figure("Midpoint")
    x, y = mid(point)
    pyplot.plot(x, y, marker='o')
    pyplot.plot([point[0][0], point[1][0]], [
                point[0][1], point[1][1]], marker='o')
    pyplot.title('Midpoint: (' + str(x) + ', ' + str(y) + ')')
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.grid()
    pyplot.show()


def trisect(point):
    if not point:
        return
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
    if not point:
        return
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
    if not point:
        return
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
    if not point:
        return
    pyplot.figure("Slope")
    s = slp(point)
    pyplot.title("Slope: " + str(s))
    pyplot.plot(point[0], point[1], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def perpendicular(point):
    if not point:
        return
    a, b = point
    pyplot.figure("Slope of perpendicular")
    x, y = mid((a, b))
    s = slp(point)
    s = -1 / s
    pyplot.axline((x, y), slope=s)
    pyplot.title("Slope of perpendicular: " + str(s))
    pyplot.plot([a[0], b[0]], [a[1], b[1]], marker='o')
    pyplot.grid()
    pyplot.xlabel('X axis')
    pyplot.ylabel('Y axis')
    pyplot.show()


def median(point):
    a, b, c = point
    m = ((a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3)
    pyplot.figure('Median')
    pyplot.title(
        'Point of intersection of medians of the triangle is at \n' + str(m))
    m = mid((b, c))
    pyplot.plot([a[0], m[0]], [a[1], m[1]], marker='o')
    m = mid((a, c))
    pyplot.plot([b[0], m[0]], [b[1], m[1]], marker='o')
    m = mid((a, b))
    pyplot.plot([c[0], m[0]], [c[1], m[1]], marker='o')
    pyplot.plot([a[0], b[0]], [a[1], b[1]], marker='o', color='blue')
    pyplot.plot([b[0], c[0]], [b[1], c[1]], marker='o', color='blue')
    pyplot.plot([c[0], a[0]], [c[1], a[1]], marker='o', color='blue')
    pyplot.grid()
    pyplot.show()


def mid(point):
    return (point[0][0] + point[1][0]) / 2.0, (point[0][1] + point[1][1]) / 2.0


def slp(point):
    return (point[1][1] - point[0][1])/(point[1][0] - point[0][0])
