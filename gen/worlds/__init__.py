# Copyright 2022, William L. Nortman, All Rights Reserved

import os


def get_worlds():
    worlds = ["Test1", "Test2"]
    print("Getting Worlds....")
    for root, dirs, files in os.walk('data/worlds'):
        for name in dirs:
            worlds.append(name)
            print("world:"+name)
        return worlds
