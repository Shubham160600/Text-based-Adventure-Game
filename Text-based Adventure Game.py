print("You are in a dark forest.")
choice = input("Go left or right? ").lower()

if choice == "left":
    print("You found a river. You win!")
elif choice == "right":
    print("You were eaten by a bear. Game over.")
else:
    print("Invalid choice. Game over.")
