'''This script reads a list of people and the courses they take and then 
grets each person for the pSciComp course
'''

# This initialises the list of people and their couses -> Data pillar
people = [
  {"name": "Jon Doe", "courses": ["math1", "pSciComp", "physics1"]},
  {"name": "Leonardo Da Vinci", "courses": ["math99", "cosmology7"]},
  {"name": "Mona Lisa", "courses": ["linalg3", "pSciComp"]},
]
course = 'pSciComp' #This specifies the course we are interested in -> config
greetings = [] # initisalises the list -> Code

# This is code that generates greetings -> Code
for person in people:
    if course in person['courses']: #Code and Data, where person['courses'] is data
        greetings.append(f"Hello {person['name']}\n")

# Here we save the text file with the greetings -> SRC
#The path to saving is ->ENV
with open('data/final/greeting.txt', 'w') as f:
    f.writelines(greetings)
