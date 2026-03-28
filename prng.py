#generates psuedo-random number

import time
import random

while True:
    time.sleep(1.0)

    with open("prng-service.txt", "r") as f:
        line = f.read().strip()

    if line == "run":
        number = random.randint(1, 3) #images
        
        with open("prng-service.txt", "w") as f:
            f.write(str(number))