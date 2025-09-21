# friends_trivia/question_bank.py
# Format expected by app_friends_mcq.py:
#   {"q": "...", "options": ["A","B","C","D"], "answer": <index 0..3>}
# You can optionally add "image" or "images" keys per question.

QUESTIONS: list[dict] = []

def add(q: str, options: list[str], correct: str):
    """Append an MCQ; correct must be one of options."""
    if correct not in options:
        raise ValueError(f"Correct answer not in options for: {q}")
    QUESTIONS.append({
        "q": q.strip(),
        "options": options,
        "answer": options.index(correct),
    })

# ---------------------------------------------------------------------
# Round 1 – How You Doin’? (Joey)
# ---------------------------------------------------------------------
add("Which Stephen King book did Joey hide in his freezer?",
    ["Pet Sematary", "The Shining", "Carrie", "It"],
    "The Shining")

add("How many sisters does Joey have?",
    ["7", "5", "2", "None"],
    "7")

add("What is the name of Joey’s Cabbage-Patch kid?",
    ["Ken Adams", "Maurice", "Hugsy", "Alicia May Emory"],
    "Alicia May Emory")

add("Which famous actor’s butt does Joey play in a shower scene?",
    ["Bruce Willis", "Al Pacino", "Charlton Heston", "Jeff Goldblum"],
    "Al Pacino")

add("What is the name of Joey’s character in the commercial for opening milk cartons?",
    ["Mike", "Tommy", "Kevin", "Drake"],
    "Kevin")

# ---------------------------------------------------------------------
# Round 2 – We Were on a Break! (Ross)
# ---------------------------------------------------------------------
add("What is Ross’ profession?",
    ["Geologist", "Astronomer", "Palaeontologist", "Museum tour guide"],
    "Palaeontologist")

add("Where does Ross spend the night with Emily after they first meet?",
    ["A hotel in Poughkeepsie", "A bed and breakfast in Vermont", "A bungalow in Tulsa", "A park in Atlantic City"],
    "A bed and breakfast in Vermont")

add("What song does Ross’ monkey, Marcel, keep playing?",
    ["‘The Lion Sleeps Tonight’ by The Tokens", "‘Tiny Dancer’ by Elton John",
     "‘The Way You Looked Tonight’ by Tony Bennett", "‘Careless Whisper’ by George Michael"],
    "‘The Lion Sleeps Tonight’ by The Tokens")

add("What instrument did Ross intend to play at Monica and Chandler’s wedding?",
    ["Keyboard", "Drums", "Saxophone", "Bagpipes"],
    "Bagpipes")

add("What item does Ross purchase for himself as part of his 1999 New Year’s Resolutions?",
    ["Digital camera", "Arcade machine", "Leather pants", "Wonder-broom"],
    "Leather pants")

# ---------------------------------------------------------------------
# Round 3 – I’m Hopeless and Awkward and Desperate for Love! (Chandler)
# ---------------------------------------------------------------------
add("What is Chandler’s middle name?",
    ["Muriel", "Nora", "Charles", "Francis"],
    "Muriel")

add("Which of Joey’s sisters does Chandler kiss?",
    ["Mary Therese", "Mary Angela", "Dina", "Cookie"],
    "Mary Angela")

add("Which toe does Chandler lose when Monica drops the knife on his foot?",
    ["Left foot big toe", "Right foot big toe", "Right foot pinkie", "Left foot pinkie"],
    "Right foot pinkie")

add("What is the name of Chandler’s favourite Baywatch star?",
    ["Kelly Slater", "Pamela Anderson", "Nancy Valen", "Yasmine Bleeth"],
    "Yasmine Bleeth")

add("What does Chandler have to do to get Joey to forgive him, after kissing Cathy?",
    ["Wear blue lipstick", "Lie in a wooden box for six hours", "Furnish their apartment", "Move to Yemen"],
    "Lie in a wooden box for six hours")

# ---------------------------------------------------------------------
# Round 4 – I Wasn’t Supposed to Put Beef in the Trifle! (Rachel)
# ---------------------------------------------------------------------
add("What film character did Rachel dress up as to fulfil Ross’ fantasy?",
    ["Princess Leia", "Supergirl", "Little Bo Peep", "Cat Woman"],
    "Princess Leia")

