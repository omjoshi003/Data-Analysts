sentence = "HELLO MY NAME IS OM JOSHI"
print(sentence)

words = sentence.split()
print(words)

reversed_sentence = ""
print(reversed_sentence)
# each word star with i add space and go to reversed_sentence
for i in words:
    reversed_sentence = i + " " + reversed_sentence

print(reversed_sentence)
