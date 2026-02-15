from pprint import pprint


INITIAL_FUEL = 10


class Spaceship:
    def __init__(self, name: str, type: str, fuel_type: str, fuel = INITIAL_FUEL):
        self.name = name
        self.type = type
        self.fuel_type = fuel_type
        self.fuel = fuel

    def refuel(self, amount: int) -> None:
        self.fuel += amount
        print(f"{self.name} has been refueled with {amount}. Current fuel: {self.fuel}")

    def __self_destruct(self) -> None:
        print(f"{self.name} is self-destructing!")
        self.fuel = 0

    @classmethod
    def create_cargo_ship(cls, name: str) -> 'Spaceship':
        return cls(name, "Cargo", "Standard Fuel", 7)

    @classmethod
    def create_battle_ship(cls, name: str) -> 'Spaceship':
        return cls(name, "Battle", "High-Grade Fuel", 50)

    def __str__(self) -> str:
        return f"{self.name} ({self.type}) - Fuel: {self.fuel} ({self.fuel_type})"
    
    def __repr__(self) -> str:
        return f"Spaceship(name='{self.name}', type='{self.type}', fuel_type='{self.fuel_type}', fuel={self.fuel})"

    def __lt__(self, other: 'Spaceship') -> bool:
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.fuel < other.fuel


if __name__ == "__main__":
    cargo_ship = Spaceship.create_cargo_ship("CargoMaster")
    battle_ship = Spaceship.create_battle_ship("Warrior")

    # print(str(cargo_ship))
    # print(repr(cargo_ship))
    pprint(dir(cargo_ship))
