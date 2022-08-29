# Copyright 2022, William L. Nortman, All Rights Reserved

def getReligion(world, religion_i):
    religion = world['religions'][int(religion_i)]
    religion['decription'] = generateDecription(world, religion)
    return religion


def generateDecription(world, religion):
    return "AAAAAaaaaaaa"
