# Project Description:
1) The project is meant to generate a random string of letters, numbers, and symbols.
2) There is one file named "documentation-text" which has a description of "random" module.
3) First of all we imported ramdom module
4) We used a variable "wordlist" which is empty list and a variable "symbols" in which special char which will be included to generate random password.
5) We used "readlines()" method this will basically return a list containing each line in the file as a list item and also we used "with" statement which works with the open() function to open a file.
6) Here comes the logic part :
- The code then iterates through each line, splitting it into words using split().
- for every item in wordlist, if that item has five or more characters, it will append that character to symbol list (symbols).
7) The code will take the words from the file i.e. "documentation-text" and create a list of all capitalized words.
8) Then a random choice from the list is made using "random.choice" function", followed "s_char" to represent special char, followed by adding a "digit" between 20 and 199 which will randomly choose the digits.
10) Then we declared a variable "combine" which will include word + special char + digits. 
11) The code will generate a random word with a randomly chosen symbol from the list of symbols, in the file "documentation-text.txt".

## Module and Functions Used:
1) Random Module : The Python Random module is a built-in module for generating random integers in Python
2) random.choice method : The random.choice() function selects an item from a non-empty series at random. 
3) random.randint : The random.randint() function generates a random integer from the range of numbers supplied.

