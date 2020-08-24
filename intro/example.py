import math


def circle_area(radius):
    return math.pi * (radius ** 2)


def exit_with_message(msg):
    print(msg)
    exit()


if __name__ == '__main__':
    
    r = input('radius = ')

    try:
        radius = float(r)
    except:
        exit_with_message('Invalid radius literal')

    if radius < 0:
        exit_with_message('Radius cannot be less than zero')

    area = circle_area(radius)

    output = 'area = {:.3f}'.format(area)
    print(output)


