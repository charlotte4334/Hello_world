
import os
from collections.abc import Collection
from types import SimpleNamespace


def create_greetings(people, output_dir, cfg):
    greetings = [] # initisalises the list -> Code

    course= cfg.course

    # This is code that generates greetings -> Code
    for person in people:
        if course in person[cfg.courses]: #Code and Data, where person['courses'] is data
            greetings.append(f"Hello {person[cfg.name]}\n")

    # Here we save the text file with the greetings -> SRC
    #The path to saving is ->ENV
    output_path = os.path.join(output_dir, 'greeting.txt')
    with open(output_path, 'w') as f:
        f.writelines(greetings)
    return output_path