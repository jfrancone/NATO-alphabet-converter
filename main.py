import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#Use dictionary comprehension, don't use to_dict function

data = pandas.read_csv('nato_phonetic_alphabet.csv')
#print(data)

#Format a dictionary in this format from the dataframe
#{new_key:new_value for (index, row) in data_frame.iterrows() if test}
dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Please enter a word: ").upper()
letter_list = [letter for letter in user_input]
#print(letter_list)

output = [dict[letter] for letter in letter_list]
print(output)





