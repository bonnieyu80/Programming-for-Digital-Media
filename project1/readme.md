# Project Description

[Free Project 7-1] Modify “Stochastic Texts”
When I invited you to modify JavaScript programs, one of them was a classic, Theo Lutz’s “Stochastic Texts” from 1959. I have made this program available, in reimplemented form, not only in JavaScript but also in Python. Find it here and download it:

nickm.com/memslam/stochastic_texts.py
Open the  le in a text editor. copy the code, and paste it into Jupyter Notebook. Then, modify it, as you did when you modi ed a JavaScript program, to make a text generator of your own that is based on this one.

#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['COUNT', 'STRANGER', 'LOOK', 'CHURCH', 'CASTLE', 'PICTURE',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['OPEN', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
              'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

[Free Project 7-2] Modify and Improve a Starter Program
Use one of this chapter’s “starter programs” as a basis for your work, develop a modi ed program that you believe improves on the version presented here. As with the original program, the program you create should be simple and should do one simple thing.

[Free Project 7-3] Write a Starter Program
Create an alternative “starter program” of similar simplicity to the four discussed in this chapter. The program you create should do only one simple thing. In a short paragraph, you should justify this program as one that is good at being an initial introduction to programming and computation.
Those with existing programming background may wish to try using another programming language, but the standard way to proceed is by working in Python.
To complete this project, write a new program, starting with a blank Jupyter Notebook cell, or change something about how an existing program computes. Having done this exercise of replacing “Hello World” with a different text, go on to write another program for your free project, one that doesn’t just involve exchanging one string for another, but which also involves some additional, different sort of computation.
For instance, there was a 1994 Saturday Night Live skit, “Total Bastard Airlines,” that presented the scene of passengers exiting an airplane. As the passengers left, members of the  ight crew repeatedly said “Buh-bye!” The actors playing passengers ran around the set, getting on the plane again and exiting the plane again, so that the  ight crew was standing there and saying, apparently without end, “Buh-bye.”
To begin with, write a program that says—actually, displays on the screen, using print()—“Buh-bye” some number of times, using iteration.To get a program to say “Buh-bye” an unbounded number of times, it is necessary to do something computationally different than is seen in “Hello World” or in the bounded iteration of a for loop. The eternal “Buh-bye” program, with a justi cation for why it is a
Draft of 2019-09-08 For the exclusive use of John Murray’s UCF class. Please do not circulate!
valuable introduction to computing, would be a legitimate free project that involves taking a step beyond what is outlined in this chapter. This book has not yet described how to write such a program, but by experimenting with the code provided so far and poking around online, it should be possible for even completely new programmers to tweak existing programs and to do something computationally new. A good way to start may be to see how code from the four short starter programs can be combined. You should also be aware that the Jupyter Notebook environment may not be the best one for running programs with in nite loops! You probably will want to use the method of writing a program in a text  le, as introduced in section 7.2, “Hello World.”
Whether you pursue this sort of project or another, remember, that the goal is not to write an elaborate program, but to write a very simple new program that can be justi ed as a good introduction to programming and that does something computationally different from the programs introduced so far.