add("How many pages were in the letter Rachel wrote to Ross (front and back!)?",
    ["12", "8", "3", "18"],
    "18")

add("What famous actor does Rachel go on date with after meeting him on a movie set?",
    ["Bruce Willis", "Ben Stiller", "Jean-Claude van Damme", "Brad Pitt"],
    "Jean-Claude van Damme")

add("What happens to Rachel’s boss, Joanna, the night before her promotion goes through?",
    ["She gets hit by a taxi", "She goes on a date with Chandler",
     "She falls down an elevator shaft", "She moves to Paris"],
    "She gets hit by a taxi")

add("What is the name of the hairless cat Rachel gets for herself?",
    ["Fluffy", "Mrs Whiskerson", "Chi Chi", "Mozzarella"],
    "Mrs Whiskerson")

# ---------------------------------------------------------------------
# Round 5 – They Don’t Know That We Know They Know We Know! (Phoebe)
# ---------------------------------------------------------------------
add("What was the name of the ice-dancer Phoebe was married to?",
    ["Duncan", "Mike", "Gary", "David"],
    "Duncan")

add("What was the name of the neighbour’s dog who’d chase Phoebe as a child?",
    ["Lily", "Clunkers", "Candy", "Satan"],
    "Satan")

add("What is the next line in the song, “Monica, Monica, have a happy Hanukkah”",
    ["“And please tell Joey, Christmas will be snowy”",
     "“Saw Santa Claus, he said hello to Ross”",
     "“Spin the dreidel, Rachel”",
     "“Went to the store, sat on Santa’s lap”"],
    "“Saw Santa Claus, he said hello to Ross”")

add("How many embryos did Phoebe have planted inside of her?",
    ["9", "3", "5", "7"],
    "5")

add("Which city did Phoebe’s boyfriend, David, move to?",
    ["Tulsa", "Yemen", "London", "Minsk"],
    "Minsk")

# ---------------------------------------------------------------------
# Round 6 – I Am So Good at Lightning Rounds! (Monica)
# ---------------------------------------------------------------------
add("Who was Monica’s first kiss ever?",
    ["Chandler", "Pete", "Richard", "Ross"],
    "Ross")

add("What was the abbreviation of the first stock Monica invested in?",
    ["MEG", "CHP", "ZXY", "SGJ"],
    "MEG")

add("What was Monica’s nickname when she was a field hockey goalie?",
    ["Mon", "Big Fat Goalie", "Little Harmonica", "Crazy Plate Lady"],
    "Big Fat Goalie")

add("What did the Ukrainian kid that Monica hung out with at school have on all his snacks?",
    ["Mayonnaise", "Salad cream", "Sour cream", "Ketchup"],
    "Mayonnaise")

add("How much did Pete Becker tip Monica at the diner where she worked?",
    ["$10", "$300", "$20,000", "Nothing"],
    "$20,000")

# ---------------------------------------------------------------------
# General knowledge (Friends)
# ---------------------------------------------------------------------
add("What is the ‘Gellar Cup’ made of?",
    ["A 3D woman coming out of a photo frame",
     "A troll doll nailed to a two by four",
     "A fruit bowl found in the garbage",
     "A sock puppet shaped like a bunny"],
    "A troll doll nailed to a two by four")

add("What does Chandler think is in the email he opens that releases a virus onto Ross’ laptop?",
    ["Nude photos of Anna Kournikova",
     "A bid for a secret teapot",
     "Updates on a junior copywriter job",
     "A message from Janice"],
    "Nude photos of Anna Kournikova")

add("What instrument is played at Phoebe and Mike’s wedding?",
    ["Harp", "Recorder", "Steel drums", "Acoustic guitar"],
    "Steel drums")

add("How do Rachel and Monica get their apartment back from Chandler and Joey?",
    ["They swap it for Knicks tickets",
     "They promise fresh OJ every morning",
     "They give them their mattresses",
     "They kiss for 1 minute"],
    "They kiss for 1 minute")

