#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

twitter = pd.DataFrame.from_csv("sources/deputes.twitter.regardscitoyens.csv", encoding="utf-8")

twitter.reset_index(inplace=True)
twitter.set_index("nom", inplace=True)

print twitter.head()

deputes = pd.DataFrame.from_csv("sources/deputes.txt", encoding="utf-8", sep="\t", header=None)

# création du tableau

df = pd.DataFrame(index=deputes.index, columns=["twitter"])

df["twitter"] = twitter["twitter"]

df.to_csv("data/twitter.temp.csv", encoding="utf-8")
