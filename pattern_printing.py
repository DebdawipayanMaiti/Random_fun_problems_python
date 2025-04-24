# Pattern Printing Python Code

# Step 1: Right-Angled Triangle of Stars
def right_angled_triangle_stars():
    n = 5
    for i in range(1, n + 1):
        print('* ' * i)

# Step 2: Inverted Right-Angled Triangle of Stars
def inverted_right_angled_triangle_stars():
    n = 5
    for i in range(n, 0, -1):
        print('* ' * i)

# Step 3: Pyramid of Stars
def pyramid_of_stars():
    n = 5
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

# Step 4: Inverted Pyramid of Stars
def inverted_pyramid_of_stars():
    n = 5
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)

# Step 5: Full Diamond of Stars
def full_diamond_of_stars():
    n = 5
    # Upper part of the diamond
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)

# Step 6: Hollow Diamond of Stars
def hollow_diamond_of_stars():
    n = 5
    # Upper part of the hollow diamond
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' + '  ' * (i - 2) + ('* ' if i > 1 else ''))

    # Lower part of the hollow diamond
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' + '  ' * (i - 2) + ('* ' if i > 1 else ''))

# Step 7: Right-Angled Triangle with Numbers
def right_angled_triangle_numbers():
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Step 8: Inverted Right-Angled Triangle with Numbers
def inverted_right_angled_triangle_numbers():
    n = 5
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Step 9: Number Pyramid
def number_pyramid():
    n = 5
    num = 1
    for i in range(1, n + 1):
        print(' ' * (n - i), end="")
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# Step 10: Number Hourglass
def number_hourglass():
    n = 5
    # Upper part of the hourglass
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    # Lower part of the hourglass
    for i in range(2, n + 1):
        print(" " * (n - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Step 11: Hollow Right-Angled Triangle with Numbers
def hollow_right_angled_triangle_numbers():
    n = 5
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()

# Step 12: Right-Angled Triangle with Stars and Numbers
def right_angled_triangle_stars_numbers():
    n = 5
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == i:
                print(num, end=" ")
            else:
                print("*", end=" ")
        num += 1
        print()

# Step 13: Number Pyramid with Odd Numbers
def number_pyramid_odd():
    n = 5
    num = 1
    for i in range(1, n + 1):
        print(' ' * (n - i), end="")
        for j in range(i):
            print(num, end=" ")
            num += 2
        print()

# Step 14: Number Diamond
def number_diamond():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + str(i) * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + str(i) * i)

# Step 15: Pascal's Triangle
def pascals_triangle():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                print(1, end=" ")
            else:
                print(2, end=" ")
        print()

# Step 16: Number Spiral
def number_spiral():
    n = 4
    matrix = [[0] * n for _ in range(n)]

    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    for row in matrix:
        print(" ".join(map(str, row)))

# Step 17: Star Diamond with Numbers
def star_diamond_numbers():
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + str(i) + " " * (i - 1) + str(i))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + str(i) + " " * (i - 1) + str(i))

# Step 18: Number Spiral with Diagonal
def number_spiral_diagonal():
    n = 4
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        matrix[i][i] = i + 1

    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = n + 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            if matrix[top][i] == 0:
                matrix[top][i] = num
                num += 1
        top += 1
        for i in range(top, bottom + 1):
            if matrix[i][right] == 0:
                matrix[i][right] = num
                num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                if matrix[bottom][i] == 0:
                    matrix[bottom][i] = num
                    num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if matrix[i][left] == 0:
                    matrix[i][left] = num
                    num += 1
            left += 1

    for row in matrix:
        print(" ".join(map(str, row)))

# Step 19: Star Hourglass with Alternating Rows
def star_hourglass_alternating():
    n = 5
    for i in range(n):
        print(" " * i, end="")
        for j in range(n - i):
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(n - 2, -1, -1):
        print(" " * i, end="")
        for j in range(n - i):
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Testing all functions
if __name__ == "__main__":
    right_angled_triangle_stars()
    inverted_right_angled_triangle_stars()
    pyramid_of_stars()
    inverted_pyramid_of_stars()
    full_diamond_of_stars()
    hollow_diamond_of_stars()
    right_angled_triangle_numbers()
    inverted_right_angled_triangle_numbers()
    number_pyramid()
    number_hourglass()
    hollow_right_angled_triangle_numbers()
    right_angled_triangle_stars_numbers()
    number_pyramid_odd()
    number_diamond()
    pascals_triangle()
    number_spiral()
    star_diamond_numbers()
    number_spiral_diagonal()
    star_hourglass_alternating()