add("What ridiculously expensive gift did Ross get Carol when he fell in love with her?",
    ["A shop window brooch", "A crystal duck",
     "An early edition of her favourite book", "A $500 dollar watch"],
    "A crystal duck")

# ---------------------------------------------------------------------
# Quotes – Who said this?
# ---------------------------------------------------------------------
add("“Who said this: Now imagine you live at the supermarket.”",
    ["Chandler", "Ross", "Gunther", "Nora Bing"],
    "Chandler")

add("“Who said this: And I love refrigerators!”",
    ["Paolo", "Janice", "Joey", "Frank Jr"],
    "Frank Jr")

add("“Who said this: You will always be the guy who peed on me.”",
    ["Phoebe", "Monica", "Bonnie", "Susan"],
    "Monica")

# =====================================================================
# Friends Quiz – Round 1: Multiple Choice (with provided answer key)
# =====================================================================
add("Which city is the series Friends set in?",
    ["Los Angeles", "New York City", "Miami", "Seattle"],
    "New York City")

add("What pet did Ross own?",
    ["A dog named Keith", "A rabbit called Lancelot",
     "A monkey named Marcel", "A lizard named Alistair"],
    "A monkey named Marcel")

add("What is Monica skilled at?",
    ["Bricklaying", "Cooking", "American football", "Singing"],
    "Cooking")

add("Monica briefly dates billionaire Pete Becker. Which country does he take her for their first date?",
    ["France", "Italy", "England", "Greece"],
    "Italy")

add("Rachel was popular in high school. Her prom date Chip ditched her for which girl at school?",
    ["Sally Roberts", "Amy Welsh", "Valerie Thompson", "Emily Foster"],
    "Amy Welsh")

add("What’s the name of the 1950s-themed diner where Monica worked as a waitress?",
    ["Marilyn & Audrey", "Twilight Galaxy", "Moondance Diner", "Marvin's"],
    "Moondance Diner")

add("What’s the name of Joey's penguin?",
    ["Snowflake", "Waddle", "Huggsy", "Bobber"],
    "Huggsy")

add("Which cartoon character was on Phoebe’s thermos that Ursula threw under a bus?",
    ["Pebbles Flintstone", "Yogi Bear", "Judy Jetson", "Bullwinkle"],
    "Judy Jetson")

add("What's the name of Janice's first husband?",
    ["Gary Litman", "Sid Goralnik", "Rob Bailystock", "Nick Layster"],
    "Gary Litman")

add("What song is Phoebe best known for?",
    ["Smelly Cat", "Smelly Dog", "Smelly Rabbit", "Smelly Worm"],
    "Smelly Cat")

add("What job does Ross have?",
    ["Paleontologist", "Artist", "Photographer", "Insurance salesman"],
    "Paleontologist")

add("What does Joey never share?",
    ["His books", "His information", "His food", "His DVDs"],
    "His food")

add("What is Chandler's middle name?",
    ["Muriel", "Jason", "Kim", "Zachary"],
    "Muriel")

add("Which Friends character plays Dr. Drake Ramoray on Days Of Our Lives?",
    ["Ross Geller", "Pete Becker", "Eddie Menuek", "Joey Tribbiani"],
    "Joey Tribbiani")

add("Who was Chandler's TV magazine always addressed to?",
    ["Chanandler Bong", "Chanandler Bang", "Chanandler Bing", "Chanandler Beng"],
    "Chanandler Bong")

add("What is Janice most likely to say?",
    ["Talk to the hand!", "Get me a coffee!", "Oh… my… God!", "No way!"],
    "Oh… my… God!")

add("What's the name of the grumpy person who works at the coffee shop?",
    ["Herman", "Gunther", "Frasier", "Eddie"],
    "Gunther")

add("Who sang the Friends theme?",
    ["The Banksys", "The Rembrandts", "The Constables", "The Da Vinci Band"],
    "The Rembrandts")

add("What kind of uniform does Joey wear to Monica and Chandler's wedding?",
    ["Chef", "Soldier", "Firefighter", "A baseball player"],
    "Soldier")

