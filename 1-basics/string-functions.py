name="Zartab"
print(name)
print(type(name))
# print(dir(name))

sentence='India is my country.'
print(sentence);

sentence="I don't know where they are"
print(sentence);

# Multi Line String 

paragraph="""
India is my country.
All Indians are my brothers and sisters
I Love my country
"""

print(paragraph)

word="kitkat"
print(word)
print(word[1])
print("Word[1:3]",word[1:3])

# print(word[8])
#     print(word[8])
#           ~~~~^^^
# IndexError: string index out of range


# Clone

print("Word[:]",word[:])

# Trimming

word_with_spaces="   Hello World   "
print(word_with_spaces)
print("Lenght",len(word_with_spaces))
word_with_spaces=word_with_spaces.strip()
print(word_with_spaces)
print("Lenght",len(word_with_spaces))

# Casing

company="code with z"
print("Company:",company)
company=company.upper()
print("Company:",company)

sentence="I AM HAPPY TO MAKE THIS VIDEO"
print("Sentence:",sentence)
print("Sentence:",sentence.lower())

sentence=sentence.capitalize()
print("Sentence:",sentence)

sentence=sentence.title()
print("Sentence:",sentence)

# Split a String

line1="1,Tom,IT,Developer,30000"
line2="Hello how are you"

data1=line1.split(",")
print(data1)

data2=line2.split(" ")
print(data2)

# Count 

name="Zartab"
a_count=name.count("a")
print("a has repeated for ",a_count,"times in",name)

# Starts and Ends with

print("Starts with z",name.startswith("z"))
print("Starts with Z",name.startswith("Z"))
print("Starts with a",name.startswith("a"))
print("Starts with Zar",name.startswith("Zar"))
print("Ends with b",name.endswith("b"))
print("Ends with B",name.endswith("B"))
print("Ends with x",name.endswith("x"))
print("Ends with tab",name.endswith("tab"))

# Escape Characters 

#  \n -- new line
#  \t -- tab
#  \\ -- backslash
#  \" -- double quotes 

text="This is a backslash \\"
print(text)
text="These are two backslashes \\\\"
print(text)
text=" I make videos for \"Code With Z\""
print(text)











