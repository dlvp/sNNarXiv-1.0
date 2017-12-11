import numpy as np
import matplotlib.pyplot as plt
import time
import os
import pickle
import random

with open('abstracts_out') as f:
    list_abstracts = f.read().splitlines()
with open('titles_out') as f:
    list_titles = f.read().splitlines()

title = random.choice(list_titles)
abstract = random.choice(list_abstracts)


with open('test_tex.tex','w') as f:
    f.write("\\documentclass[12pt]{article} \n \\begin{document} \n \\title{\\bf %s }\n" % title)
    f.write("\\date{\\vspace{-5ex}} \n \\maketitle \n \\begin{abstract}\n %s\n \\end{abstract}\n \\end{document}\n" % abstract)
