set lyrics to "SOMEBODY ONCE TOLD ME THE WORLD IS GONNA ROLL ME
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
ONLY SHOOTING STARS BREAK THE MOLD"


set i to 1
delay 5
display dialog "Are you sure you want to do this...?" with icon stop buttons {"Yep, what a concept."} default button 1
tell app "System Events"
	repeat (count words of lyrics) times
		set thisLetter to word i of lyrics as string
		keystroke thisLetter
		keystroke return
		if thisLetter is equal to " " then
			delay 0.5
		else
			delay 0.2
		end if
		set i to i+1
	end repeat
end tell