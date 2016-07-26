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

  def sort(x):
    r = x.split(" ")[-1]

    if x.split(" ")[-2] == "Le" or x.split(" ")[-2] == "La":
      r = x.split(" ")[-2] + " " + r

    return r

  sorted(result, key=sort)

  return result

#print parse_txt1("./sources/tribune-jdd.txt")
#print len(parse_txt2("./sources/motion-droite-mai.vote.txt"))

deputes = pd.DataFrame.from_csv("sources/deputes.txt", encoding="utf-8", sep="\t", header=None)

# création du tableau

df = pd.DataFrame(index=deputes.index, columns=sources.keys())


# intégration des signatures/votes

for col, l in sources.iteritems():
  names = parse_txt2(l)
  print col
  df.ix[names, col] = "x"

df = df.fillna("")

# intégration des groupes parlementaires

df["groupe parlementaire"] = deputes.iloc[:, 3]


# intégration des partis politiques

partis = pd.DataFrame.from_csv("sources/deputes_parti.txt", sep="\t", header=None, encoding="utf-8", index_col=None)

partis["id"] = partis[1] + " " + partis[0]
print partis["id"]

partis.set_index("id", inplace=True)
print partis
df["parti politique"] = partis[3]

print df.head()
print len(df)

df.to_csv("data/motions.csv", encoding="utf-8")
