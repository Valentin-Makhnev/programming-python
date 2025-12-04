class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()
    
    def _normalize(self):
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        
        while self.hours >= 24:
            self.hours -= 24
    
    def add_hour(self):
        self.hours += 1
        self._normalize()
    
    def add_minute(self):
        self.minutes += 1
        self._normalize()
    
    def add_second(self):
        self.seconds += 1
        self._normalize()
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def __add__(self, other):
        total_seconds = (
            self.hours * 3600 + self.minutes * 60 + self.seconds +
            other.hours * 3600 + other.minutes * 60 + other.seconds
        )
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return Clock(hours % 24, minutes, seconds)
    