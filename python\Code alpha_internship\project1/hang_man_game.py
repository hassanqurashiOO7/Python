
import random

print("-------WELCOME TO HANGMAN GAME-------")

words = ['apple', 'banana', 'orange', 'pineapple']
word = random.choice(words)

guess = []
wrong_guess_count = 0
max_guess_count = 6




# 🔁 Game Loop
while wrong_guess_count < max_guess_count:
    user = input("\nEnter a letter: ").lower()

    if len(user) != 1:
        print("Only one letter allowed")
        continue

    if not user.isalpha():
        print("Only alphabets allowed")
        continue

    if user in guess:
        print("Already guessed")
        continue

    guess.append(user)

    if user in word:
        print("✅ Correct guess")
    else:
        print("❌ Wrong guess")
        wrong_guess_count += 1

   

    # 🧠 Display word
    display = ""
    for letter in word:
        if letter in guess:
            display += letter
        else:
            display += "_"

    print("Word:", display)
    print("Lives left:", max_guess_count - wrong_guess_count)

    # 🏆 Win condition
    if "_" not in display:
        print("\n🎉 You guessed the word:", word)
        break


# 💀 Game Over
if wrong_guess_count == max_guess_count:
    print("\n💀 Game Over! The word was:", word)
