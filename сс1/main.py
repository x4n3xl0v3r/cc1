import sys
import enum
from typing import Optional as Opt


class TriangleType(enum.StrEnum):
    TRI_REGULAR = "regular"
    TRI_ISOSCELES = "isosceles"
    TRI_EQUILATERAL = "equilateral"
    TRI_IMPOSSIBLE = "not_a_tri"
    ERROR = "error"


def get_triangle_name(t_type: TriangleType):
    if t_type == TriangleType.TRI_REGULAR:
        return "обычный"
    elif t_type == TriangleType.TRI_ISOSCELES:
        return "равнобедренный"
    elif t_type == TriangleType.TRI_EQUILATERAL:
        return "равносторонний"
    elif t_type == TriangleType.TRI_IMPOSSIBLE:
        return "не треугольник"


def invalid_input_data_handler():
    print("неизвестная ошибка")
    sys.exit(1)


def get_args() -> Opt[tuple[int, int, int]]:
    side_args = sys.argv[1:]
    if len(side_args) != 3:
        invalid_input_data_handler()

    try:
        return tuple(map(int, side_args))
    except ValueError:
        invalid_input_data_handler()


def is_equilateral(a: int, b: int, c: int) -> bool:
    return a == b == c


def is_isosceles(a: int, b: int, c: int) -> bool:
    return (a == b) or (a == c) or (b == c)


def is_impossible(a: int, b: int, c: int) -> bool:
    return (a + b < c) or (a + c < b) or (b + c < a) or (a <= 0) or (b <= 0) or (c <= 0)


def get_triangle_type(a: int, b: int, c: int) -> TriangleType:
    if is_impossible(a, b, c):
        return TriangleType.TRI_IMPOSSIBLE

    if is_equilateral(a, b, c):
        return TriangleType.TRI_EQUILATERAL

    if is_isosceles(a, b, c):
        return TriangleType.TRI_ISOSCELES

    return TriangleType.TRI_REGULAR


if __name__ == '__main__':
    a_side, b_side, c_side = get_args()
    tri_type = get_triangle_type(a_side, b_side, c_side)

    print(get_triangle_name(tri_type))
