name = "Dominion"
# print(name[0])    # first letter
# print(name[-1])   # last letter
# print(name[2])    # 3rd letter

# slicing 
# ai = "claude"
# print(ai[:4])
# print(ai[1:])
# print(ai[-3:])

# name = "  Dominion  "

# print(name.upper())      # "  DOMINION  "  — all uppercase
# print(name.lower())      # "  dominion  "  — all lowercase
# print(name.strip())      # "Dominion"      — removes leading/trailing whitespace
# print(name.replace("o", "0"))   # "  D0min10n  " — replaces every match

# name = "  HELLo WORLD       "
# clean_name = name.strip().lower().replace("world","people")
# print(clean_name)   

#excercise 1 
# working on reversing strings 
# words = "i love python"
# words = words.split() 
# reverse = words[::-1]
# reverse = " ".join(reverse)
# print(reverse)

# excercise 2
#counting the leanght of a raw sentence 
word = "hello how are you"
word = word.split()
print(len(word))