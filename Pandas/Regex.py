# \w: the “word character” class represents the regex range [A-Za-z0-9_], and it matches a single uppercase character, lowercase character, digit or underscore
# \d: the “digit character” class represents the regex range [0-9], and it matches a single digit character
# \s: the “whitespace character” class represents the regex range [ \t\r\n\f\v], matching a single space, tab, carriage return, line break, form feed, or vertical tab

# \W: the “non-word character” class represents the regex range [^A-Za-z0-9_], matching any character that is not included in the range represented by \w
# \D: the “non-digit character” class represents the regex range [^0-9], matching any character that is not included in the range represented by \d
# \S: the “non-whitespace character” class represents the regex range [^ \t\r\n\f\v], matching any character that is not included in the range represented by \s

# With ranges we can match any single capital letter with the regex [A-Z], lowercase letter with the regex [a-z], any digit with the regex [0-9]. We can even have multiple ranges in the same character set!
# To match any single capital or lowercase alphabetical character, we can use the regex [A-Za-z].

#The regex I love (baboons|gorillas) will match the text I love and then match either baboons or gorillas, as the grouping limits the reach of the | to the text within the parentheses.

#Fixed Quantifiers

# \w{3} will match exactly 3 word characters
# \w{4,7} will match at minimum 4 word characters and at maximum 7 word characters

# The regex roa{3}r will match the characters ro followed by 3 as, and then the character r, such as in the text roaaar.
# The regex roa{3,7}r will match the characters ro followed by at least 3 as and at most 7 as, followed by an r, matching the strings roaaar, roaaaaar and roaaaaaaar.

#Optional Quantifiers
# regex humou?r matches the characters humo, then either 0 occurrences or 1 occurrence of the letter u, and finally the letter r. 
# The regex The monkey ate a (rotten)? banana will completely match both The monkey ate a rotten banana and The monkey ate a banana.
# The regex Aren't owl monkeys beautiful\? will thus completely match the text Aren't owl monkeys beautiful?.

# Kleene star - The regex meo*w will match the characters me, followed by 0 or more os, followed by a w. Thus the regex will match mew, meow, meooow, and meoooooooooooow.
# Kleene Plus - The regex meo+w will match the characters me, followed by 1 or more os, followed by a w. Thus the regex will match meow, meooow, and meoooooooooooow, but not match mew.
# The regex My cat is a \* will completely match the text My cat is a *.
#The anchors hat ^ and dollar sign $ are used to match text at the start and the end of a string, respectively.
# The regex ^Monkeys: my mortal enemy$ will completely match the text Monkeys: my mortal enemy but not match Spider Monkeys: my mortal enemy in the wild or Squirrel Monkeys: my mortal enemy in the wild.
# The regex My spider monkey has \$10\^6 in the bank will completely match the text My spider monkey has $10^6 in the bank



