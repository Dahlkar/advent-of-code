from shapely.geometry import Point, Polygon


def parse(file):
    with open(file) as f:
        data = []
        min_y = 0
        max_y = 0
        min_x = 0
        max_x = 0
        for line in f.read().split('\n')[:-1]:
            l = line.split(':')
            sensor_line = l[0].split('Sensor at ')[1].split(',')
            beacon_line = l[1].split(' closest beacon is at ')[1].split(',')
            sx = int(sensor_line[0].split('x=')[1])
            sy = int(sensor_line[1].split('y=')[1])
            bx = int(beacon_line[0].split('x=')[1])
            by = int(beacon_line[1].split('y=')[1])
            data.append(
                {
                    'sensor': (sx, sy),
                    'beacon': (bx, by),
                    'distance': (abs(sx-bx) + abs(sy-by)),
                }
            )

    return data

def fill_coverage(data, line):
    sensor = data['sensor']
    beacon = data['beacon']
    to_line = abs(sensor[1] - line)
    distance = data['distance']
    if data['distance'] >= to_line:
        return (sensor[0] - (distance - to_line), sensor[0] + (distance - to_line))

def get_radial_nodes(data, m):
    s = data['sensor']
    sx, sy = s
    nodes = []
    for x in range(data['distance'] + 2):
        for y in range(data['distance'] + 2):
            dist = abs(sx - x) + abs(sy - y)
            if dist > data['distance']:
                nodes.append((x, y))
    result = []
    for node in nodes:
        x, y = node
        if sx + x <= m and sy + y <= m:
            result.append((sx + x, sy + y))
        if sx - x >= 0 and sy + y <= m:
            result.append((sx - x, sy + y))
        if sx + x <= m and sy - y >= 0:
            result.append((sx + x, sy - y))
        if sx - x >= 0 and sy - y >= 0:
            result.append((sx - x, sy - y))

    return result

def is_within(x, y, distance, sensor):
    sx, sy = sensor
    return abs(sx - x) + abs(sy - y) <= distance

def md(p, q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])

def first(file, check):
    data = parse(file)
    coverage = []
    beacons = set()
    for item in data:
        if item['beacon'][1] == check:
            beacons.add(item['beacon'])

        cov = fill_coverage(item, check)
        if cov:
            coverage.append(cov)

    counter = 0
    cov_e = max([cov[1] for cov in coverage])
    cov_s = min([cov[0] for cov in coverage])
    print(cov_e - cov_s)

def second(file, m):
    data = parse(file)
    acoeffs, bcoeffs = set(), set()
    for item in data:
        x, y = item['sensor']
        r = item['distance']
        acoeffs.add(y-x+r+1)
        acoeffs.add(y-x-r-1)
        bcoeffs.add(x+y+r+1)
        bcoeffs.add(x+y-r-1)

    bound = m
    for a in acoeffs:
        for b in bcoeffs:
            p = ((b-a)//2, (a+b)//2)
            if all(0<c<bound for c in p):
                if all(md(p,i['sensor'])>i['distance'] for i in data):
                    print(4_000_000*p[0]+p[1])
    # w = set()
    # o = set()
    # nodes = []
    # for item in data:
    #     nodes += get_radial_nodes(item, m)

    # for item in data:
    #     for node in nodes:
    #         x, y = node
    #         if is_within(x, y, item['distance'], item['sensor']):
    #             w.add((x, y))
    #         else:
    #             o.add((x, y))
            # if is_within(x + 1, y, item['distance'], item['sensor']):
            #     w.add((x + 1, y))
            # else:
            #     o.add(( x + 1, y ))
            # if is_within(x, y + 1, item['distance'], item['sensor']):
            #     w.add((x, y + 1))
            # else:
            #     o.add(( x, y + 1 ))
            # if is_within(x, y - 1, item['distance'], item['sensor']):
            #     w.add((x, y - 1))
            # else:
            #     o.add(( x, y - 1 ))
            # if is_within(x - 1, y, item['distance'], item['sensor']):
            #     w.add((x - 1, y))
            # else:
            #     o.add(( x - 1, y ))
            # if is_within(x - 1, y - 1, item['distance'], item['sensor']):
            #     w.add((x - 1, y - 1))
            # else:
            #     o.add(( x - 1, y - 1 ))
            # if is_within(x + 1, y + 1, item['distance'], item['sensor']):
            #     w.add((x + 1, y + 1))
            # else:
            #     o.add(( x + 1, y + 1 ))

    # result = (o - w).pop()
    # print(result[0] * 4000000 + result[1])

if __name__ == '__main__':
    first('test.txt', 10)
    # first('input.txt', 2000000)

    second('test.txt', 20)
    second('input.txt', 4000000)
