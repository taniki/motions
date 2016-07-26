#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json

actions = [
  "motion de droite (12/05/2016)",
  "motion de droite - vote (12/05/2016)",
  "motion des gauches (12/05/2016)",
  "motion (28/06/2016)",
  "tribune jdd",
  "motion citoyenne"
]

df = pd.DataFrame.from_csv("data/motions.csv", encoding="utf-8")

data = {}

#data["nodes"] = { action: len(df[ df[action] == "x" ]) for action in actions  }

data["nodes"] = [ { "node": i+1, "name" : action } for i, action in enumerate(actions) ]

data["nodes"] = [ { "node": 0, "name": "député.e.s" } ] + data["nodes"]

data["links"] = [
  {"source": 0, "target": 1, "value":  0},
  {"source": 0, "target": 2, "value":  0},
  {"source": 0, "target": 3, "value":  len(df[ df["motion des gauches (12/05/2016)"] == "x" ]) },
  {
    "source": 3,
    "target": 4,
    "value": len(df[ (df["motion des gauches (12/05/2016)"] == "x") & (df["motion (28/06/2016)"] == "x") ])},
  {
    "source": 0,
    "target": 4,
    "value": len(df[ (df["motion des gauches (12/05/2016)"] != "x") & (df["motion (28/06/2016)"] == "x") ])
  },
  {
    "source": 4,
    "target": 5,
    "value": len(df[ (df["tribune jdd"] == "x") & (df["motion (28/06/2016)"] == "x") ])
  },
  {
    "source": 0,
    "target": 5,
    "value": len(df[ (df["tribune jdd"] == "x") & (df["motion (28/06/2016)"] != "x") & (df["motion des gauches (12/05/2016)"] != "x") ])
  },
  {
    "source": 3,
    "target": 5,
    "value": len(df[ (df["tribune jdd"] == "x") & (df["motion (28/06/2016)"] != "x") & (df["motion des gauches (12/05/2016)"] == "x") ])
  },
  {
    "source": 5,
    "target": 6,
    "value": len(df[ (df["tribune jdd"] == "x") & (df["motion citoyenne"] == "x") ])
  }
]

with open('data/sankey.json', 'w') as out:
  json.dump(data, out, sort_keys = True, indent = 2, ensure_ascii=False)
