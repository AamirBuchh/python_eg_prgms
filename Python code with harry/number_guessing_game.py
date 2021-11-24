# guessing game
hd_no = 18 # hidden no
print("\n->You have 9 guesses to get the number right and be really careful with your choices.\n->For a wrong no you will be given a hint weather the no is less than or greater that the wrong no.\n->Number in the range of 0-50\n->All the best.\n\n")
gu_count = 0 #guess count
guesses = 3
while(gu_count<=guesses):
    u_ip = int(input("\nEnter the guess : "))#user input
    gu_count = gu_count+1
    if u_ip == hd_no:
        print(f"***Congrats!!!You guessed the right no({u_ip}) in {gu_count} guesses***\n")
        break
    elif gu_count>guesses:
        print("*"*11)
        print("*Game Over*")
        print("*"*11)
        rtry = input("\nWould you like to retry(Y/N) : ")
        if rtry == "Y" or rtry == "y":
            gu_count = 0
            continue
        elif(rtry=="N" or rtry=="n"):
            break
        else:
            break
    else:
        print(f"Try again.\nGuesses remaining : {guesses-gu_count}\n")
        if u_ip>hd_no:
            print("Entered no is greater\n")
        else:
            print("Entered no is lesser\n")
    
    

