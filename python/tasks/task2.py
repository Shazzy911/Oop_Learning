# Problem 2: Multiple Inheritance (Easy-Medium)
# Task:

# Create two classes: Musician and Athlete.
# Musician has an attribute instrument and a method play_music().
# Athlete has an attribute sport and a method play_sport().
# Create a class TalentedPerson that inherits from both Musician and Athlete.
# Steps:

# Create classes Musician and Athlete.
# Define attributes and methods for each.
# Create a subclass TalentedPerson inheriting both Musician and Athlete.
# Ensure the TalentedPerson can use both play_music() and play_sport().

class Musician:
    def __init__(self, instrument):
        self.instrument = instrument

    def play_music(self):
        print(f"Musician is playing {self.instrument}")

class Athlete:
    def __init__(self,sport):
        self.sport = sport
    
    def play_sport(self):
        print(f"Athlete Like to play {self.sport}")


class TalentedPerson(Musician, Athlete):
    def __init__(self, instrument, sport):
        Musician.__init__(self, instrument)
        Athlete.__init__(self, sport)

person1 = TalentedPerson("Guitar", "Hockey")

person1.play_music()
person1.play_sport()