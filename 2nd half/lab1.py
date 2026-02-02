from typing import Literal, override
from collections.abc import Iterator


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y))
    
    @override
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def orientation(p: Point, q: Point, r: Point) -> Literal[0, 1, 2]:
    val: float = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    
    # через веркторное произведение

    if val == 0:
        return 0
    
    return 1 if val > 0 else 2


def distance(p: Point, q: Point) -> float:
    return (q.x - p.x) ** 2 + (q.y - p.y) ** 2


def jarvis_march(points: list[Point]) -> list[Point]:
    n: int = len(points)

    if n < 3:
        return []

    leftmost = 0

    for i in range(1, n):
        if points[i].x < points[leftmost].x or (
           points[i].x == points[leftmost].x and \
           points[i].x < points[leftmost].y
        ):
            leftmost = i

    hull: list[Point] = []
    p: int = leftmost

    while True:
        hull.append(points[p])

        q: int = (p + 1) % n

        for i in range(n):
            if orientation(p=points[p], q=points[i], r=points[q]) == 2:
                q = i

            elif orientation(p=points[p], q=points[i], r=points[q]) == 0:
                if distance(p=points[p], q=points[i]) > distance(p=points[p], q=points[q]):
                    q: int = i

        p: int = q

        if p == leftmost:
            break

    if len(hull) < 3:
        return []

    return hull


def read_points() -> list[Point]:
    points: list[Point] = []

    try:
        n: int = int(input("Enter amount of points: "))
        if n <= 0:
            print("Amount of points must positive")
            return []

        print("Enter points coordinates in format (x y)\n")

        for i in range(n):

            while True:
                try:
                    coords: list[str] = input(f"Point {i + 1}: ").strip().split()
                    
                    if len(coords) != 2:
                        print("Must enter 2 numbers")
                        continue

                    x, y = map(float, coords)
                    points.append(Point(x, y))
                    
                    break

                except ValueError:
                    print("Enter only numbers!")

    except ValueError:
        print("Amount of nubers must be real!")
        return []

    return points


def main() -> None:
    print("НАХОЖДЕНИЕ ВЫПУКЛОЙ ОБОЛОЧКИ МНОЖЕСТВА ТОЧЕК")
    print("Алгоритм: Джарвиса")

    points: list[Point] = read_points()

    if not points:
        return
    
    print()
    print("Points:", [point for point in points], "\n")

    hull: list[Point] = jarvis_march(points)

    if hull:
        print("Выпуклая оболочка существует!")
        print(f"Количество вершин оболочки: {len(hull)}")
        print("Вершины оболочки в порядке обхода против часовой стрелки:")

        for i, p in enumerate(hull, 1):
            print(f"{i}. {p}")


    else:
        print("Выпуклая оболочка НЕ существует!")
    
        if len(points) < 3:
            print("Причина: точек меньше 3")

        else:
            print("Причина: все точки коллинеарны")

    print("=" * 50)


def example_usage():
    points_1: list[tuple[float, float]] = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0), (1, 0.5)]
    
    example_points_exist: list[Point] = [Point(x, y) for x, y in points_1]
    print("Точки:", example_points_exist)

    hull = jarvis_march(example_points_exist)
    
    if hull:
        print("Оболочка найдена:", hull)
    else:
        print("Оболочка не найдена")

    print("\n" + "-" * 30)

    points_2: list[tuple[float, float]] = [(0, 0), (1, 1), (2, 2), (3, 3)]
    colinear_points: list[Point] = [Point(x, y) for x, y in points_2]
    
    print("Коллинеарные точки:", colinear_points)

    hull = jarvis_march(colinear_points)
    if hull:
        print("Оболочка найдена:", hull)
    else:
        print("Оболочка не найдена - все точки коллинеарны")


if __name__ == "__main__":

    # main()
    example_usage()
