import msvcrt
import random

alph = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
chars = (
    # These 4 our mine
    "Finn", "Jake", "Princess Bubblegum", "Marceline", "Ice King",
    # Then I had chatGBT make me a larger list or characters because I want to post this on the adventure time subreddit
    "BMO", "Lumpy Space Princess", "Flame Princess", "Lady Rainicorn",
    "Tree Trunks", "Lemongrab", "Gunter", "Magic Man", "The Lich",
    "Susan Strong", "Peppermint Butler", "Fern", "Prismo", "Huntress Wizard",
    "Billy", "King of Ooo", "Me-Mow", "Cinnamon Bun", "Ricardio", "N.E.P.T.R.",
    "Shelby", "Starchie", "Martin Mertens", "Simon Petrikov", "Betty Grof",
    "Candy Cane Guy", "Doctor Princess", "Death", "Manfried",
    "Earl of Lemongrab", "Slime Princess", "Hot Dog Princess", "Wildberry Princess",
    "Breakfast Princess", "Ghost Princess", "Banana Guard",
    "Choose Goose", "Duke of Nuts", "Jake Jr.", "Kim Kil Whan", "T.V.",
    "Viola", "Charlie", "Jermaine", "Flambo", "Abracadaniel",
    "Snow Golem", "Fire Wolf Pup", "Banana Man", "Donny", "Tiffany Oiler",
    "Joshua", "Margaret", "Grob Gob Glob Grod", "Death", "Mr. Fox", "The King of Mars",
    "Rattleballs", "Maja the Sky Witch",
     "Scorcher", "The Duke", "James", "Shoko",
    "Root Beer Guy", "The Earl", "Elder Plops",
    "James Baxter", "Lemonhope", "Turtle Princess",
    "King Worm", "Cuber (Graybles)", "Mo", "Hambo", "Breezy", "Golb"
        )

