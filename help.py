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

answer = { }

def ask_questions():
   """User indicates drink preferences, then I print it"""
   true=["y","yes", "Yes","Y"]
   for key in questions:
        question=input("{} " .format(questions[key]))
        if question in true:
            answer[key]=True
        else:
            answer[key]=False
   print(answer)

def construct_drink():
    drink=[]
    for key in answer:
        ingredient=(ingredients[key])
        drink.append(random.choice(ingredient))
    print(drink)

if __name__=="__main__":
    ask_questions()
    construct_drink()