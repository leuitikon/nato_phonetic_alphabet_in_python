import pandas

# Load the NATO phonetic alphabet CSV data into a pandas DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1: Create a dictionary in this format {"A": "Alfa", "B": "Bravo", ...}
# Iterate through DataFrame rows using iterrows() to build the phonetic dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
# Prompt the user to enter a word and convert all letters to uppercase for matching
word = input("Enter a word: ").upper()

# Use list comprehension to look up each letter in the phonetic dictionary
output_list = [phonetic_dict[letter] for letter in word]

# Print the final list of phonetic code words
print(output_list)