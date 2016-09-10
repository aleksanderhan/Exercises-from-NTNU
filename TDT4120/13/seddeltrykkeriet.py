from sys import stdin

def max_value(widths, heights, values, paper_width, paper_height):
    result = [None]*(paper_width + 1)
    for width in xrange(paper_width + 1):
        result[width] = [-1] * (paper_height + 1)
    
    min_size = 10**9
    for width in widths:
        if width < min_size:
            min_size = width
    for heigth in heights:
        if heigth < min_size:
            min_size = heigth
    
    for x in xrange(min_size):
        for width in xrange(paper_width):
            result[width][x] = 0
        for heigth in xrange(paper_height):
            result[x][heigth] = 0
    
    for x in xrange(len(values)):
        if widths[x] <= paper_width and heights[x] <= paper_height and result[widths[x]][heights[x]] < values[x]:
            result[widths[x]][heights[x]] = values[x]
        if heights[x] <= paper_width and widths[x] <= paper_height and result[heights[x]][widths[x]] < values[x]:
            result[heights[x]][widths[x]] = values[x]
    
    for width in xrange(paper_width + 1):
        for heigth in xrange(paper_height + 1):
            if result[width][heigth] == 0:
                continue
            if result[width][heigth] == -1:
                best = 0
            else:
                best = result[width][heigth]
            for cutWidth in xrange(1, width):
                if best < result[cutWidth][heigth] + result[width - cutWidth][heigth]:
                    best = result[cutWidth][heigth] + result[width - cutWidth][heigth]
            for cutHeight in xrange(1, heigth):
                if best < result[width][cutHeight] + result[width][heigth - cutHeight]:
                    best = result[width][cutHeight] + result[width][heigth - cutHeight]
            result[width][heigth] = best
    return result[paper_width][paper_height]


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = line.split('x', 1)
        print max_value(widths, heights, values, int(paper_width), int(paper_height))


main()