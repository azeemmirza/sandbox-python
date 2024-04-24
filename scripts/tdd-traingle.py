def area_of_triangle(base: float, height: float) -> float:
    """Calculates area of a triangle given in non-negative numbers"""

    # Checks if we have correct parameter type for base
    if type(base) not in [int, float]:
        raise TypeError()

    # Checks if we have correct parameter type for height
    if type(height) not in [int, float]:
        raise TypeError()

    if base < 0:
        raise ValueError()

    if height < 0:
        raise ValueError()

    return (base / 2) * height


test_data = [
    (2, 5),
    (2.5, 3.5),
    (True, 5),
    ('2.5', 5),
    (0, 6),
]

for data in test_data:
    print(f'The area of the triangle { data } is: { area_of_triangle(*data) }')
