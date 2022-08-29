# Copyright 2022, William L. Nortman, All Rights Reserved
import json
import os
import subprocess
import traceback
from os.path import exists
from gen.person import (
    name,
)


def get_world(world_name):
    world = loadGeneratedWorld(world_name)
    if world is None:
        world = loadFantasyGroundsJsonFiles(world_name)
        world['world_name'] = world_name
        complete_world = populate_world(world)
        saveGeneratedWorld(world_name, complete_world)

        return complete_world
    return world


def populate_world(world):
    print(world)
    burgs = world['burgs']
    for burg in burgs:
        if 'name' in burg:
            print("Working on " + burg['name'])
            burg_generated = False
            while not burg_generated:
                try:
                    burg_pop_factor = float(burg['population'])
                    factor_rate = float(world['poprate'])
                    total_population = burg_pop_factor * factor_rate
                    burg['total_population'] = int(total_population)
                    generated_burg_details = get_burg_generationed_data(world, burg)
                    burg_generated = True

                    if 'dynasty' in generated_burg_details:
                        dynasty = generated_burg_details['dynasty']
                        leader_key = dynasty['generations']['heir']['heir']['regnant']
                        burg['leader'] = dynasty['persons'][leader_key]['name']
                        print("leader: " + burg['leader'])
                        burg['dynasty'] = dynasty
                    if 'domain' in generated_burg_details:
                        domain = generated_burg_details['domain']
                        burg['domain'] = domain

                except Exception as e:
                    print("Failed Parse - Trying Again.")
                    burg_generated = False
                    print(str(e))
                    traceback.print_exc()

    return world


def get_terrain_name(burg):
    terrain_name = ""
    burg_type = burg['type']
    if burg_type == "Generic":
        terrain_name = "Plains"
    elif burg_type == "Naval":
        terrain_name = "River"
    elif burg_type == "Lake":
        terrain_name = "Lakes"
    elif burg_type == "Hunting":
        terrain_name = "Grassland"
    return terrain_name


def get_burg_generationed_data(world, burg):
    cultures = world['cultures']
    culture = cultures[burg['culture']]
    cultureName = culture['name']
    try:
        trimStart = cultureName.index('(') + 1
        trimEnd = cultureName.index(")")
        raceName = cultureName[trimStart:trimEnd]
    except:
        raceName = 'Human'
    burgsize = "city"
    if burg['totalPopulation'] < 150:
        burgsize = 'hamlet'
    elif burg['totalPopulation'] < 800:
        burgsize = 'village'
    elif burg['totalPopulation'] < 8_000:
        burgsize = 'town'
    elif burg['totalPopulation'] < 20_000:
        burgsize = 'city'
    elif burg['totalPopulation'] < 1200_000:
        burgsize = 'capital'
    else:
        burgsize = 'kingdom'
    terrain_name = get_terrain_name(burg)
    print("node . " + raceName +
          " " + burgsize + " " + burg['name'] + " " + terrain_name)
    p = subprocess.Popen(
        ['/Users/bill.nortman/.nvm/versions/node/v16.13.1/bin/node',
         '/Users/bill.nortman/dev2/gen-test2/bin/index.js',
         raceName, burgsize, burg['name'], terrain_name], stdout=subprocess.PIPE)
    out = p.stdout.read()
    generated_burg_details = json.loads(out.decode("utf-8").strip())
    renamePeople(generated_burg_details)
    populateIndustrySummary(generated_burg_details)
    return generated_burg_details


def populateIndustrySummary(generated_burg_details):
    if 'dynasty' in generated_burg_details:
        industries = generated_burg_details['domain']['demographics']['industries']
        totalIndustriesPeople = 0
        for industry in industries:
            totalIndustriesPeople += int(industry['count'])
        generated_burg_details['domain']['totalIndustriesPeople'] = int(
            totalIndustriesPeople)
        print("totalIndustriesPeople:", totalIndustriesPeople)


def renamePeople(generatedBurgDetails):
    if 'dynasty' in generatedBurgDetails:
        dynasty = generatedBurgDetails['dynasty']
        race = dynasty['race']
        persons = dynasty['persons']
        familyLastName = None
        for personKey in persons:
            if familyLastName is None:
                familyLastName = name.last_name(personKey, race)
            person = persons[personKey]
            person['name'] = name.first_name(
                personKey, race, person['DNA']['gender']) + " " + familyLastName
            print(person['name'])


def saveGeneratedWorld(world_name, world):
    baseapppath = os.getcwd()
    newpath = "%s/data/worlds/%s/%s" % (baseapppath, world_name, world_name)
    with open("%s-generated.json" % (newpath), 'w') as open_file:
        json.dump(world, open_file)


def loadGeneratedWorld(world_name):
    baseapppath = os.getcwd()
    newpath = "%s/data/worlds/%s/%s" % (baseapppath, world_name, world_name)
    try:
        print("Checking for ")
        print("%s-generated.json" % (newpath))
        if not exists("%s-generated.json" % (newpath)):
            return None
        print("Exists ")

        with open("%s-generated.json" % (newpath), 'r') as open_file:
            world = json.load(open_file)
            print("Read in")
            return world
    except:
        return None


def loadFantasyGroundsJsonFiles(world_name):
    rawWorld = {}
    baseapppath = os.getcwd()
    newpath = "%s/data/worlds/%s/%s" % (baseapppath, world_name, world_name)

    with open("%s-burgs.json" % (newpath), 'r') as open_file:
        burgs = json.load(open_file)
        rawWorld['burgs'] = burgs
    with open("%s-markers.json" % (newpath), 'r') as open_file:
        markers = json.load(open_file)
        rawWorld['markers'] = markers
    with open("%s-cultures.json" % (newpath), 'r') as open_file:
        cultures = json.load(open_file)
        rawWorld['cultures'] = cultures
    with open("%s-religions.json" % (newpath), 'r') as open_file:
        religions = json.load(open_file)
        rawWorld['religions'] = religions
    with open("%s-states.json" % (newpath), 'r') as open_file:
        states = json.load(open_file)
        rawWorld['states'] = states
    with open("%s-poprate.txt" % (newpath), 'r') as open_file:
        Lines = open_file.readlines()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            rawWorld['poprate'] = float(line)
    return rawWorld
