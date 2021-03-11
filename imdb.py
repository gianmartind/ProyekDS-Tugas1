# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:34:11 2021

@author: gianm
"""

#One hot encoding

import pandas as pd
import matplotlib as plt

data = pd.read_csv("E:\Kuliah\Proyek Data Science\ProyekDS-Tugas1\IMDB-Movie-Data.csv")

allGenre = set()

i = 0
while i < len(data.Genre):
    genreArray = data.Genre[i].split(",")
    for n in genreArray:
        allGenre.add(n)
    i = i + 1


zeros = [0] * len(data.Genre)
for n in allGenre:
    data['{}'.format(n)] = zeros

j = 0
while j < len(data.Genre):
    genre = data.Genre[j]
    for n in allGenre:
        if genre.find(n) != -1:
            data['{}'.format(n)][j] = 1
        else:
            data['{}'.format(n)][j] = 0
    j += 1