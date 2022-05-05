import json
import yaml

with open("csvExample.csv", 'r') as f:
    headlines = f.readline().strip('\n').split(',')
    people = []
    for line in f:
        data = line.strip('\n').split(',')
        person = {headlines[i]: data[i] for i in range(4)}
        people.append(person)

with open("jsonOutput.json", 'w') as f:
    f.write('[' + '\n')
    for i in range(len(people) - 1):
        json.dump(people[i], f, indent=2)
        f.write(',\n')
    json.dump(people[-1], f, indent=2)
    f.write(']' + '\n')

with open("jsonOutput.json", 'r') as f:
    # dictionaries = json.load(f)
    dictionaries= yaml.safe_load(f)

with open("csvOutput.csv", 'w') as f:
    headlines = list(dictionaries[0].keys())
    f.write(','.join(headlines))
    f.write('\n')
    for dictionary in dictionaries:
        values = list(dictionary.values())
        f.write(','.join(values))
        f.write('\n')
