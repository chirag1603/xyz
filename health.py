import random
health = 50
difficulty = 4
potio_health = int(random.randint(25,50) / difficulty)
health = health + potio_health
print(health)
