import time

class AnimalShelter:
  def __init__(self):
    animalTypes = ['cat', 'dog']
    self.animals = {}
    for animal in animalTypes:
      self.animals[animal] = []

  def enqueue(self, animal):
    if not animal in self.animals:
      self.animals[animal] = Animal('name', animalType, time.time())


if __name__ == '__main__':
  pass
