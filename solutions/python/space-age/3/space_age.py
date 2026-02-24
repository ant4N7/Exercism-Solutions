class SpaceAge:

    ORBITAL_PERIOD = {'mercury': 0.2408467, 
                      'venus': 0.61519726, 
                      'earth': 1.0, 
                      'mars': 1.8808158, 
                      'jupiter': 11.862615, 
                      'saturn': 29.447498, 
                      'uranus': 84.016846, 
                      'neptune': 164.79132}

    def __init__(self, seconds):
        self.earth_years = seconds / 31557600
        for planet, OP in SpaceAge.ORBITAL_PERIOD.items():
            setattr(self, f'on_{planet}', lambda OP=OP: round(self.earth_years / OP, 2))
