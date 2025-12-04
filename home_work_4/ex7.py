class Grass:
    def __init__(self, nutrition):
        self.nutrition = nutrition

class Herbivore:
    def __init__(self, hunger_level=10):
        self.hunger_level = hunger_level
    
    def eat(self, grass: Grass):
        if self.hunger_level > 0:
            self.hunger_level = max(0, self.hunger_level - grass.nutrition)
            return f"Животное поело траву. Уровень голода: {self.hunger_level}"
        else:
            return "Животное не голодно"
        