import pdb

from hometown import tavern_scene
from classes import Obstacle


def left(calc_list):
    calculated_list = []
    for each in calc_list:
        line = each[0], each[1], each[0], (each[1] + each[3])
        calculated_list.append(line)
    print(calculated_list)


def right(calc_list):
    calculated_list = []
    for each in calc_list:
        line = (each[0] + each[2]), each[1], (each[0] + each[2]), each[1]
        calculated_list.append(line)
    print(calculated_list)


def top(calc_list):
    calculated_list = []
    for each in calc_list:
        line = each[0], each[1], (each[0] + each[2]), each[1]
        calculated_list.append(line)
    return


def bottom(calc_list):
    calculated_list = []
    for each in calc_list:
        line = each[0], (each[1] + each[3]), (each[0] + each[2]), (each[1] + each[3])
        calculated_list.append(line)


def sort_lines(line_list):
    mid = []
    left = []
    right = []
    bottom = []
    sides = []
    for line in line_list.key:
        if line == 'mid':
            mid.append(line)
        elif line == 'left':
            return left.append(line)
        elif line == 'right':
            return right.append(line)
        elif line == 'bottom':
            return bottom.append(line)
        elif line == 'sides':
            return sides.append(line)


def linecalc(dictionary):
    for each in dictionary:
        if each == 'left':
            left(each['left'])
        if each == 'right':
            right(each['right'])
        if each == 'top':
            top(each['top'])
        if each == 'bottom':
            bottom(each['bottom'])
