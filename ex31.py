print("""You enter a darkroom with two doors
Do you go through door 1 or door 2""")

# so basically constructing a very narrow maze sorta game maybe building up to the end of it...
choice = input("> ")
if choice == "1":
    print("There is a big bear here eating cheesecake.\nWhat do  you do??")
    print("1. Take the cheesecake")
    print("2. Scream at the bear")
    choice = input("> ")
    if choice == "1":
        print("The bear eats your face off. Good job!!")
    elif choice == "2":
        print("The bear tears you limb by limb")
    else:
        print(f"Well, doing {choice} is probably better")
        print("Bear runs away")
elif choice == "2":
    print("You stare at the endless abyss at Cthulu's retina")
    print("1. Blueberries\n2. Yellow jacket clothespins\n3. Understanding revolvers yelling melodies")
    choice = input("> ")
    if choice == "1" or choice == "2":
        print("Congrats your mind survives powered by the mind of jello")
        print("Good job")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good Job")
else:
    print("You stumble upon and fall on a knife and die. Good Job")
