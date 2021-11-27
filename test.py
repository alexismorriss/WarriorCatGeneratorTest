import random


class Cats:
    def __init__(self, prefix, suffix, clan, color, markings, eyeColor, tailType, furLength, rank, personality1, personality2, personality3):
        self.prefix = prefix
        self.suffix = suffix
        self.clan = clan
        self.color = color
        self.markings = markings
        self.eyeColor = eyeColor
        self.tailType = tailType
        self.furLength = furLength
        self.rank = rank
        self.personality1 = personality1
        self.personality2 = personality2
        self.personality3 = personality3


def main():
    userInput = "yes"
    clanMembers = []
    print("Welcome to WC Bulk Creator!")
    possiblePrefix = ["Acorn", "Adder", "Alder", "Amber", "Ant",
                      "Apple", "Arch", "Ash", "Aspen", "Badger", "Bark", "Bay", "Bee", "Beech", "Beetle", "Bella", "Berry", "Big", "Billy", "Birch", "Bird", "Black", "Blaze", "Blizzard", "Bloom", "Blossom", "Blue", "Bluebell", "Boulder", "Bounce", "Bracken", "Bramble", "Brave", "Brave", "Breeze", "Briar", "Bright", "Brindle", "Bristle", "Broken", "Brown", "Bubbling", "Bug", "Bumble", "Buzzard", "Cedar", "Cherry", "Chestnut", "Chirp", "Chive", "Cinder", "Cinnamon", "Claw", "Clear", "Cloud", "Clover", "Cone", "Copper", "Creek", "Cricket", "Crooked", "Crouch", "Crow", "Curl", "Daisy", "Dandelion", "Dapple", "Dark", "Dawn", "Dead", "Deer", "Dew", "Doe", "Dove", "Down", "Drizzle", "Drift", "Duck", "Dusk", "Dust", "Eagle", "Ebony", "Echo", "Eel", "Elder", "Ember", "Fallen", "Fallow", "Fawn", "Feather", "Fennel", "Fern", "Ferret", "Fidget", "Fin", "Finch", "Fire", "Flail", "Flame", "Flash", "Flax", "Fleet", "Flicker", "Flint", "Flip", "Flower", "Flutter", "Fly", "Fog", "Fox", "Freckle", "Fringe", "Frog", "Frond", "Frost", "Furze", "Fuzzy", "Golden", "Goose", "Gorse", "Grass", "Gravel", "Gray", "Green", "Gull", "Hail", "Half", "Hare", "Hatch", "Haven", "Hawk", "Hay", "Hazel", "Heather", "Heavy", "Heron", "Hickory", "Hill", "Hollow", "Holly", "Honey", "Hoot", "Hop", "Hope", "Hound", "Ice", "Ivy", "Jagged", "Jay", "Jump", "Juniper", "Kestrel", "Kink", "Kite", "Lake", "Larch", "Lark", "Lavender", "Leaf", "Leopard", "Lichen", "Light", "Lightning", "Lily", "Lion", "Little", "Lizard", "Log", "Lost", "Loud", "Low", "Lynx", "Maggot", "Mallow", "Maple", "Marigold", "Marsh", "Meadow", "Midge", "Milk", "Milkweed", "Minnow", "Mint", "Mist", "Mistle", "Misty", "Mole", "Monkey", "Moon", "Morning", "Moss", "Mossy", "Moth", "Mottle", "Mouse", "Mud", "Mumble", "Myrtle", "Nectar", "Needle", "Nettle", "Newt", "Night", "Nut", "Oak", "Oat", "Odd", "Olive", "One", "Otter", "Owl", "Pale", "Parsley", "Patch", "Pear", "Pebble", "Perch", "Petal", "Pigeon", "Pike", "Pine", "Pink", "Plum", "Pod", "Pool", "Poppy", "Pounce", "Prickle", "Primrose", "Puddle", "Quail", "Quick", "Quiet", "Rabbit", "Ragged", "Rain", "Rat", "Raven", "Red", "Reed", "Riley", "Ripple", "River", "Robin", "Rock", "Rook", "Root", "Rose", "Rowan", "Rubble", "Running", "Rush", "Russet", "Rye", "Sage", "Sand", "Sandy", "Scorch", "Sedge", "Seed", "Shade", "Shadow", "Sharp", "Shattered", "Sheep", "Shell", "Shimmer", "Shining", "Shivering", "Short", "Shred", "Shrew", "Shy", "Silver", "Sky", "Slate", "Sleek", "Slight", "Sloe", "Small", "Smoke", "Snail", "Snake", "Snap", "Sneeze", "Snip", "Snook", "Snow", "Soft", "Song", "Soot", "Sorrel", "Spark", "Sparrow", "Speckle", "Spider", "Spike", "Spire", "Splash", "Spot", "Spotted", "Squirrel", "Stag", "Starling", "Stem", "Stoat", "Stone", "Stork", "Storm", "Strike", "Stumpy", "Sun", "Sunny", "Swallow", "Swamp", "Swan", "Sweet", "Swift", "Tall", "Talon", "Tangle", "Tansy", "Tawny", "Thistle", "Thorn", "Thrift", "Thrush", "Thunder", "Tiger", "Timber", "Tiny", "Toad", "Torn", "Trout", "Tulip", "Tumble", "Turtle", "Twig", "Vine", "Violet", "Vixen", "Vole", "Wasp", "Wave", "Weasel", "Web", "Weed", "Wet", "Whisker", "Whistle", "White", "Whorl", "Wild", "Willow", "Wind", "Wish", "Wolf", "Wood", "Woolly", "Wren", "Yarrow", "Yellow", "Yew"]

    possibleSuffix = ["Bark", "Beam", "Bee", "Belly", "Berry", "Bird", "Blaze", "Blossom", "Branch", "Breeze", "Briar", "Bright", "Brook", "Burr", "Burrow", "Bush", "Claw", "Cloud", "Crawl", "Creek", "Dapple", "Dawn", "Dusk", "Dust", "Ear", "Eater", "Eye", "Eyes", "Face", "Fall", "Fang", "Feather", "Fern", "Fire", "Fish", "Flake", "Flame", "Flight", "Flower", "Foot", "Frost", "Fur", "Gorse", "Hawk", "Haze", "Heart", "Ice", "Jaw", "Leaf", "Leap", "Leg", "Light", "Mask", "Minnow", "Mist", "Moon", "Muzzle", "Needle",
                      "Nose", "Pad", "Peak", "Pelt", "Pool", "Poppy", "Pounce", "Puddle", "Rose", "Ripple", "Runner", "Scar", "Scratch", "Seed", "Shade", "Shell", "Shine", "Sight", "Skip", "Slip", "Snout", "Snow", "Song", "Speck", "Speckle", "Spirit", "Splash", "Spot", "Spots", "Spring", "Stalk", "Stem", "Step", "Stone", "Storm", "Stream", "Strike", "Stripe", "Swoop", "Tail", "Talon", "Teeth", "Thistle", "Thorn", "Throat", "Toe", "Tooth", "Tuft", "Watcher", "Water", "Whisker", "Whisper", "Whistle", "Willow", "Wind", "Wing", "Wish"]
    clanInput = input(
        "First, please enter your clans (seperated by commas): ")
    clanlist = clanInput.split(", ")
    coatColors = ["black", "brown", "blue", "silver", "white", "ginger", "red",
                  "white", "cream", "golden", "russet", "yellow", "sandy", "beige", "tan", "gray"]
    coatMarkings = ["tabby", "tuxedo", "tortieshell", "calico"]
    possibleEyes = ["blue", "green", "brown",
                    "black", "amber", "yellow", "gray", "hazel"]
    possibleTail = ["short", "long", "stub", "no"]
    possibleLength = ["short", "long"]
    possibleRank = ["Kit", "Apprentice", "Medicine Cat Apprentice",
                    "Warrior", "Medicine Cat", "Elder"]
    possiblePersonality = ["Abrasive", "Accessible", "Active", "Adaptable", "Admirable", "Adventurous", "Aggressive", "Agreeable", "Alert", "Aloof", "Amiable", "Anticipative", "Anxious", "Apathetic", "Appreciative", "Arrogant", "Asocial", "Aspiring", "Assertive", "Awkward", "Balanced", "Benevolent", "Bland", "Blunt", "Boisterous", "Brave", "Brilliant", "Brutal", "Calm", "Capable", "Captivating", "Careless", "Caring", "Cautious", "Charismatic", "Charmin", "Cheerful", "Childish", "Clear-headed", "Clever", "Cold", "Compassionate", "Complacent", "Complaintive", "Compulsive", "Confident", "Confused", "Conscientious", "Considerate", "Contemplative", "Cooperative", "Courageous", "Courteous", "Cowardly", "Crafty", "Crass", "Creative", "Crude", "Cruel", "Curious", "Cynical", "Daring", "Deceitful", "Decent", "Decisive", "Dedicated", "Delicate", "Demanding", "Dependent", "Desperate", "Destructive", "Devious", "Difficult", "Dignified", "Disciplined", "Discontented", "Discouraging", "Dishonest", "Disloyal", "Disobedient", "Disorderly", "Disorganized", "Disrespectful", "Disruptive", "Dissolute", "Dramatic", "Dull", "Dutiful", "Earnest", "Easy", "Efficient", "Egocentric", "Elegant", "Energetic", "Enthusiastic", "Envious", "Erratic", "Excitable", "Exciting", "Extreme", "Faithful", "Faithless", "Farsighted", "Fearful", "Fickle", "Fiery", "Firm", "Fixed", "Flamboyant", "Flexible", "Focused", "Foolish", "Forgetful", "Forgiving", "Forthright", "Fraudulent", "Freethinking", "Friendly", "Frightening", "Fun-loving", "Funny", "Generous", "Gentle", "Genuine", "Gloomy", "Going", "Graceless", "Greedy", "Grim", "Gullible", "Hard-working", "Hateful", "Haughty", "Helpful", "Heroic", "Hesitant",
                           "Honest", "Honorable", "Hostile", "Humble", "Humorous", "Idealistic", "Ignorant", "Imaginative", "Impatient", "Impractical", "Imprudent", "Impulsive", "Inconsiderate", "Incurious", "Indecisive", "Independent", "Individualistic", "Insecure", "Insensitive", "Insightful", "Insincere", "Intelligent", "Intuitive", "Irrational", "Irresponsible", "Irritable", "Kind", "Knowledgeable", "Lazy", "Logical", "Loving", "Loyal", "Malicious", "Mannerless", "Mature", "Meddlesome", "Melancholic", "Miserable", "Misguided", "Modest", "Moody", "Morbid", "Motherly", "Naive", "Narrow", "Narrow-minded", "Neglectful", "Obnoxious", "Observant", "Obsessive", "Opinionated", "Opportunistic", "Optimistic", "Organized", "Passionate", "Passive", "Patient", "Peaceful", "Perfectionist", "Persuasive", "Petty", "Possessive", "Power-hungry", "Practical", "Pretentious", "Procrastinating", "Protective", "Rational", "Realistic", "Regretful", "Relaxed", "Reliable", "Resentful", "Resourceful", "Respectful", "Responsible", "Rigid", "Rowdy", "Scornful", "Secretive", "Self-indulgent", "Selfish", "Selfless", "Sensitive", "Sentimental", "Serious", "Shallow", "Shy", "Silly", "Single-minded", "Sly", "Sociable", "Spontaneous", "Steadfast", "Strong", "Strong-willed", "Sweet", "Sympathetic", "Thievish", "Thorough", "Thoughtless", "Timid", "Tolerant", "Treacherous", "Troublesome", "Trusting", "Unappreciative", "Uncaring", "Uncooperative", "Uncreative", "Uncritical", "Understanding", "Undisciplined", "Ungrateful", "Unrealistic", "Unreliable", "Vague", "Venal", "Venomous", "Vindictive", "Vulnerable", "Warm", "Weak", "Weak-willed", "Well-meaning", "Willful", "Wise", "Wishful", "Witty", "Youthful", ]

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
        radPersonality1 = random.randint(1, len(possiblePersonality))
        radPersonality2 = random.randint(1, len(possiblePersonality))
        radPersonality3 = random.randint(1, len(possiblePersonality))

        prefix = possiblePrefix[radPrefix-1]
        suffix = possibleSuffix[radSuffix-1]
        clan = clanlist[radClan-1]
        color = coatColors[radCoat-1]
        markings = coatMarkings[radMarkings-1]
        eyeColor = possibleEyes[radEyes-1]
        tailType = possibleTail[radTail-1]
        furLength = possibleLength[radLength-1]
        rank = possibleRank[radRank-1]
        personality1 = possiblePersonality[radPersonality1-1]
        personality2 = possiblePersonality[radPersonality2-1]
        personality3 = possiblePersonality[radPersonality3-1]

        if rank == "Kit":
            if lowercase == "Y":
                suffix = "kit"
            else:
                suffix = "Kit"
        else:
            pass
        if rank == "Apprentice" or rank == "Medicine Cat Apprentice":
            if lowercase == "Y":
                suffix = "paw"
            else:
                suffix = "Paw"
        else:
            pass

        radWhite = random.randint(1, 10)

        if radWhite <= 4 and color != "white":
            color = color + " and white"
        cat = Cats(prefix, suffix, clan, color, markings,
                   eyeColor, tailType, furLength, rank, personality1, personality2, personality3)
        clanMembers.append(cat)

    print()

    for cat in clanMembers:
        if cat.eyeColor[0] == "a":
            if cat.tailType == "no":
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "An", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with", cat.tailType, "tail", "|", "Personality Traits:", cat.personality1 + ",", cat.personality2 + ", and", cat.personality3)
            else:
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "An", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with a", cat.tailType, "tail", "|", "Personality Traits:", cat.personality1 + ",", cat.personality2 + ", and", cat.personality3)

        else:
            if cat.tailType == "no":
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "A", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with", cat.tailType, "tail", "|", "Personality Traits:", cat.personality1 + ",", cat.personality2 + ", and", cat.personality3)
            else:
                print("Name:", cat.prefix + cat.suffix, "|", "Clan:", cat.clan, "|", "Rank:", cat.rank, "|", "Appearence:",
                      "A", cat.eyeColor, "eyed,", cat.furLength, "furred,", cat.color, cat.markings, "with a", cat.tailType, "tail", "|", "Personality Traits:", cat.personality1 + ",", cat.personality2 + ", and", cat.personality3)

    print()

    input("Hit enter when ready to close.")


main()
