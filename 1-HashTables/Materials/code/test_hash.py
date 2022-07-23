class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)


p = Point(3, 5, 7)
q = Point(3, 5, 9)
r = Point(3, 5, 7)
print(hash(p) == hash(r))
print(p == r)