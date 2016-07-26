#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import codecs

sources = {
  "motion de droite (12/05/2016)": "sources/motion-droite-mai.txt",
  "motion de droite - vote (12/05/2016)": "sources/motion-droite-mai.vote.txt",
  "motion des gauches (12/05/2016)": "sources/motion-gauches-mai.txt",
  "motion (28/06/2016)": "sources/motion-juillet.txt",
  "tribune jdd": "sources/tribune-jdd.txt",
  "motion citoyenne": "sources/motion-juillet2.txt"
}

def parse_txt1(file):
  f = codecs.open(file, "r", "utf-8")

  txt = f.read()

  result = txt.split(",")
  result = [ item.strip() for item in result ]

  # print [ x.split(" ")[-1] for x in result ]

  sorted(result, key=lambda x: x.split(" ")[-1])

  return result


def parse_txt2(file):
  f = codecs.open(file, "r", "utf-8")

  txt = f.read()

  result = txt.strip()

  result = result.split("\n")

  if "," in txt:
    result = [ x.split(",")[0] for x in result ]

  sorted(result, key=lambda x: x.split(" ")[-1])

  return result

#print parse_txt1("./sources/tribune-jdd.txt")
#print len(parse_txt2("./sources/motion-droite-mai.vote.txt"))

deputes = parse_txt2("sources/deputes.txt")

df = pd.DataFrame(index=deputes, columns=sources.keys())

for col, l in sources.iteritems():
  names = parse_txt2(l)
  print col
  df.ix[names, col] = "x"

df = df.fillna("")

print df.head()

df.to_csv("data/motions.csv", encoding="utf-8")
