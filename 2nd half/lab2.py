from dataclasses import dataclass
from typing import Optional, Tuple, List
import math

@dataclass
class Point:
    x: float
    y: float

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

@dataclass
class Line:
    a: float
    b: float
    c: float
    
    @staticmethod
    def from_points(p1: Point, p2: Point) -> 'Line':
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = p2.x * p1.y - p1.x * p2.y
        return Line(a, b, c)

@dataclass
class Segment:
    p1: Point
    p2: Point
    
    def to_line(self) -> Line:
        return Line.from_points(self.p1, self.p2)

@dataclass
class Circle:
    center: Point
    radius: float

delta = 1e-10

def line_line_intersection(l1: Line, l2: Line) -> Optional[Point]:
    det = l1.a * l2.b - l2.a * l1.b
    
    if abs(det) < delta:
        return None
    
    x = (l1.b * l2.c - l2.b * l1.c) / det
    y = (l2.a * l1.c - l1.a * l2.c) / det
    
    return Point(x, y)


def line_segment_intersection(line: Line, segment: Segment) -> Optional[Point]:
    seg_line = segment.to_line()
    
    intersection = line_line_intersection(line, seg_line)
    
    if intersection is None:
        return None
    
    x_min = min(segment.p1.x, segment.p2.x)
    x_max = max(segment.p1.x, segment.p2.x)

    y_min = min(segment.p1.y, segment.p2.y)
    y_max = max(segment.p1.y, segment.p2.y)
    
    if (x_min - delta <= intersection.x <= x_max + delta and 
        y_min - delta <= intersection.y <= y_max + delta):
        return intersection
    
    return None


def segments_intersection(s1: Segment, s2: Segment) -> Optional[Point]:
    l1 = s1.to_line()
    l2 = s2.to_line()
    
    intersection = line_line_intersection(l1, l2)
    
    if intersection is None:
        return None
    
    def point_on_segment(p: Point, s: Segment) -> bool:
        x_min = min(s.p1.x, s.p2.x)
        x_max = max(s.p1.x, s.p2.x)
        y_min = min(s.p1.y, s.p2.y)
        y_max = max(s.p1.y, s.p2.y)
        
        return (x_min - delta <= p.x <= x_max + delta and 
                y_min - delta <= p.y <= y_max + delta)
    
    if (point_on_segment(intersection, s1) and 
        point_on_segment(intersection, s2)):
        return intersection
    
    return None

def line_circle_intersection(line: Line, circle: Circle) -> List[Point]:
    points = []
     
    if abs(line.b) > delta:
        k = -line.a / line.b
        b = -line.c / line.b

        cx, cy, r = circle.center.x, circle.center.y, circle.radius
        
        A = 1 + k ** 2
        B = 2 * (k * (b - cy) - cx)
        C = cx ** 2 + (b - cy) ** 2 - r ** 2
        
        discriminant = B ** 2 - 4 * A * C
        
        if discriminant < -delta:
            return []

        elif abs(discriminant) < delta:
            x = -B / (2 * A)
            y = k * x + b
            points.append(Point(x, y))

        else:
            sqrt_d = math.sqrt(max(0, discriminant))
            x1 = (-B + sqrt_d) / (2 * A)
            y1 = k * x1 + b
            
            x2 = (-B - sqrt_d) / (2 * A)
            y2 = k * x2 + b
            
            points.append(Point(x1, y1))
            points.append(Point(x2, y2))
    
    else:
        x = -line.c / line.a
        cx, cy, r = circle.center.x, circle.center.y, circle.radius
        
        dx = x - cx
        d = r** 2 - dx ** 2
        
        if d < -delta:
            return []

        elif abs(d) < delta:
            points.append(Point(x, cy))

        else:
            sqrt_d = math.sqrt(max(0, d))

            points.append(Point(x, cy + sqrt_d))
            points.append(Point(x, cy - sqrt_d))
    
    return points


def segment_circle_intersection(segment: Segment, circle: Circle) -> List[Point]:
    line = segment.to_line()
    all_intersections = line_circle_intersection(line, circle)
    
    result = []

    x_min = min(segment.p1.x, segment.p2.x)
    x_max = max(segment.p1.x, segment.p2.x)

    y_min = min(segment.p1.y, segment.p2.y)
    y_max = max(segment.p1.y, segment.p2.y)
    
    for p in all_intersections:
        if (x_min - delta <= p.x <= x_max + delta and 
            y_min - delta <= p.y <= y_max + delta):
            result.append(p)
    
    return result


def circles_intersection(c1: Circle, c2: Circle) -> List[Point]:
    points = []
    
    cx1, cy1, r1 = c1.center.x, c1.center.y, c1.radius
    cx2, cy2, r2 = c2.center.x, c2.center.y, c2.radius
    
    dx = cx2 - cx1
    dy = cy2 - cy1

    d = math.sqrt(dx*dx + dy*dy)
    
    if d > r1 + r2 + delta or d < abs(r1 - r2) - delta or d < delta:
        return points
    
    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(max(0, r1*r1 - a*a))
    
    cx = cx1 + a * dx / d
    cy = cy1 + a * dy / d
    
    if abs(h) < delta:
        points.append(Point(cx, cy))

    else:
        rx = -dy * (h / d)
        ry = dx * (h / d)
        
        points.append(Point(cx + rx, cy + ry))
        points.append(Point(cx - rx, cy - ry))
    
    return points


def orientation(p: Point, q: Point, r: Point) -> int:
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    
    if abs(val) < delta:
        return 0

    return 1 if val > 0 else 2

def point_in_triangle(p: Point, A: Point, B: Point, C: Point) -> bool:
    def sign(p1: Point, p2: Point, p3: Point) -> float:
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)
    
    d1 = sign(p, A, B)
    d2 = sign(p, B, C)
    d3 = sign(p, C, A)
    
    has_neg = (d1 < -delta) or (d2 < -delta) or (d3 < -delta)
    has_pos = (d1 > delta) or (d2 > delta) or (d3 > delta)
    
    return not (has_neg and has_pos)

def triangles_from_points(points: List[Point]) -> List[Tuple[Point, Point, Point]]:
    triangles = []
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if orientation(points[i], points[j], points[k]) != 0:
                    triangles.append((points[i], points[j], points[k]))
    
    return triangles

def find_nested_triangles(points: List[Point]) -> List[Tuple[Tuple[Point, Point, Point], 
                                                          Tuple[Point, Point, Point]]]:

    triangles = triangles_from_points(points)
    nested_pairs = []
    
    for i, t1 in enumerate(triangles):
        A1, B1, C1 = t1
        for j, t2 in enumerate(triangles):
            if i == j:
                continue
            
            A2, B2, C2 = t2
            
            if (point_in_triangle(A2, A1, B1, C1) and
                point_in_triangle(B2, A1, B1, C1) and
                point_in_triangle(C2, A1, B1, C1)):
                nested_pairs.append((t1, t2))
    
    return nested_pairs


def solve_problem(points: List[Point]) -> bool:
    nested = find_nested_triangles(points)
    return len(nested) > 0


if __name__ == "__main__":
    points = [
        Point(0, 0),
        Point(10, 0),
        Point(5, 8.66),
        Point(5, 4),
        Point(3, 2),
        Point(7, 2)
    ]
    
    result = solve_problem(points)
    print(f"Есть ли вложенные треугольники? {result}")
    
    if result:
        nested = find_nested_triangles(points)
        print(f"Найдено пар вложенных треугольников: {len(nested)}")
        for outer, inner in nested[:3]:
            print(f"Внешний: {outer}")
            print(f"Внутренний: {inner}")
            print()
