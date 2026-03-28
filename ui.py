import time

while True:
    print("\n--Pizza Generator--")
    user_input = input("Enter '1' to generate a pizza image or '2' to exit: ")

    if user_input == "1": #user enters 1
        with open("prng-service.txt", "w") as f:
            f.write("run")
        
        time.sleep(2.0)
        
        with open("prng-service.txt", "r") as f:
            number = f.read().strip()
            
        with open("image-service.txt", "w") as f:
            f.write(number)
            
        time.sleep(2.0)
        
        with open("image-service.txt", "r") as f:
            image_path = f.read().strip()
            print(f"Your pizza is ready!😋 Path: {image_path}")

    elif user_input == "2": #user enters 2
        print("\nThanks for generating! 🍕🎉\n")
        break