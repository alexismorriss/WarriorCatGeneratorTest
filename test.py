import random


class Cats:
    def __init__(self, prefix, suffix, clan, color, markings, eyeColor, tailType, furLength, rank):
        self.prefix = prefix
        self.suffix = suffix
        self.clan = clan
        self.color = color
        self.markings = markings
        self.eyeColor = eyeColor
        self.tailType = tailType
        self.furLength = furLength
        self.rank = rank


def main():
    clanMembers = []
    print("Welcome to WC Clan Creator!")
    possiblePrefix = ["Acorn", "Adder", "Alder", "Amber", "Ant",
                      "Apple", "Arch", "Ash", "Aspen", "Badger", "Bark", "Bay", "Bee", "Beech", "Beetle", "Bella", "Berry", "Big", "Billy", "Birch", "Bird", "Black", "Blaze", "Blizzard", "Bloom", "Blossom", "Blue", "Bluebell"]
    possibleSuffix = ["Claw", "Fur", "Tuft", "Ear", "Pounce", "Tail"]
    howManyClans = input(
        "First, please enter your clans (seperated by commas): ")
    clanlist = howManyClans.split(",")
    coatColors = ["black", "brown", "blue", "silver", "white"]
    coatMarkings = ["tabby", "tuxedo", "tortieshell", "calico"]
    possibleEyes = ["blue", "green", "brown", "black", "amber", "yellow"]
    possibleTail = ["short", "long", "stub", "none"]
    possibleLength = ["short", "long"]
    possibleRank = ["kit", "apprentice", "medicine cat apprentice",
                    "warrior", "medicine cat", "elder"]

    howMany = int(input(
        "Next, please tell me many how many cats you wish to make: "))
    for i in range(howMany):
        radPrefix = random.randint(1, len(possiblePrefix))
        radSuffix = random.randint(1, len(possibleSuffix))
        radCoat = random.randint(1, len(coatColors))
        radMarkings = random.randint(1, len(coatMarkings))
        radEyes = random.randint(1, len(possibleEyes))
        radTail = random.randint(1, len(possibleTail))
        radLength = random.randint(1, len(possibleLength))
        radRank = random.randint(1, len(possibleRank))
        radClan = random.randint(1, len(clanlist))

        prefix = possiblePrefix[radPrefix-1]
        suffix = possibleSuffix[radSuffix-1]
        clan = clanlist[radClan-1]
        color = coatColors[radCoat-1]
        markings = coatMarkings[radMarkings-1]
        eyeColor = possibleEyes[radEyes-1]
        tailType = possibleTail[radTail-1]
        furLength = possibleLength[radLength-1]
        rank = possibleRank[radRank-1]
        cat = Cats(prefix, suffix, clan, color, markings,
                   eyeColor, tailType, furLength, rank)
        clanMembers.append(cat)

        if rank == "kit":
            cat.suffix = "Kit"
        elif rank == 'apprentice' or rank == "medicine cat apprentice":
            cat.suffix = "Paw"

    for cat in clanMembers:
        if cat.eyeColor[0] == "a":
            (print("Your name is", cat.prefix + cat.suffix + ",",
                   "you are an", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are a", cat.rank))
            if cat.rank[0] == "a":
                print("Your name is", cat.prefix + cat.suffix + ",",
                      "you are a", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are an", cat.rank)
        else:
            print("Your name is", cat.prefix + cat.suffix + ",",
                  "you are a", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are a", cat.rank)
            if cat.rank[0] == "a":
                print("Your name is", cat.prefix + cat.suffix + ",",
                      "you are a", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are an", cat.rank)
            else:
                print("Your name is", cat.prefix + cat.suffix + ",",
                      "you are a", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are a", cat.rank)
    input("Hit enter when ready to close.")


main()
