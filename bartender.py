import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

stock = {
    "glug of rum": 20,
    "slug of whisky": 20,
    "splash of gin": 20,
    "olive on a stick": 20,
    "salt-dusted rim": 20,
    "rasher of bacon":20,
    "sugar cube":20,
    "spoonful of honey":20,
    "spash of cola":20,
    "slice of orange":20,
    "dash of cassis":20,
    "cherry on top":20,
}

answer = { }

customers = { }

def ask_questions():
   """User indicates drink preferences, then I print it"""
   print("I'm going to ask a few questions to help you pick a drink. Please answer yes or no.")
   true=["y","yes"]
   for key in questions:
        question=input("{} " .format(questions[key]))
        if question.lower() in true:
            answer[key]=True
        else:
            answer[key]=False
   customers[input("What is your name? ")]=(answer)
   print(answer)

def construct_drink():
    """Takes the choices from ask_questions and puts them into a drink."""
    print("Based on your answers, now I'll make your drink.")
    drink=[]
    for key in answer:
        if (answer[key])==True:
            ingredient=(ingredients[key])
            drink.append(random.choice(ingredient))
    for ingredient in stock:
        if ingredient in drink:
            stock[ingredient] -=1
    return "Here's what is in your drink: {}" .format(drink)

def name_drink():
    """Names the customer's drink"""
    nouns=["dog", "cat", "bird"]
    adjectives=["fluffy", "happy", "tired"]
    name=random.choice(adjectives) + " " + random.choice(nouns)
    return ("The name of your drink is {}" .format(name))

def another_drink():
    """Asks if the customer would like a drink and remembers their preferences if they are a returning customer"""
    while True:
        still_drinking=(input("Would you like a drink? "))
        true=["y","yes"]
        if still_drinking.lower() in true:
            name=input("What is your name? ")
            try:
                new_drink=customers[name]
                other_drink=[]
                for key in answer:
                    if new_drink[key]:
                        ingredient=(ingredients[key])
                        other_drink.append(random.choice(ingredient))
                for ingredient in stock:
                    if ingredient in other_drink:
                        stock[ingredient] -=1
                print ("You have these things in your new drink: {}" .format(other_drink))
            except KeyError:
                ask_questions()
                print(construct_drink())
                print(name_drink())
        else:
            print("Here is your check")
            break


if __name__=="__main__":
    ask_questions()
    print(construct_drink())
    print(name_drink())
    another_drink()
    print(stock)