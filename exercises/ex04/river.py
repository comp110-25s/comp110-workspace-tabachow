"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int  # Day of the river’s lifecycle you are modeling
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish if age > 3 and bears if age > 5."""
        new_fish: list[Fish] = self.fish
        new_bears: list[Bear] = self.bears
        for fish in self.fish:
            if fish.age > 3:
                new_fish.pop()
        for bear in self.bears:
            if bear.age > 5:
                new_bears.pop()
        return None

    def remove_fish(self, amount: int):
        """Removes amount many Fish from the River."""
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Each Bear eats 3 Fish if there are >= 5 Fish in river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Removes Bear from river if hunger_score < 0."""
        new_bears: list[Bear] = self.bears
        for bear in self.bears:
            if bear.hunger_score < 0:
                new_bears.pop()
        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring."""
        for i in range(0, (len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Each pair of Bears produces 1 offspring."""
        for i in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate 7 days of life in the river."""
        for i in range(7):
            self.one_river_day()
