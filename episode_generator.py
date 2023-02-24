#import necessary modules
import os
import glob
import random
import pandas as pd
print("Hang tight, searching for the best episode!")
#list all csv files only
csv_files = glob.glob('*.{}'.format('csv'))
#concat the files together with a loop
concat_data = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
#random shuffle the dataset and take one row
shuffled = concat_data.sample(n=1)
#print statement with shuffled data
print("You should watch", shuffled['Episode'].to_string(index=False), "from", shuffled['Season'].to_string(index=False), "of", shuffled['Show'].to_string(index=False))
choice = input("Yeah, Boo, or Tie?"'\n')
#output for "Yeah"
if choice == "Yeah":
    print("Wicked! Enjoy your coffee, mom <3")
#randomly choose reponse if kids can't decide, lead to loop with yeah, boo, or tie for new suggestion
if choice == "Tie":
    print("Okay kids! Let's let the fates decide...")
    fate = ["Yeah", "Boo"]
    decide = random.choice(fate)
    if decide == "Yeah":
        print("The fates have spoken. You should watch", shuffled['Episode'].to_string(index=False))
    if decide == "Boo":
        print("The fates say Boo. Run it again, ma!")
#when original option is boo, loop to generate new suggestions with yeah, tie or boo outcomes
while choice == "Boo":
    shuffled = concat_data.sample(n=1)
    print("You should watch", shuffled['Episode'].to_string(index=False), "from", shuffled['Season'].to_string(index=False), "of", shuffled['Show'].to_string(index=False))
    choice = input("Will they watch this one?"'\n')
    if choice == "Tie":
        print("Okay kids! Let's let the fates decide...")
        fate = ["Yeah", "Boo"]
        decide = random.choice(fate)
        if decide == "Yeah":
            print("The fates have spoken. You should watch", shuffled['Episode'].to_string(index=False))
        if decide == "Boo":
            print("The fates say Boo. Run it again, ma!")
    if choice == "Yeah":
            print("Finally! Enjoy your coffee, mom <3")
            break
