'''
An example code with python that is going to be explained in different lessons that
"FreeCodeCamp - Learning Python" has for this language.
In other words, it's an example that they used in different videos for explaining some important things about Python.
'''

# In general, this code count the common word that the user has in a file that it was introduced at the beggining of the simulation

# The user can introduce the name of the file and then the program open it.
name = input('Enter file name: ') # In this case: "file.txt"
File = open(name) # opens the file saved in the variable "name"

# Counts the number that each word appears in the file introduced at the beginning
counts = dict() # Creates a dictionary and saved it as "count"

for line in File: # starts a loop to read each line of the file
    words = line.split() #split the line to read each word
    for word in words: # starts another loop for each word in the line
        counts[word] = counts.get(word, 0) + 1 # Search in the dict() function if there are the same word saved in "word"
#print(counts)

# The pogram choose the most common word of the file
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#Finally, prints the word that is more common and the number of times that appears in the whole text of the file
print(bigword, bigcount)

