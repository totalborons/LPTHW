from sys import argv
prompt = '\t>'
script, user_name = argv
print(f"So this is the {script} script")
print(f"I'd like to ask some questions from you {user_name}")
print("Do you like me?")
liking = input(prompt)
print(f"Where do you live {user_name}")
live = input(prompt)
print(f"Which computer do you like {user_name}")
computer = input(prompt)

print(f"""
Alright so you've said {liking} about liking me.
{user_name} lives at {live} and your computer is {computer}
""")


# typical simple one
