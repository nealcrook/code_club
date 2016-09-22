Here are a set of Python projects that I used for teaching a coding club at my
local primary school.

I wrote python3_intro as a preliminary introduction before diving in to the
other projects. We all went through these together to get the hang of using the
python shell and the editor. After that we did lesson1.pdf - lesson4.pdf from
CodeClub.org (not reproduced here) which all used Python focussed on turtle
graphics - finishing up with a nice fractal-drawing program. What's included
here is my week-by-week attempt to dream up a new project.

My students were Yr4, 5 & 6. Very enthusiastic. They greatly enjoyed the Turtle
projects (so much so that I though about developing some more projects using
Turtle graphics). In general it took them between 1 and 2 sessions to do a
project, which meant that some progressed through more quickly than others. I
tried to slow them down my adding "extras" at the end of the projects that I
created.

I think that it's important to provide hard-copy printout of the project
work-sheet. I started each session with a recap of what we'd learned and some
background on the new project. However, each work-sheet aims to be
self-contained and complete - you could simply type in the code exactly as shown
in the work-sheet.



This is the sequence in which I used them:

1. my_cc_proj_0_python3_intro -- we went through this together and
tried out some of the examples.
2. lesson1.pdf -- Turtle Power (from CodeClub.org)
3. lesson2.pdf -- Teaching Turtles (from CodeClub.org)
4. lesson3.pdf -- Secret Codes (from CodeClub.org)
5. lesson4.pdf -- Turtles all the way down (from CodeClub.org)
6. my_cc_proj_1_tables -- times table trainer.
7. my_cc_proj_2_birds_on_a_wire -- random packing on a line.
8. my_cc_proj_3_igpay_atinlay -- pig latin
9. my_cc_proj_4_curiouser_and_curiouser -- processing text
10. my_cc_proj_8_monty_hall -- statistical modelling
11. my_cc_proj_9_turtle -- a Turtle graphics crib-sheet but with no
structured project
12. my_cc_proj_11_adventure -- data-driven programing. For this you need to provide the students with the included file "RPG.py"
13. my_cc_proj_999_at_home -- an end-of-term handout I used to
encourage the students to do some programming at home



For each of my projects there is a directory containing:

* a .pdf file. This is the handout to the students. The more recent
code-club material seems to be orientated to being viewed on a screen
and having the code "cut" and then "pasted" into the IDLE editor. I
don't like that approach for two reasons. Firstly, I think that typing
the code in, making mistakes, spotting and fixing them is an essential
part of learning to program. Second, the student will have the Python
shell, the IDLE editor and the Turtle window all open and there tends
not to be enough screen space to have the learning material on display
as well. Of course, it's a pain having to print them out. For my code
club I ended up printing them myself at home because the school kept
saying they'd do it but didn't.

* an .odt file. This is the libreoffice (http://www.libreoffice.org)
document from which the .pdf was generated. You'll only need this if
you want to modify anything

* several .py files. These are the set of programs that evolve towards
the final solution. This is the code that I wrote for the project and
which I then "pasted" into the handout. You don't need these because
you can type in all the code yourself. Likewise, you should not provide
this to the students becasue (in my opinion) typing in the code is an
essential part of the learning process.

In addition:

* for curiouser_and_curiouser there are project gutenberg
(http:/www.gutenberg.org) texts of Alice In Wonderland and Les
Miserables which you need to make available on a shared drive
* for adventure there is a file RPG.py which you need to make
available on a shared drive - this is the starting point for the
project
* for adventure there is also a subdirectory containing a Python
implementation of Colossal Cave Adventure. You might like to make this
available on a shared drive; the handouts explain how to run it.

All of these examples assume use of Python3 so I hope that is what you have
installed. If you are using Python2 some may work and some will not. If you want
to use them with Python2 let me know and I will see if I can make Python2
versions of them projects.

In the school where I ran the code club, there was a foolish firewall setting on
the machines which prevented IDLE from working correctly unless the students
were logged in using a (more privileged) supply teacher login account. The
problem showed itself as an error message when trying to run IDLE (an error
message about not being able to open a "socket" which the the mechanism that
IDLE uses to communicate between the python shell and the editor window). There
is a work-around for this problem so if it affects you let me know and I will
write up the work-around.

If you work through each of these projects you should be in a good position to
support your students in doing the same. My experience was that most of the
students dived straight to typing in the code fragments and only read the
explanatory text when strictly necessary - so I tended to start the club with 5
minutes chat in front of the white-board. For example, for the secret codes I
wrote up a coded message on the board and worked with the students to try to
crack it.

I'll be interested in any constructive feedback on any of the projects. If you
find them useful I could even be persuaded to develop some more (I have a list
of ideas and several part-finished projects).

Part-finished projects (not included here)

````
my_cc_proj_5 - noughts and crosses
my_cc_proj_6 - draw a maze
my_cc_proj_7 - creative writing
my_cc_proj_10 - paint
my_cc_proj_11 - square
````
