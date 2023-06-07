# Create a Python program that reads a text file and counts the occurrences of each
# word using a dictionary. The program should print the words and their counts.

def count_occurrences(filename):
    number_of_words = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in number_of_words:
                    number_of_words[word] += 1
                else:
                    number_of_words[word] = 1
    
    for word, count in number_of_words.items():
        print(f"{word}: {count}")

# nombre del archivo al que se le contarán las ocurrencias de palabras
filename = "documento.txt"

# llamado de la función para contar ocurrencias de palabras
count_occurrences(filename)
