import sys
import math

#Orbital Period defined in seconds
#Orbital radius defined in kilometers
planets = {
    "mercury": {
        "name": "mercury",
        "orbital_radius": 57.9e6,
        "orbital_period": 88 * 86400,
        "description": "The smallest and innermost planet with a rocky surface and no atmosphere."
    },
    "venus": {
        "name": "venus",
        "orbital_radius": 108.2e6,
        "orbital_period": 224.7 * 86400,
        "description": "Known for its thick, toxic atmosphere and extreme surface temperatures."
    },
    "earth": {
        "name": "earth",
        "orbital_radius": 149.6e6,
        "orbital_period": 365.2 * 86400,
        "description": "The only known planet to support life, with diverse climates and ecosystems."
    },
    "mars": {
        "name": "mars",
        "orbital_radius": 228.0e6,
        "orbital_period": 687.0 * 86400,
        "description": "The Red Planet, home to the largest volcano and canyon in the Solar System."
    },
    "jupiter": {
        "name": "jupiter",
        "orbital_radius": 778.5e6,
        "orbital_period": 4331 * 86400,
        "description": "The largest planet, famous for its Great Red Spot and strong magnetic field."
    },
    "saturn": {
        "name": "saturn",
        "orbital_radius": 1432.0e6,
        "orbital_period": 10747 * 86400,
        "description": "Recognized for its stunning ring system and low density."
    },
    "uranus": {
        "name": "uranus",
        "orbital_radius": 2867.0e6,
        "orbital_period": 30589 * 86400,
        "description": "An ice giant with a unique axial tilt, leading to extreme seasonal changes."
    },
    "neptune": {
        "name": "neptune",
        "orbital_radius": 4515.0e6,
        "orbital_period": 59800 * 86400,
        "description": "Known for its deep blue color and the fastest winds in the Solar System."
    },
    "pluto": {
        "name": "pluto",
        "orbital_radius": 5906.4e6,
        "orbital_period": 90660 * 86400,
        "description": "A dwarf planet with a rocky surface and thin atmosphere, reclassified in 2006."}
}

#distance:
#The function calculate the distance between two planets, after
#an elapsed time,  All planets start at angle 0.0, at their orbital radius.

#Input:
#planet1: a string representing a planet
#planet2: a string representing a planet
#times: an array of seconds representing elapsed time from the starting position 
#of the planets.

#Output: return a dictionary if the planets are in the planets dictionary 
#or None if the planets does not exist.

#The output dictionary
#planets: An array of planets in alpahbetical order. A planet is represented as a string.
#times: A copy of the time input arry
#distances: distance between planets in km
#You can do this in polar or catersian coordinates.
def distances(planet1,planet2, times):
    #==========Your code goes here!=========
    if planet1 not in planets or planet2 not in planets:
        return None

    # Get the planet data
    a = planets[planet1]
    b = planets[planet2]

    # Get radii and orbital periods
    r1, t1 = a["orbital_radius"], a["orbital_period"]
    r2, t2 = b["orbital_radius"], b["orbital_period"]

    result_distances = []

    # Loop through each time and calculate the distance
    for time in times:
        angle1 = 2 * math.pi * time / t1
        angle2 = 2 * math.pi * time / t2

        x1 = r1 * math.cos(angle1)
        y1 = r1 * math.sin(angle1)
        x2 = r2 * math.cos(angle2)
        y2 = r2 * math.sin(angle2)

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        result_distances.append(float(f"{distance:.5f}"))



    return {
        "planets": sorted([planet1, planet2]),
        "times": times,
        "distances": result_distances
    }
def check():
    test_cases=[{"planet1":"earth","planet2":"mars","times":[0], 
                "expected":{"planets":["earth","mars"],"times":[0],
                            "distances":[7.84e7]}},
                {"planet1":"zeta prime","planet2":"mars","times":[0], 
                "expected":None},
                {"planet1":"mars","planet2":"ghetti prime","times":[0,1,2], 
                "expected":None},
                {"planet1":"pluto","planet2":"earth","times":[8.64e6,2.592e7,3.456e7,6.912e7], 
                "expected":{"planets":["earth","pluto"],"times":[8.64e6,2.592e7,3.456e7,6.912e7],
                            "distances":[5929532375.6308,5845858031.88055,5781098213.0158,5845784560.77428]}},]

    for test in test_cases:
        print("======Start of test case======")
        result = distances(test["planet1"], test["planet2"], test["times"])
        print("Your result")
        print(result)
        print("Expected answer")
        print(test["expected"])
        print("======End of test case======")
        

if __name__ == "__main__" :
    check()