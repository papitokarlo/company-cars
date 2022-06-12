from django.test import TestCase

# Create your tests here.


import sys


class Test():
    __name__ = "User"
    def __init__(self, x):
        self.name = x
        self.lname = x*3

    def __str__(self):
        return (f'{self.name}, {self.lname}, {self.__name__}')

per1 = Test('ca')

print(per1)

from platform import system, platform,version

print(version())

print(system())
print(platform())

# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False
#     print(event)


"""
Since detonations take place only at odd times, if n (the number of seconds) is even,
the grid is composed only of O.
At n == 1, no detonations take place, so the grid is the starting grid (initial_grid).
At n == 3, the first detonation happens (grid_after_first_detonation).
After this second, we note that there is a recurrent pattern that repeat itself every 4 seconds:
- at n == 5, 9, 13, ... (i.e. when n % 4 == 1), the grid is equal to grid_after_second_detonation
- at n == 7, 11, 15, ... (i.e when n % 4 == 3), the grid is equal to grid_after_third_detonation
"""


def createGrid(r, c, grid_at_previous_step):
    grid_at_next_step = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            current_cell = grid_at_previous_step[i][j]
            if current_cell == 'O':
                grid_at_next_step[i][j] = '.'
                if i - 1 >= 0:
                    grid_at_next_step[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    grid_at_next_step[i + 1][j] = '.'
                if j - 1 >= 0:
                    grid_at_next_step[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    grid_at_next_step[i][j + 1] = '.'
    return grid_at_next_step


def bomberMan(n, r, c, initial_grid):

    grid_after_first_detonation = createGrid(r, c, initial_grid)

    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        return initial_grid if n == 1 else grid_after_first_detonation
    else:
        grid_after_second_detonation = createGrid(r, c, grid_after_first_detonation)
        grid_after_third_detonation = createGrid(r, c, grid_after_second_detonation)
        return grid_after_second_detonation if n % 4 == 1 else grid_after_third_detonation


if __name__ == "__main__":
    r, c, n = input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    for _ in range(r):
       grid.append(list(str(input().strip())))
    result = bomberMan(n, r, c, grid)
    for row in result:
        print("".join(row))

print('code execute succesfuly')

# for _ in range(int(input())):
#     s = input()
#     s = list(s[::-1])
#     done = 0
#     for i in range(1,len(s)):
#         if s[i-1] > s[i]:
#             for j in range(i):
#                 if s[j] > s[i]:
#                     s[j],s[i] = s[i],s[j]
#                     s = sorted(s[:i])[::-1] + s[i:]
#                     print("".join(s[::-1]))
#                     break
#             break
#     else:
#         print("no answer")
def biggerIsGreater(w):
    w = list(w)
    # Find non-increasing suffix
    i = len(w)-1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    # Find the rightmost successor to pivot in the suffix
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    
    # Swap the pivot with the rightmost character
    w[i-1], w[j] = w[j], w[i-1]

    # Reverse the sufix
    w[i:] = w[len(w)-1:i-1:-1]

    return ''.join(w)

biggerIsGreater('23')
biggerIsGreater('hdd')
biggerIsGreater('ajjbd')
biggerIsGreater('YGYRR')
