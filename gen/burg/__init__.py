# Copyright 2022, William L. Nortman, All Rights Reserved

import math
import random


def get_burg(world, burg_i):
    burgs = world["burgs"]
    burg = burgs[int(burg_i)]
    dynasty = burg['dynasty']
    leader_key = dynasty['generations']['heir']['heir']['regnant']
    burg['leader'] = dynasty['persons'][leader_key]
    generate_burg(world, burg)
    return burg


def generate_burg(world, burg):
    markers = world["markers"]
    burg_markers = []

    for marker in markers:
        xdiff = pow(float(marker['x']) - float(burg['x']), 2)
        ydiff = pow(float(marker['y']) - float(burg['y']), 2)
        distance = math.sqrt(xdiff + ydiff)
        if distance < 100:
            marker_distance = {"marker": marker, "distance": distance}
            burg_markers.append(marker_distance)
    burg_markers.sort(key=lambda k: k['distance'])
    populate_marker_stories(world, burg, burg_markers)
    burg['closeMarkers'] = burg_markers


def populate_marker_stories(world, burg, burgMarkers):
    for burgMarker in burgMarkers:
        marker_type = burgMarker['marker']['type']
        for story in marker_type['stories']:
            for burg_i in story.burgs:
                if burg['i'] == burg_i:
                    burg[marker_type]['stories'].append(story)


def get_industry_count(burg, industry_search):
    for industry in burg['domain']['demographics']['industries']:
        if industry['industry'] == industry_search:
            return int(industry['count'])


def generate_burg_description(world,burg):
    random.seed(world['world_name']+burg['i'])
