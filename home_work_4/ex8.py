class Water:
    def __init__(self):
        self.name = "Вода"
    
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        elif isinstance(other, Metal):
            return Rust()
        return None

class Air:
    def __init__(self):
        self.name = "Воздух"
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Metal):
            return Corrosion()
        return None

class Fire:
    def __init__(self):
        self.name = "Огонь"
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Metal):
            return MeltedMetal()
        return None

class Earth:
    def __init__(self):
        self.name = "Земля"
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Metal):
            return Ore()
        return None

class Metal:
    def __init__(self):
        self.name = "Металл"
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Rust()
        elif isinstance(other, Air):
            return Corrosion()
        elif isinstance(other, Fire):
            return MeltedMetal()
        elif isinstance(other, Earth):
            return Ore()
        elif isinstance(other, Metal):
            return Alloy()
        return None

class Storm:
    def __init__(self):
        self.name = "Шторм"

class Steam:
    def __init__(self):
        self.name = "Пар"

class Mud:
    def __init__(self):
        self.name = "Грязь"

class Lightning:
    def __init__(self):
        self.name = "Молния"

class Dust:
    def __init__(self):
        self.name = "Пыль"

class Lava:
    def __init__(self):
        self.name = "Лава"

class Rust:
    def __init__(self):
        self.name = "Ржавчина"

class Corrosion:
    def __init__(self):
        self.name = "Коррозия"

class MeltedMetal:
    def __init__(self):
        self.name = "Расплавленный металл"

class Ore:
    def __init__(self):
        self.name = "Руда"

class Alloy:
    def __init__(self):
        self.name = "Сплав"

elements = [Water(), Air(), Fire(), Earth(), Metal()]

for i, elem1 in enumerate(elements):
    for elem2 in elements[i:]:
        result = elem1 + elem2
        if result:
            print(f"{elem1.name} + {elem2.name} = {result.name}")
        else:
            print(f"{elem1.name} + {elem2.name} = Нет результата")
    print()

water = Water()
air = Air()
fire = Fire()
earth = Earth()
metal = Metal()

result1 = water + air
print(f"Вода + Воздух = {result1.name if result1 else 'None'}")

result2 = fire + earth
print(f"Огонь + Земля = {result2.name if result2 else 'None'}")

result3 = water + metal
print(f"Вода + Металл = {result3.name if result3 else 'None'}")

result4 = metal + metal
print(f"Металл + Металл = {result4.name if result4 else 'None'}")