add("What are Ross and Monica's parents called?",
    ["Jack and Jill", "Philip and Holly", "Jack and Judy", "Margaret and Peter"],
    "Jack and Judy")

add("What is the name of Phoebe's alter-ego?",
    ["Phoebe Neeby", "Monica Bing", "Regina Phalange", "Elaine Benes"],
    "Regina Phalange")

add("What is the name of Rachel's Sphynx cat?",
    ["Baldy", "Mrs. Whiskerson", "Sid", "Felix"],
    "Mrs. Whiskerson")

add("When Ross and Rachel were “on a break,” Ross slept with Chloe. Where does she work?",
    ["Xerox", "Microsoft", "Domino’s", "Bank of America"],
    "Xerox")

add("Chandler’s mom had an interesting career and even more interesting love life. What’s her name?",
    ["Priscilla Mae Galway", "Nora Tyler Bing", "Mary Jane Blaese", "Jessica Grace Carter"],
    "Nora Tyler Bing")

add("Monica and Chandler met on Thanksgiving in 1987. She pursued being a chef because Chandler complimented her on which dish?",
    ["Green bean casserole", "Meatloaf", "Stuffing", "Macaroni and cheese"],
    "Macaroni and cheese")

# =====================================================================
# Extras converted from your loose list
# =====================================================================
add("What is the name of the coffee shop the friends always visit?",
    ["Central Perk", "The Moondance Diner", "Perk Central", "Café Nervosa"],
    "Central Perk")

add("What is the name of Ross’s pet monkey?",
    ["Marcel", "Mojo", "Maurice", "Max"],
    "Marcel")

add("What is Joey’s famous catchphrase?",
    ["How you doin'?", "Could I BE any cooler?", "Oh. My. God.", "We were on a break!"],
    "How you doin'?")

add("According to the lightning round quiz, what is Monica’s biggest pet peeve?",
    ["Animals dressed as humans", "People chewing loudly", "Leaving lights on", "Dirty dishes"],
    "Animals dressed as humans")

add("To whom is Chandler’s TV Guide addressed?",
    ["Miss Chanandler Bong", "Mr. Chandler Bing", "Ms. Chandler Bong", "Mr. Chanandler Bing"],
    "Miss Chanandler Bong")

add("What is Phoebe’s most famous song?",
    ["Smelly Cat", "Sticky Shoes", "Two of Them Kissed Last Night", "Little Black Curly Hair"],
    "Smelly Cat")

add("What are the names of Ross and Monica’s parents?",
    ["Jack and Judy", "Frank and Alice", "Leonard and Nora", "Richard and Nora"],
    "Jack and Judy")

add("What is the name of Ross and Rachel’s daughter?",
    ["Emma", "Ella", "Emily", "Erica"],
    "Emma")

add("Ross dresses up as which character to teach Ben about Hanukkah?",
    ["The Holiday Armadillo", "The Hanukkah Turtle", "The Festive Lizard", "The Party Porcupine"],
    "The Holiday Armadillo")

add("Which friend famously dances with a turkey on their head to cheer someone up?",
    ["Monica", "Joey", "Chandler", "Phoebe"],
    "Monica")

add("On which soap opera does Joey play Dr. Drake Ramoray?",
    ["Days of Our Lives", "General Hospital", "All My Children", "Passions"],
    "Days of Our Lives")

add("What is Rachel’s last name?",
    ["Green", "Greene", "Greer", "Greenfield"],
    "Green")

add("What was Monica’s high school nickname?",
    ["Big Fat Goalie", "Big Red", "The Chef", "Miss Organized"],
    "Big Fat Goalie")

add("What is the name of Joey’s stuffed penguin?",
    ["Hugsy", "Waddle", "Mr. Flippers", "Pengu"],
    "Hugsy")

# ---------------------------------------------------------------------
# More Friends MCQs (added batch)
# ---------------------------------------------------------------------

add("Who puts his head in a turkey on Thanksgiving?",
    ["Joey", "Chandler", "Ross", "Gunther"],
    "Joey")

