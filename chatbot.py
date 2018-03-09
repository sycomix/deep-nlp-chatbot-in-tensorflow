""" Deep NLP Chatbot """

import numpy as np
import re
import tensorflow as tf
import time

# Importing the dataset
lines = open('./dataset/cornell movie-dialogs corpus/movie_lines.txt', encoding='utf-8',
             errors='ignore').read().split('\n')
conversations = open('./dataset/cornell movie-dialogs corpus/movie_conversations.txt', encoding='utf-8',
                     errors='ignore').read().split('\n')

# Dictionary that maps each line and its id
id_to_line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id_to_line[_line[0]] = _line[4]
