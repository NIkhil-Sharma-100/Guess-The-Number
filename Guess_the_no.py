from random import randint

secret_number = randint(1,100)
attempt = 0

print("Welcome To \"Guess The Number\"")

while True:
    try:
        guess = int(input("Number is : "))
    except ValueError:
        print("❌ Please enter valid input")    

    attempt +=1

    if  guess == secret_number:
        print(f"Congratulation!! You Guessed right in {attempt} attempts")


        try:
            with open("highscore.txt","r") as file:
                content = (file.read().strip())
                highscore = int(content) if content else None

        except FileNotFoundError:
            highscore = None   

        if highscore is None or attempt < highscore:
            with open("highscore.txt", "w") as file:
                file.write(str(attempt))
            print(f"OH! New highscore : {attempt}")
                 
                
        break

    elif guess < secret_number:
        print("Wrong , Go high")

    elif guess > secret_number:
        print("Worong , Go low")
        
    else:
        print("Nah!! Enter Valid Input")        

    