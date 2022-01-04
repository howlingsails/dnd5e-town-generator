import random, json


with open('data/races.json', 'r') as open_file:
    __obj = json.load(open_file)
    
    RACE_BY_WEIGHT = {race: __obj[race]['density'] for race in __obj}
    TOTAL = sum(RACE_BY_WEIGHT.values())

def raceFromParam(seed):
    races = __obj;
    if '-' in seed[1]:
        raceGoal =seed[1].split('-')[1]
        for race in races:
            if race == raceGoal:
                return race 


def race(seed):
    result = raceFromParam(seed)
    if result is None:
        random.seed(str(seed))
        r = random.randint(1, TOTAL)
        for race in RACE_BY_WEIGHT:
            r = r - RACE_BY_WEIGHT[race]
            if r <= 0:
                return race
    return result;
