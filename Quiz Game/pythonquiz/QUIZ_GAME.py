def playing_quiz():
   total_questions = 0
   correct_answered = 0
   wrong_answered = 0
   total_questions +=1
   answer = input("What does CPU stand For?")
   if answer == "central processing unit":
    print('Correct!')
    correct_answered +=1
   else:
    print("Incorrect!")
    wrong_answered +=1

   total_questions +=1
   answer = input("What does RAM stand For?")
   if answer == "random acess memory":
    print('Correct!')
    correct_answered+=1
   else:
    print("Incorrect!")
    wrong_answered+=1

   total_questions +=1
   answer = input("What does ROM stand For?")
   if answer == "read only  memory":
    print('Correct!')
    correct_answered+=1
   else:
    print("Incorrect!")
    wrong_answered+=1

   total_questions +=1
   answer = input("What does GPU stand For?")
   if answer == "graphics processing unit":
    print('Correct!')
    correct_answered+=1
   else:
    print("Incorrect!")
   wrong_answered+=1


   print('Total Number of answers',total_questions)
   print('Correct answers ',correct_answered)
   print('Wrong Answers',wrong_answered)

   



def main():
 print("Welcome to my computer quiz!")
    
 while True:
        playing = input("Do you want to play? (yes/no) ").lower()
        if playing == "yes":
            print("Okay! Let's play :)")
            playing_quiz()
        elif playing == "no":
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

main() 

   

