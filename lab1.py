import cmath

def solve_cubic_equation(a, b, c, d):
    discriminant1 = b ** 2 - 3 * a * c
    discriminant2 = 2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d
    C = ((discriminant2 + cmath.sqrt(discriminant2 ** 2 - 4 * discriminant1 ** 3)) / 2) ** (1/3)
    if C != 0:
        x1 = (-1 / (3 * a)) * (b + C + discriminant1 / C)
    else:
        x1 = (-1 / (3 * a)) * (b + discriminant1 ** (1/3))

    x2 = (-1 / (3 * a)) * (b + cmath.exp(2j * cmath.pi / 3) * C + discriminant1 / (C * cmath.exp(2j * cmath.pi / 3)))
    x3 = (-1 / (3 * a)) * (b + cmath.exp(4j * cmath.pi / 3) * C + discriminant1 / (C * cmath.exp(4j * cmath.pi / 3)))

    return x1, x2, x3

# Ввод коэффициентов с клавиатуры
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = float(input("Введите коэффициент d: "))

# Решение уравнения
solutions = solve_cubic_equation(a, b, c, d)

# Вывод решений
print("Корни кубического уравнения:")
for idx, solution in enumerate(solutions, start=1):
    print(f"Корень {idx}: {solution}")