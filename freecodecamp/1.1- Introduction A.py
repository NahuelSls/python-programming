'''
An example code with python that is going to be explained in the different lessons that
freecodecamp has for this language.
In other words, it's an example that they used in different videos for explaining some important things about Python.
'''

# In general, this code count the common word that the user has in a file that it was introduced at the beggining of the simulation

# The user can introduce the name of the file and then the program open it
name = input('Enter file name: ')
File = open(name, 'r')

# Counts the number that each word appears in the file introduced at the beginning
counts = dict()
for line in File:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
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

