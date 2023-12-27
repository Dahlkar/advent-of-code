#!/usr/bin/env python3
from dataclasses import dataclass, fields
from itertools import combinations

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __post_init__(self):
        for f in fields(self):
            setattr(self, f.name, int(getattr(self, f.name)))


def parse_data(filename):
    with open(filename) as f:
        lines = []
        for line in f.read().splitlines():
            start, speed = line.split(' @ ')
            start = Point(*start.split(', '))
            speed = Point(*speed.split(', '))
            lines.append((start, speed))

        return lines


def line(point, speed):
    m = speed.y/speed.x
    q = -m * point.x + point.y
    return m, q


def intersecting(lines, start, end):
    pairs = combinations(lines, 2)
    intersections = 0
    for (p1, s1), (p2, s2) in pairs:
        if (s1.x * s2.y - s2.x * s1.y) == 0:
            continue
        m1, q1 = line(p1, s1)
        m2, q2 = line(p2, s2)
        xc = (q2 - q1) / (m1 - m2)
        yc = m1 * xc + q1
        tc1 = (xc - p1.x) / s1.x
        tc2 = (xc - p2.x) / s2.x
        if tc1 < 0 or tc2 < 0:
            continue

        if start <= xc <= end and start <= yc <= end:
            intersections += 1

    return intersections

def part2(lines):
    from sympy import solve, symbols

    x = symbols('x')
    y = symbols('y')
    z = symbols('z')
    vx = symbols('vx')
    vy = symbols('vy')
    vz = symbols('vz')

    p1, s1 = lines[0]
    p2, s2 = lines[1]
    p3, s3 = lines[2]

    x1, y1, z1 = p1.x, p1.y, p1.z
    x2, y2, z2 = p2.x, p2.y, p2.z
    x3, y3, z3 = p3.x, p3.y, p3.z

    vx1, vy1, vz1 = s1.x, s1.y, s1.z
    vx2, vy2, vz2 = s2.x, s2.y, s2.z
    vx3, vy3, vz3 = s3.x, s3.y, s3.z

    sols = solve(
        [(x-x1)*(vy-vy1)-(y-y1)*(vx-vx1),
         (y-y1)*(vz-vz1)-(z-z1)*(vy-vy1),
         (x-x2)*(vy-vy2)-(y-y2)*(vx-vx2),
         (y-y2)*(vz-vz2)-(z-z2)*(vy-vy2),
         (x-x3)*(vy-vy3)-(y-y3)*(vx-vx3),
         (y-y3)*(vz-vz3)-(z-z3)*(vy-vy3)] ,
        [x, y, z, vx, vy, vz], dict=True)

    # select solution with integer speed components
    for s in sols:
        if s[vx]==int(s[vx]) and s[vy]==int(s[vy]) and s[vz]==int(s[vz]):
            print(s)
            break

    return s[x]+s[y]+s[z]


lines = parse_data('example.txt')
result = intersecting(lines, 7, 27)
print(result)
assert result == 2
result = part2(lines)
print(result)
assert result == 47
lines = parse_data('input.txt')
result = intersecting(lines, 200000000000000, 400000000000000)
print(result)
result = part2(lines)
print(result)
