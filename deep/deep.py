

comprehension = ''' “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams
'''

# ask user a question using an input function
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " ).lower().strip()
#note that all user input is a string until otherwise converted
# compare input with system option; "42" , "forty-two", "forty two"
options = ["42" , "forty-two", "forty two"]
# logic to compare input with system option
if question in options:
    print ("Yes")
else: print ("No")
# output function to output result
