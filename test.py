import random


class Cats:
    def __init__(self, prefix, suffix, clan, color, markings, eyeColor, tailType, furLength, rank, personality):
        self.prefix = prefix
        self.suffix = suffix
        self.clan = clan
        self.color = color
        self.markings = markings
        self.eyeColor = eyeColor
        self.tailType = tailType
        self.furLength = furLength
        self.rank = rank
        self.personality = personality


def main():
    clanMembers = []
    print("Welcome to WC Bulk Creator!")
    possiblePrefix = ["Acorn", "Adder", "Alder", "Amber", "Ant",
                      "Apple", "Arch", "Ash", "Aspen", "Badger", "Bark", "Bay", "Bee", "Beech", "Beetle", "Bella", "Berry", "Big", "Billy", "Birch", "Bird", "Black", "Blaze", "Blizzard", "Bloom", "Blossom", "Blue", "Bluebell", "Boulder", "Bounce", "Bracken", "Bramble", "Brave", "Brave", "Breeze", "Briar", "Bright", "Brindle", "Bristle", "Broken", "Brown", "Bubbling", "Bug", "Bumble", "Buzzard", "Cedar", "Cherry", "Chestnut", "Chirp", "Chive", "Cinder", "Cinnamon", "Claw", "Clear", "Cloud", "Clover", "Cone", "Copper", "Creek", "Cricket", "Crooked", "Crouch", "Crow", "Curl", "Daisy", "Dandelion", "Dapple", "Dark", "Dawn", "Dead", "Deer", "Dew", "Doe", "Dove", "Down", "Drizzle", "Drift", "Duck", "Dusk", "Dust", "Eagle", "Ebony", "Echo", "Eel", "Elder", "Ember", "Fallen", "Fallow", "Fawn", "Feather", "Fennel", "Fern", "Ferret", "Fidget", "Fin", "Finch", "Fire", "Flail", "Flame", "Flash", "Flax", "Fleet", "Flicker", "Flint", "Flip", "Flower", "Flutter", "Fly", "Fog", "Fox", "Freckle", "Fringe", "Frog", "Frond", "Frost", "Furze", "Fuzzy", "Golden", "Goose", "Gorse", "Grass", "Gravel", "Gray", "Green", "Gull", "Hail", "Half", "Hare", "Hatch", "Haven", "Hawk", "Hay", "Hazel", "Heather", "Heavy", "Heron", "Hickory", "Hill", "Hollow", "Holly", "Honey", "Hoot", "Hop", "Hope", "Hound", "Ice", "Ivy"]
    possibleSuffix = ["Bark", "Beam", "Bee", "Belly", "Berry", "Bird", "Blaze", "Blossom", "Branch", "Breeze", "Briar", "Bright", "Brook", "Burr", "Burrow", "Bush", "Claw", "Cloud", "Crawl", "Creek", "Dapple", "Dawn", "Dusk", "Dust", "Ear", "Eater", "Eye", "Eyes", "Face", "Fall", "Fang", "Feather", "Fern", "Fire", "Fish", "Flake", "Flame", "Flight", "Flower", "Foot", "Frost", "Fur", "Gorse", "Hawk", "Haze", "Heart", "Ice", "Jaw", "Leaf", "Leap", "Leg", "Light", "Mask", "Minnow", "Mist", "Moon", "Muzzle", "Needle",
                      "Nose", "Pad", "Peak", "Pelt", "Pool", "Poppy", "Pounce", "Puddle", "Rose", "Ripple", "Runner", "Scar", "Scratch", "Seed", "Shade", "Shell", "Shine", "Sight", "Skip", "Slip", "Snout", "Snow", "Song", "Speck", "Speckle", "Spirit", "Splash", "Spot", "Spots", "Spring", "Stalk", "Stem", "Step", "Stone", "Storm", "Stream", "Strike", "Stripe", "Swoop", "Tail", "Talon", "Teeth", "Thistle", "Thorn", "Throat", "Toe", "Tooth", "Tuft", "Watcher", "Water", "Whisker", "Whisper", "Whistle", "Willow", "Wind", "Wing", "Wish"]
    clanInput = input(
        "First, please enter your clans (seperated by commas): ")
    clanlist = clanInput.split(", ")
    coatColors = ["black", "brown", "blue", "silver", "white"]
    coatMarkings = ["tabby", "tuxedo", "tortieshell", "calico"]
    possibleEyes = ["blue", "green", "brown", "black", "amber", "yellow"]
    possibleTail = ["short", "long", "stub", "no"]
    possibleLength = ["short", "long"]
    possibleRank = ["Kit", "Apprentice", "Medicine Cat Apprentice",
                    "Warrior", "Medicine Cat", "Elder"]
    possiblePersonality = ["Stern", "Kind", "Motherly",
                           "Mischevious", "Angry", "Loyal", "Helpful", "Tired"]

    howManyCats = int(input(
        "Next, please tell me many how many cats you wish to make: "))

    lowercase = input(
        "Lastly, please tell me if you want the suffixes lowercase (Y/N): ")

    if lowercase == "Y":
        for i in range(len(possibleSuffix)):
            possibleSuffix[i] = possibleSuffix[i].lower()
    else:
        pass

    for i in range(howManyCats):
        radPrefix = random.randint(1, len(possiblePrefix))
        radSuffix = random.randint(1, len(possibleSuffix))
        radCoat = random.randint(1, len(coatColors))
        radMarkings = random.randint(1, len(coatMarkings))
        radEyes = random.randint(1, len(possibleEyes))
        radTail = random.randint(1, len(possibleTail))
        radLength = random.randint(1, len(possibleLength))
        radRank = random.randint(1, len(possibleRank))
        radClan = random.randint(1, len(clanlist))
        radPersonality = random.randint(1, len(possiblePersonality))

        prefix = possiblePrefix[radPrefix-1]
        suffix = possibleSuffix[radSuffix-1]
        clan = clanlist[radClan-1]
        color = coatColors[radCoat-1]
        markings = coatMarkings[radMarkings-1]
        eyeColor = possibleEyes[radEyes-1]
        tailType = possibleTail[radTail-1]
        furLength = possibleLength[radLength-1]
        rank = possibleRank[radRank-1]
        personality = possiblePersonality[radPersonality-1]
        cat = Cats(prefix, suffix, clan, color, markings,
                   eyeColor, tailType, furLength, rank, personality)
        clanMembers.append(cat)

        if rank == "kit":
            cat.suffix = "Kit"
        elif rank == 'apprentice' or rank == "medicine cat apprentice":
            cat.suffix = "Paw"

    print()

    for cat in clanMembers:
        if cat.eyeColor[0] == "a":
            print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                  "An", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with a", cat.tailType, "tail", "|", "Personality:", cat.personality)
            if cat.tailType == "no":
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "An", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with", cat.tailType, "tail", "|", "Personality:", cat.personality)
        else:
            if cat.tailType == "no":
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "A", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with", cat.tailType, "tail", "|", "Personality:", cat.personality)
            else:
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "A", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with a", cat.tailType, "tail", "|", "Personality:", cat.personality)

    print()

    userInput = input(
        "Hello! As you may have noticed we don't have all the prefixes! Would you like to add some? (Y/N) ")

    input("Hit enter when ready to close.")


main()
