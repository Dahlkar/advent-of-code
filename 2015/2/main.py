
def calc_surface_area(h, w, l):
    areas = [h * w, h * l, w * l]
    return sum(2 * area for area in areas) + min(areas)


def calc_ribbon(h, w, l):
    sides = [h, w, l]
    sides.remove(max(sides))
    return sum(2 * side for side in sides) + (h * w * l)


if __name__ == '__main__':
    with open('input.txt') as f:
        total_surface_area = 0
        total_ribbon = 0
        print(calc_surface_area(2, 3, 4))
        print(calc_surface_area(1, 1, 10))
        print(calc_ribbon(2, 3, 4))
        print(calc_ribbon(1, 1, 10))
        for line in f.readlines():
            h, w, l =  line.split('x')
            surface_area = calc_surface_area(int(h), int(w), int(l))
            total_surface_area += surface_area
            ribbon = calc_ribbon(int(h), int(w), int(l))
            total_ribbon += ribbon

        print(total_surface_area)
        print(total_ribbon)
