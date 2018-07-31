# sNNarXiv-1.0
A Recurrent Neural Network to generate High Energy Theory abstracts (https://dlvp.github.io/Physics-snnarxiv/)

## Content
I uploade all the notebook to train the RNN and use it to generate text. On the other hand neither the corpus, nor the trained parameters for the RNN are attached below. For those, contact me privately.

<b>arxiv_abstracts.ipynb</b>: notebook for preprocessing of titles and abstracts and extraction of formulas

<b>abstract_word_rnn.ipynb</b>:  notebook that contains the TensorFlow code to train the RNN that will generate abstracts

<b>title_word_rnn.ipynb</b>: notebook that contains the TensorFlow code to train the RNN that will generate titles

<b>abstract_word_rnn_gen.ipynb</b>: notebook which used the trained RNN to generate abstracts

<b>title_word_rnn_gen.ipynb</b>: notebook which used the trained RNN to generate titles

<b>abstracts_out</b>: sample of generated abstracts

<b>titles_out</b>: sample of generated titles

<b>generate_tex.py</b>: randomly picks an abstract from abstracts_out and a title from titles_out and output a compilable tex file
