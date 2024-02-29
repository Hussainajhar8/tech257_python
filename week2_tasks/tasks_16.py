# TASK: Write a 'Hero story' Python script
# The task
# First part
# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'
story1 = {
    "start": "In a big city called Metropolis, there was a guy named Alex. He had a job in an office during the day, but at night, he turned into a hero called Shadowstrike. With quick moves and a big heart, he kept the city safe from bad guys.",
    "middle": "One night, Shadowstrike found out about a bad plan by a mean villain named Darkmind. Darkmind wanted to make the city chaotic. Shadowstrike was determined to stop him. He faced dangerous traps and fought lots of bad guys, but he didn't give up.",
    "end": "Finally, after a big fight, Shadowstrike beat Darkmind. The city cheered for their hero. Shadowstrike went back to his normal life, but he knew he'd always be ready to protect Metropolis as Shadowstrike, the hero of the city."
}
# Print the entire dictionary
print(story1)
# Print the type of your dictionary
print(type(story1))
# Print only the keys
print(story1.keys())
# Print only the values
print(story1.values())
# Print the individual values using the keys (individually, lots of print commands)
print(story1["start"], story1["middle"], story1["end"])
# Now, let's add a new key:value pair:
# 'hero': yourSuperHero
story1.update({"hero": "Shadowstrike"})
# Hints:
# THE MORE CREATIVE THE BETTER
# If time
# Improve the program. For example, can you make it a "Choose your own adventure" story?
print("Welcome, we want you to write a story and choose your own adventure")
start = input("Write the start of your story")
middle = input("Write the middle of your story")
end = input("Write the end of your story")

new_story = {
    "start": start,
    "middle": middle,
    "end": end
}

print(new_story["start"], new_story["middle"], new_story["end"])