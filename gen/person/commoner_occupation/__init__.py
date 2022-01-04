import json, random

with open('data/commoner-occupations.json', 'r') as open_file:
    OCCUPATIONS = json.load(open_file)

tot = 0
for occ in OCCUPATIONS:
    tot += 1 / OCCUPATIONS[occ]
    OCCUPATIONS[occ] = tot

def get_occupation(seed):
    random.seed(seed)

    r = random.random()
    print('r:'+str(r))
    for occ in OCCUPATIONS:
        print('occ:'+str(OCCUPATIONS[occ])+' occ:'+occ)
        if r < OCCUPATIONS[occ]:
            return occ
    else:
        return 'Commoner'