questions = [
        # these top three are mine
        ("What's the best season?", ["Winter", "Summer", "Spring", "Fall"]),
        ("You see a goblin, what do you do?", ["Slay it", "Offer it some gold", "Ask it to join you team"]),
        ("What is your Quest?", ["To save the princess", "To find a big monster", "To explore a dungeon",
                                 "To hang out while there is a knife storm outside"]),
        # the rest of these are made by chatGBT so that I can post this to the adventure time subreddit
        ("Who is your favorite main character?", ["Finn", "Jake", "Princess Bubblegum", "Marceline", "Ice King"]),
        ("What would you want to eat in the Candy Kingdom?",
         ["Candy Corn", "Peppermint Butler", "Banana Guard", "Donut", "Cupcake"]),
        ("Which weapon would you wield in Ooo?",
         ["Finn Sword", "Grass Sword", "Billy's Gauntlet", "Ice King's Crown", "Flame Sword"]),
        ("What adventure would you go on?",
         ["Explore dungeons", "Fight monsters", "Save princesses", "Discover new lands", "Solve mysteries"]),
        ("Who would you want as your sidekick?",
         ["BMO", "Lumpy Space Princess", "Lady Rainicorn", "Tree Trunks", "Gunter"]),
        ("Which princess would you rescue?",
         ["Princess Bubblegum", "Flame Princess", "Lumpy Space Princess", "Slime Princess", "Wildberry Princess"]),
        ("Which realm of Ooo would you live in?",
         ["Candy Kingdom", "Fire Kingdom", "Ice Kingdom", "Lumpy Space", "Nightosphere"]),
        ("What kind of magical ability would you want?",
         ["Control ice", "Control fire", "Transform into any shape", "Talk to animals", "Mind reading"]),
        ("Which villain would you rather face?", ["The Lich", "Ricardio", "Me-Mow", "Magic Man", "Hunson Abadeer"]),
        ("What would you do with the Enchiridion?",
         ["Learn secrets", "Use it to fight evil", "Protect it", "Hide it", "Destroy it"]),
        ("Which Adventure Time creature would you be?",
         ["Fire Wolf", "Snow Golem", "Rainicorn", "Giant Worm", "Demon Cat"]),
        ("Who would you want as a mentor?", ["Billy", "Flame King", "Huntress Wizard", "Finn", "Peppermint Butler"]),
        ("Which game would you play with BMO?", ["Card Wars", "Video games", "Football", "Chess", "Tag"]),
        ("What would your royal title be?",
         ["Candy King/Queen", "Ice King/Queen", "Fire King/Queen", "Slime King/Queen", "Lumpy King/Queen"]),
        ("Which musical instrument would you play?",
         ["Finn's flute", "Marceline's bass", "Jake's viola", "BMO's drums", "Peppermint Butler's piano"]),
        ("What would you do if you found a dungeon?",
         ["Explore it", "Run away", "Invite friends", "Camp outside", "Map it out"]),
        ("Who would you join in a fight?",
         ["Finn and Jake", "Flame Princess", "Ice King", "Marceline", "Princess Bubblegum"]),
        ("Which episode would you want to be part of?",
         ["The Enchiridion!", "Dungeon Train", "I Remember You", "The Lich", "Simon & Marcy"]),
        ("Which magical artifact would you own?",
         ["Ice King's Crown", "Enchiridion", "Grass Sword", "Nightosphere Amulet", "Demon Blood Sword"]),
        ("What would you ask Prismo for as a wish?",
         ["Immortality", "Ultimate knowledge", "World peace", "A perfect sandwich", "Infinite riches"]),
        ("What kind of pet would you want in Ooo?",
         ["A Cute Bee", "Shelby the Worm", "Hot Dog Knight", "Gunter the penguin", "Fire Wolf Pup"]),
        ("What would you do with Ice King's powers?",
         ["Rule the Ice Kingdom", "Freeze enemies", "Create snowstorms", "Build ice sculptures", "Fly"]),
        ("Who is the best wizard in Ooo?",
         ["Ice King", "Abracadaniel", "Huntress Wizard", "Magic Man", "Peppermint Butler"]),
        ("If you could live a day in Ooo, what would you do?",
         ["Go on an adventure", "Visit the Candy Kingdom", "Hang out with Finn and Jake", "Explore the Fire Kingdom",
          "Battle the Lich"]),
        ("What's your favorite color?",
         ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', 'White', 'Gray', 'Violet',
          'Indigo', 'Cyan', 'Magenta', 'Turquoise', 'Beige', 'Maroon', 'Navy', 'Gold', 'Silver', 'Lime', 'Olive',
          'Teal']),
        ("What's your favorite type of food?", ["Pizza", "Burgers", "Sushi", "Pasta", "Salad"]),
        ("Which hobby would you most enjoy?", ["Reading", "Hiking", "Painting", "Playing video games", "Gardening"]),
        ("If you could have a superpower, what would it be?",
         ["Invisibility", "Flying", "Super strength", "Mind reading"]),
        ("Which animal would you want as a pet?", ["Dog", "Cat", "Bird", "Fish", "Hamster", "Snake"]),
        ("Which environment do you feel most comfortable in?", ["Mountains", "Beach", "Forest", "City", "Desert"]),
        ("What's your ideal vacation spot?", ["Paris", "Tokyo", "Hawaii", "New York City", "Sydney", "Italy", "Mexico"]),
        ("What type of movies do you prefer?",
         ["Action", "Comedy", "Drama", "Horror", "Science fiction", "Documentary"]),
        ("What’s your favorite time of day?", ["Morning", "Afternoon", "Evening", "Night"]),
        ("Which music genre do you listen to the most?", ["Pop", "Rock", "Hip-hop", "Classical", "Jazz", "Electronic"]),
        ("If you could visit a planet in our solar system, which one would you choose?",
         ["Mars", "Venus", "Jupiter", "Saturn", "Neptune"]),
        ("What's your favorite way to relax?",
         ["Meditating", "Watching TV", "Listening to music", "Going for a walk", "Sleeping"]),
        ("Which is your go-to dessert?", ["Ice cream", "Cake", "Cookies", "Brownies", "Pie"]),
        ("What do you value most in a friendship?", ["Loyalty", "Honesty", "Humor", "Kindness", "Support"]),
        ("Which fictional world would you most want to live in?",
         ["Middle-earth", "Hogwarts", "The Marvel Universe", "Narnia", "The Star Wars galaxy"]),
        ("What kind of sport do you prefer?", ["Soccer", "Basketball", "Tennis", "Swimming", "Running"]),
        ("Which ice cream flavor is your favorite?",
         ["Vanilla", "Chocolate", "Strawberry", "Mint chocolate chip", "Cookies and cream"]),
        ("What do you enjoy doing on the weekends?",
         ["Spending time with family", "Watching movies", "Playing sports", "Catching up on sleep",
          "Going out with friends"]),
        ("Which holiday do you look forward to the most?",
         ["Christmas", "Halloween", "Thanksgiving", "New Year's", "Easter"]),
        ("Which fantasy creature would you want to be?", ["Dragon", "Phoenix", "Griffin", "Unicorn", "Werewolf"]),
        ("What type of weather do you prefer?", ["Sunny", "Rainy", "Snowy", "Windy", "Cloudy"]),
        ("If you could master a skill instantly, what would it be?",
         ["Playing a musical instrument", "Speaking multiple languages", "Coding", "Cooking", "Drawing"]),
        ("What motivates you the most?", ["Achievement", "Recognition", "Adventure", "Creativity", "Helping others"])
    ]

score = 0

# All logic is done by yours truly and I think it is quite elegant
def poseQuestion(question, *args):
    global score
    errorFlag = True
    while(errorFlag):
        i = 0
        print(question)
        for arg in args:
            print(f"{alph[i]}. {arg}")
            i += 1
        answer = input("").upper()
        errorFlag = answer not in alph or alph.index(answer) > i - 1
        if(errorFlag):
            print("Invalid input, try again!\n")
        else:
            score += alph.index(answer) + 1
            print()

# main function, like in java
if __name__ == "__main__":
    print("\nThe Adventure Time Personality Test!")
    print("      Press any key to start       \n")
    msvcrt.getch()

    invalid = True
    while(invalid):
        try:
            num = int(input("What is your favorite number: "))
            invalid = False
            print()
        except ValueError:
            print("Invalid input, try again!\n")

    random.shuffle(questions)

    i = 0
    while i<20:
        print(f"{i+1}/20")
        poseQuestion(questions[i][0], *questions[i][1])
        i += 1

    # this is how I make it seem random
    character = chars[(score*num)%len(chars)]
    print(f"You are {character}!\n")
    print("Press any key to Exit...")
    msvcrt.getch()
