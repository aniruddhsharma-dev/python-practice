# Write a function that counts vowels in a string.

# Solurion: 
def count_vowels(s):
    vowels = "aeiouAEIOU"        # List of vowels (both lowercase and uppercase)
    count = 0                    # Initialize count to 0
    for char in s:               # Iterate through each character in the string
        if char in vowels:       # Check if the character is a vowel
            count += 1           # Increment the count if it is a vowel
    return count
    
print(count_vowels("Aniruddh Sharma"))