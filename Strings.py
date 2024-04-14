
import text_utils as alias_text

def strings():
    s = input("Introduce the word that you want to work with: ")
    decision = input("What do you want to do with the string? Enter 1 to reverse, 2 to capitalize: ")
    if decision == "1":
        s = alias_text.reverse_string(s)
        print(s)
    elif decision == "2":
        s = alias_text.capitalize_string(s)
        print(s)
    else:
        print("Invalid option. Please enter 1 to reverse the string or 2 to capitalize it.")

strings()

#Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.