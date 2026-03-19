import json

with open("../data/questions_riasec.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

scores = {"R":0,"I":0,"A":0,"S":0,"E":0,"C":0}

for q in questions:
    rep = input(q["question"] + " (o/n) : ")
    if rep.lower() == "o":
        scores[q["type"]] += 1

print("\nVotre profil RIASEC :")
for k, v in scores.items():
    print(k, ":", v)
    