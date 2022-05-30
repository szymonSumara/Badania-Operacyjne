class Road:
    def __init__(self, first_station, second_station, time_cost, fuel_cost):
        self.first_station = first_station
        self.second_station = second_station
        self.time_cost = time_cost
        self.fuel_cost = fuel_cost

    def __eq__(self, other):
        if (
            self.first_station != other.first_station
            and self.first_station != other.second_station
        ):
            return False
        if (
            self.second_station != other.first_station
            and self.second_station != other.second_station
        ):
            return False
        return True

    def __repr__(self):
        return str(self.first_station) + " " + str(self.second_station)

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
