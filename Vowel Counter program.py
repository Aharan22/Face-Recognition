text = input("text: ")

count = 0


for character in text:
    if (character in "aAEeiIoOuU"):
        count +=1
        print("Vowel Count:",count)
    



text = input("Text: ")  # Prompt the user to input a string
count = 0  # Initialize the vowel counter

# Loop through each character in the input string
for character in text:
    if character in "aAeEiIoOuU":  # Check if the character is a vowel (case insensitive)
        count += 1  # Increment the counter if it's a vowel

# Print the total count of vowels
print("Count:", count)

def count_vowels(text):
      
    count=0
    for character in text:
        if character in "aAeEiIoOuU":  # Check if the character is a vowel (case insensitive)
            count += 1  # Increment the counter if it's a vowel
            return count
        text = input("Text: ")
        
        count = count_vowels(text)
        print("Count:", count)
        
    

