import random
# coatColors = ["black", "brown", "blue", "silver", "white"]
# radCoat = random.randint(1, len(coatColors))

# print("Your coat is", coatColors[radCoat-1])


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
    possiblePrefix = ["Bee", "Heather", "Ripple", "Night", "Ivory"]
    possibleSuffix = ["Claw", "Fur", "Tuft", "Ear", "Pounce", "Tail"]
    clan = input("First, please enter your clan name: ")
    coatColors = ["black", "brown", "blue", "silver", "white"]
    coatMarkings = ["tabby", "tuxedo", "tortieshell", "calico"]
    possibleEyes = ["blue", "green", "brown", "black", "amber", "yellow"]
    possibleTail = ["short", "long", "stub", "none"]
    possibleLength = ["short", "long"]
    possibleRank = ["kit", "apprentice", "medicine cat apprentice",
                    "warrior", "medicine cat", "elder"]

    howMany = int(input(
        "Next, please tell me many how many cats are in your clan: "))
    for i in range(howMany):
        radPrefix = random.randint(1, len(possiblePrefix))
        radSuffix = random.randint(1, len(possibleSuffix))
        radCoat = random.randint(1, len(coatColors))
        radMarkings = random.randint(1, len(coatMarkings))
        radEyes = random.randint(1, len(possibleEyes))
        radTail = random.randint(1, len(possibleTail))
        radLength = random.randint(1, len(possibleLength))
        radRank = random.randint(1, len(possibleRank))

        prefix = possiblePrefix[radPrefix-1]
        suffix = possibleSuffix[radSuffix-1]
        color = coatColors[radCoat-1]
        markings = coatMarkings[radMarkings-1]
        eyeColor = possibleEyes[radEyes-1]
        tailType = possibleTail[radTail-1]
        furLength = possibleLength[radLength-1]
        rank = possibleRank[radRank-1]
        cat = Cats(prefix, suffix, clan, color, markings,
                   eyeColor, tailType, furLength, rank)
        clanMembers.append(cat)

    for cat in clanMembers:
        print("Your name is", cat.prefix + cat.suffix + ",",
              "you are a", cat.eyeColor, "eyed", cat.furLength, "furred", cat.color, cat.markings, "with a", cat.tailType, "tail" + ",", "your clan is", cat.clan, "and you are a", cat.rank)


main()