add("Which brand offers Rachel a job in Paris?",
    ["Louis Vuitton", "Gucci", "Prada", "Chanel"],
    "Louis Vuitton")

add("Who pees on Monica's leg after she was stung by a jellyfish?",
    ["Chandler", "Joey", "Ross", "Gunther"],
    "Chandler")

add("Joey and Chandler have a statue of which animal in their apartment?",
    ["A dog", "A cat", "A duck", "A horse"],
    "A dog")

add("What role did Joey play on 'Days of Our Lives'?",
    ["Dr. Drake Ramoray", "Dr. Richard Burke", "Dr. Mike Hannigan", "Dr. Ross Geller"],
    "Dr. Drake Ramoray")

add("What is Chandler's profession?",
    ["Statistical analysis and data reconfiguration", "IT procurement manager", "Copywriter", "Data entry specialist"],
    "Statistical analysis and data reconfiguration")

add("What does Rachel guess Chandler's job is?",
    ["Transponster", "Data analyst", "Tax auditor", "Statistical coordinator"],
    "Transponster")

add("What was the name of Monica's dad's best friend whom she dated?",
    ["Richard", "Paul", "Alan", "Pete"],
    "Richard")

add("When Rachel called her dad from the wedding, she said 'I don't want to be a shoe, I want to be a ____.'",
    ["Hat", "Purse", "Dress", "Bag"],
    "Hat")

add("What is Phoebe's twin sister's name?",
    ["Ursula", "Phoebe Jr.", "Monica", "Alice"],
    "Ursula")

add("What caused a fire in Monica and Rachel's apartment?",
    ["A hair straightener", "A curling iron", "Candles", "The toaster"],
    "A hair straightener")

add("How many kids does Ross have?",
    ["2", "1", "3", "4"],
    "2")

add("Who does Gunther have a crush on?",
    ["Rachel", "Monica", "Phoebe", "Janice"],
    "Rachel")

add("What is Phoebe's brother's name?",
    ["Frank Jr.", "David", "Mike", "Ben"],
    "Frank Jr.")

add("Where does Joey keep 'The Shining' when it gets too scary?",
    ["In the freezer", "In the refrigerator", "Under his bed", "In the oven"],
    "In the freezer")

add("Where did Rachel get her first job?",
    ["Central Perk", "Bloomingdale's", "Ralph Lauren", "Fortunata Fashions"],
    "Central Perk")

add("Phoebe dated a cop. What was his name?",
    ["Gary", "David", "Mike", "Parker"],
    "Gary")

add("After working at Central Perk, which department store does Rachel start working for?",
    ["Bloomingdale's", "Ralph Lauren", "Louis Vuitton", "Gucci"],
    "Bloomingdale's")

add("Who from the group did Joey have a crush on?",
    ["Rachel", "Monica", "Phoebe", "Janice"],
    "Rachel")

add("What do the friends call the neighbor they can see through Monica and Rachel's window?",
    ["Ugly Naked Guy", "Handsome Naked Guy", "Old Naked Guy", "Buff Naked Guy"],
    "Ugly Naked Guy")

add("What does Janice's ex-husband sell?",
    ["Mattresses", "Cars", "Televisions", "Jewelry"],
    "Mattresses")

add("When Chandler hid Joey's underwear, what did Joey do?",
    ["He wore all of Chandler's clothes", "He hid Chandler's shoes", "He moved out", "He cut up Chandler's credit cards"],
    "He wore all of Chandler's clothes")

add("What are Ross's kids' names?",
    ["Ben and Emma", "Ben and Emily", "Jack and Erica", "Frank Jr. and Leslie"],
    "Ben and Emma")

add("Who was Monica's roommate before Rachel?",
    ["Phoebe", "Janice", "Ursula", "Carol"],
    "Phoebe")

add("What is Rachel's favorite book?",
    ["Little Women", "Pride and Prejudice", "The Shining", "The Notebook"],
    "Little Women")

add("What was Chandler's (fake) address in Yemen?",
    ["15 Yemen Road, Yemen", "5 Yemen Street, Yemen", "15 Yemin Road, Sanaa", "10 Yemen Avenue, Yemen"],
    "15 Yemen Road, Yemen")

