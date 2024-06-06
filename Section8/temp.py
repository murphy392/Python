acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition?\n')
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
# Write the acronym and definition to the file

