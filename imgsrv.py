#converts image path

import time

while True:
    time.sleep(1.0)
    
    with open("image-service.txt", "r") as f:
        content = f.read().strip()
    
    if content.isdigit():
        image_path = f"pizza-images/{content}.jpg" #image path
        
        with open("image-service.txt", "w") as f:
            f.write(image_path)