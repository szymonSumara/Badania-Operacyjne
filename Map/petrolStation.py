class PetrolStation:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __str__(self):
        return str(self.cost)  # + "x: " +str(self.x)+ " y: " + str(self.y)

    def __repr__(self):
        return str(self.cost)  # + "x: " +str(self.x)+ " y: " + str(self.y)

    def __eq__(self, other):
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.cost != other.cost:
            return False
        return True

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