add("What did Phoebe tell Mike she changed her name to?",
    ["Princess Consuela Banana Hammock", "Regina Phalange", "Valerie Bananahammock", "Crabtree Hammock"],
    "Princess Consuela Banana Hammock")

add("What is Monica's job?",
    ["A chef", "A waitress", "A fashion buyer", "A nanny"],
    "A chef")

add("Whose triplets was Phoebe a surrogate to?",
    ["Her brother Frank Jr. and his wife Alice", "Ross and Rachel", "Monica and Chandler", "Carol and Susan"],
    "Her brother Frank Jr. and his wife Alice")

add("Who is Jack and Judy Geller's favorite child?",
    ["Ross", "Monica", "Neither", "Both"],
    "Ross")

add("What did Phoebe name the rat in her apartment?",
    ["Bob", "Gus", "Clunkers", "Mittens"],
    "Bob")

add("When Ross falls asleep on the train, where does he end up?",
    ["Montreal", "Poughkeepsie", "Boston", "Albany"],
    "Montreal")

add("Who was Ross's first wife?",
    ["Carol", "Emily", "Rachel", "Julie"],
    "Carol")

add("Why did Ross and Emily call off the wedding?",
    ["Ross said Rachel's name at the altar", "Emily moved to Paris", "Visa issues", "Ross missed the ceremony"],
    "Ross said Rachel's name at the altar")

add("Where did Ross and Rachel get married?",
    ["Las Vegas", "Barbados", "London", "New York City"],
    "Las Vegas")

add("Where did Monica and Chandler first get together?",
    ["At Ross's wedding in London", "In Las Vegas", "At the beach house", "At the Geller house"],
    "At Ross's wedding in London")

add("Who did Phoebe name her brother's daughter after?",
    ["Chandler", "Rachel", "Ursula", "Monica"],
    "Chandler")

add("What does Joey name his Barcalounger?",
    ["Rosita", "Estelle", "Big Red", "La-Z-Mon"],
    "Rosita")

add("When Monica gets her credit card stolen, what name does she give the thief?",
    ["Monana", "Monnica", "Moana", "Mona"],
    "Monana")

add("Which Sprouse twin played Ben, Ross's son?",
    ["Cole Sprouse", "Dylan Sprouse", "Both of them", "Neither of them"],
    "Cole Sprouse")

add("Which character said the iconic line 'Pivot'?",
    ["Ross", "Chandler", "Joey", "Monica"],
    "Ross")

add("Who was Chandler's college roommate?",
    ["Ross", "Joey", "Gunther", "Kip"],
    "Ross")

add("Why did Ross and Carol break up?",
    ["Carol came out as a lesbian", "Ross moved to London", "They grew bored", "Ross cheated"],
    "Carol came out as a lesbian")

add("At Monica and Chandler's wedding, who is Monica's maid of honor?",
    ["Rachel", "Phoebe", "Janice", "Emily"],
    "Rachel")

add("Which of the friends hates Thanksgiving?",
    ["Chandler", "Ross", "Rachel", "Monica"],
    "Chandler")

add("Where does the group travel to for Ross's paleontology convention?",
    ["Barbados", "London", "Tulsa", "Vermont"],
    "Barbados")

add("What are Rachel's sisters' names?",
    ["Amy and Jill", "Amy and Janice", "Jill and Emily", "Amy and Carol"],
    "Amy and Jill")

add("In college, what was the name of Ross and Chandler's band?",
    ["Way, No Way", "The Routine", "Embryos", "Flock of Seagulls"],
    "Way, No Way")

add("What is the name of Richard's son?",
    ["Timothy", "Ben", "Jack", "Joshua"],
    "Timothy")

add("What was the name of Ross and Monica's dog when they were kids?",
    ["Chi-Chi", "LaPooh", "Clunkers", "Marcel"],
    "Chi-Chi")

add("What is Chandler especially bad at?",
    ["Giving gifts", "Dancing", "Singing", "Cooking"],
    "Giving gifts")

add("Who says the last line in the whole series?",
    ["Chandler", "Ross", "Monica", "Joey"],
    "Chandler")

