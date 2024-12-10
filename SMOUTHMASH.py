import random

lyricsString = """SOMEBODY ONCE TOLD ME THE WORLD IS GONNA ROLL ME 
I AIN\'T THE SHARPEST TOOL IN THE SHED 
SHE WAS LOOKING KIND OF DUMB WITH HER FINGER AND HER THUMB 
IN THE SHAPE OF AN \"L\" ON HER FOREHEAD 
WELL THE YEARS START COMING AND THEY DON\'T STOP COMING 
FED TO THE RULES AND I HIT THE GROUND RUNNING 
DIDN\'T MAKE SENSE NOT TO LIVE FOR FUN 
YOUR BRAIN GETS SMART BUT YOUR HEAD GETS DUMB 
SO MUCH TO DO, SO MUCH TO SEE 
SO WHAT\'S WRONG WITH TAKING THE BACK STREETS? 
YOU\'LL NEVER KNOW IF YOU DON'T GO 
YOU\'LL NEVER SHINE IF YOU DON'T GLOW 
HEY NOW, YOU\'RE AN ALL-STAR, GET YOUR GAME ON, GO PLAY 
HEY NOW, YOU\'RE A ROCK STAR, GET THE SHOW ON, GET PAID 
AND ALL THAT GLITTERS IS GOLD 
ONLY SHOOTING STARS BREAK THE MOLD 
IT\'S A COOL PLACE AND THEY SAY IT GETS COLDER 
YOU\'RE BUNDLED UP NOW, WAIT TILL YOU GET OLDER 
BUT THE METEOR MEN BEG TO DIFFER 
JUDGING BY THE HOLE IN THE SATELLITE PICTURE 
THE ICE WE SKATE IS GETTING PRETTY THIN 
THE WATER\'S GETTING WARM SO YOU MIGHT AS WELL SWIM 
MY WORLD\'S ON FIRE, HOW ABOUT YOURS? 
THAT\'S THE WAY I LIKE IT AND I NEVER GET BORED 
HEY NOW, YOU\'RE AN ALL-STAR, GET YOUR GAME ON, GO PLAY 
HEY NOW, YOU\'RE A ROCK STAR, GET THE SHOW ON, GET PAID 
ALL THAT GLITTERS IS GOLD 
ONLY SHOOTING STARS BREAK THE MOLD 
HEY NOW, YOU\'RE AN ALL-STAR, GET YOUR GAME ON, GO PLAY 
HEY NOW, YOU\'RE A ROCK STAR, GET THE SHOW, ON GET PAID 
AND ALL THAT GLITTERS IS GOLD 
ONLY SHOOTING STARS 
SOMEBODY ONCE ASKED COULD I SPARE SOME CHANGE FOR GAS? 
I NEED TO GET MYSELF AWAY FROM THIS PLACE 
I SAID YEP WHAT A CONCEPT 
I COULD USE A LITTLE FUEL MYSELF 
AND WE COULD ALL USE A LITTLE CHANGE 
WELL, THE YEARS START COMING AND THEY DON\'T STOP COMING 
FED TO THE RULES AND I HIT THE GROUND RUNNING 
DIDN\'T MAKE SENSE NOT TO LIVE FOR FUN 
YOUR BRAIN GETS SMART BUT YOUR HEAD GETS DUMB 
SO MUCH TO DO, SO MUCH TO SEE 
SO WHAT\'S WRONG WITH TAKING THE BACK STREETS? 
YOU\'LL NEVER KNOW IF YOU DON\'T GO (GO!) 
YOU\'LL NEVER SHINE IF YOU DON\'T GLOW 
HEY NOW, YOU\'RE AN ALL-STAR, GET YOUR GAME ON, GO PLAY 
HEY NOW, YOU\'RE A ROCK STAR, GET THE SHOW ON, GET PAID 
AND ALL THAT GLITTERS IS GOLD 
ONLY SHOOTING STARS BREAK THE MOLD 
AND ALL THAT GLITTERS IS GOLD 
ONLY SHOOTING STARS BREAK THE MOLD"""

# Preprocess from block string into list
shuffleSongStructure = False # Ignores transitions with respect to the song's whitespace when True
if shuffleSongStructure:
    # Line endings are stripped and converted to words delimiters
    lyricsString = ' '.join([line.strip() for line in lyricsString.split('\n') if line.strip()])
    # lyricsString = " ".join(lyricsString.split("\n"))
lyricsArray = lyricsString.split(" ")

# Make a transition dictionary and print it
markovOrder = 1 # Context window
associations = {}
for index in range(len(lyricsArray) - 2 * markovOrder):
    seed_index = index + markovOrder
    next_index = seed_index + markovOrder
    seed = " ".join(lyricsArray[index:seed_index])
    nextWord = " ".join(lyricsArray[seed_index:next_index])
    if seed in associations:
        associations[seed].append(nextWord)
    else:
        associations[seed] = [nextWord]
print("Generated Associations:")
for word,transition in [[key, associations[key]] for key in sorted(associations.keys())]: # Sort keys to more easily reference with output
    print(repr(word), "->", transition)

length = 150 // markovOrder
result = []
seed = random.choice(list(associations.keys())) # Choose a random starting key
# seed = "SOMEBODY ONCE TOLD"
assert(len(seed.split(" ")) == markovOrder) # seed word length must match markov order
result.append(seed)
# Go markov go
for _ in range(length - 1):
    if seed in associations:
        nextWord = random.choice(associations[seed]) # skibididobadahbididobodo
        result.append(nextWord)
        seed = " ".join(result[-markovOrder:]) # Updates seed to result of the built string
    else:
        seed = random.choice(list(associations.keys())) # Updates seed as any random key
        if shuffleSongStructure:
            seed = '\n' + seed
        result.append(seed)

# Combine result into a single output string
output = " ".join(result)
print()
print('shuffleSongStructure:', shuffleSongStructure)
print('markovOrder:', markovOrder)
print("\nGenerated Lyrics:")
print(output)
