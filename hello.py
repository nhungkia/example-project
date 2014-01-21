from hello.math import name_length, word_count

name = raw_input("What's your name? ").strip()

while not name:
    name = raw_input("No really, what's your name? ").strip()

wc = word_count(name)
cc = name_length(name)

print "Hello, " + name + "."
print "You have a {}-word name with {} characters.".format(wc, cc)
