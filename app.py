yes = True
no = False
question = 1
score = 0

key = {
    input('What\'s the name for a "special" port on a router? '): "interface",
}


while yes:
    print("Question", question)
    for x,y in key.items():
        x
        if x == y:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        question += 1
    yes = False


# for x, y in ch1_key.items():
#     print("Question.", x,y)