add("How old was Monica when she learned how to tell time?",
    ["13", "10", "8", "15"],
    "13")

add("What fruit is Ross allergic to?",
    ["Kiwi", "Apple", "Strawberry", "Mango"],
    "Kiwi")

add("What was the name of Monica and Rachel's downstairs neighbor?",
    ["Mr. Heckles", "Mr. Treeger", "Mr. Filange", "Mr. Geller"],
    "Mr. Heckles")

add("What store does Phoebe hate?",
    ["Pottery Barn", "Restoration Hardware", "IKEA", "CB2"],
    "Pottery Barn")

add("What is Richard's job?",
    ["Ophthalmologist", "Optometrist", "Dentist", "Proctologist"],
    "Ophthalmologist")

add("What was the job of Rachel's ex-fiancé, Barry?",
    ["Orthodontist", "Dentist", "Oral surgeon", "Optometrist"],
    "Orthodontist")

add("What did Monica start making to get over Richard?",
    ["Jam", "Salsa", "Marmalade", "Cookies"],
    "Jam")

add("On Thanksgiving, which sport does the group play together?",
    ["Football", "Basketball", "Soccer", "Tennis"],
    "Football")

add("What is the name of Richard's daughter?",
    ["Michelle", "Emily", "Emma", "Nina"],
    "Michelle")

add("What are Monica and Chandler's twins' names?",
    ["Jack and Erica", "Ben and Emma", "Frank Jr. Jr. and Leslie", "Jack and Judy"],
    "Jack and Erica")

add("What is the name of Joey's agent?",
    ["Estelle", "Ursula", "Elaine", "Nora"],
    "Estelle")

add("What was the name of the club Ross and Will had in high school?",
    ["The I Hate Rachel Green Club", "Science Club", "Debate Club", "Drama Club"],
    "The I Hate Rachel Green Club")

add("What was Joey's nickname when he was a waiter at a restaurant?",
    ["Dragon", "Big Joe", "Ken Adams", "Dr. Drake"],
    "Dragon")

add("Phoebe stole a comic book from Ross. What was the name of the book?",
    ["Science Boy", "Space Boy", "Dino Dude", "Galaxy Guy"],
    "Science Boy")

add("What was Joey's imaginary friend's name?",
    ["Maurice", "Ken Adams", "Hugsy", "Tony"],
    "Maurice")

add("What is Phoebe's job?",
    ["A masseuse", "A musician", "A chef", "A barista"],
    "A masseuse")

add("Rachel goes on Ross's honeymoon alone. Where does she go?",
    ["Greece", "Barbados", "Paris", "London"],
    "Greece")

add("What pet animals did Chandler and Joey have?",
    ["A chick and a duck", "A dog and a cat", "A fish and a turtle", "A parrot"],
    "A chick and a duck")

add("What is Joey's imaginary friend's profession?",
    ["Space cowboy", "Astronaut", "Firefighter", "Spy"],
    "Space cowboy")

add("What was Ross and Rachel's daughter's first word?",
    ["Gleba", "Mama", "Hi", "Phoebe"],
    "Gleba")

add("What does Phoebe not believe in?",
    ["Evolution", "Gravity", "Germs", "Dinosaurs"],
    "Evolution")

add("As a child, Rachel had a dog. What was its name?",
    ["LaPooh", "Chi-Chi", "LaDiDa", "Poofy"],
    "LaPooh")

add("What game show was Joey auditioning to host?",
    ["Bamboozled", "Pyramid", "Jeopardy!", "Wheel of Fortune"],
    "Bamboozled")

add("At Barry and Mindy's wedding, who is the maid of honor?",
    ["Rachel", "Mindy", "Monica", "Phoebe"],
    "Rachel")

add("How does Ross end up getting Ugly Naked Guy's apartment?",
    ["He hangs out with him naked", "He bribes the super", "He writes a letter campaign", "He trades his couch"],
    "He hangs out with him naked")

add("What was Ross's fiancée Emily's last name?",
    ["Waltham", "Green", "Geller", "Hannigan"],
    "Waltham")

