# Copyright 2022, William L. Nortman, All Rights Reserved
def getState(world, state_i):
    states = world["states"]
    state = states[int(state_i)]
    burgs = world['burgs']
    for burg in burgs:
        if 'state' in burg:
            if burg['state'] is not None:
                # print(str(burg['state'])+" ? " + state_i)
                burgState = int(burg['state'])
                if burgState == int(state_i):
                    # print("***** MATCH *****")
                    if int(burg['capital']) == 1:
                        if 'dynasty' in burg:
                            dynasty = burg['dynasty']
                            leaderKey = dynasty['generations']['heir']['heir']['regnant']
                            state['leader'] = dynasty['persons'][leaderKey]
                            state['capitalName'] = burg['name']
                            state['dynasty'] = dynasty
    return state
