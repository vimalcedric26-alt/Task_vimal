from random import randint
word_given=['python','javascript','java','automation','pytest','guvi','selenium']
my_choice=input("Guess the word from the list:")
computer_choice=word_given[randint(0,len(word_given)-1)]
print(f"Computer chose: {computer_choice}")
if my_choice==computer_choice:
    print("Your choice is correct")
else:
    print("Your choice is incorrect")