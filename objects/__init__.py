from objects.village import Village as VObject
from config import SECRET as PASSWORD
import time
from gen import world, worlds, religion, state,burg
MANAGER = {}
TIMES = {}




def Worlds():
    return worlds.getWorlds()


def World(world_name):
    return world.getWorld(world_name)


def Religion(world, religion_i):
    return religion.getReligion(world, religion_i)


def State(world, state_i):
    return state.getState(world, state_i)

def Burg(world,burg_i):
    return burg.getBurg(world,burg_i)


def Village(name, size):
    seed = f"{name}-{size}"
    TIMES[seed] = time.time()

    if seed not in MANAGER:
        MANAGER[seed] = VObject(name, size, PASSWORD)

    return MANAGER[seed]


def clean_tree():
    # Clean memory: remove villages that haven't been inspected for a while.
    to_remove = []

    for seed in MANAGER:
        if (time.time() - TIMES[seed]) > (30):
            to_remove.append(seed)

    for seed in to_remove:
        print(f'Removing {seed}!')
        del MANAGER[seed]
        del TIMES[seed]
