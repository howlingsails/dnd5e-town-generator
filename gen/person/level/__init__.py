import random

def get_level(seed, class_name, is_mature):
    random.seed(str(seed))

    if class_name == 'Commoner':
        return 1
    
    level = 1
    while random.random() < 0.2 and level < 8:
        level += 1
    
    return level