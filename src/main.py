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
# déterminer le profil dominant
dominant = max(scores, key=scores.get)

print("\nProfil dominant :", dominant)
descriptions = {
    "R": "Réaliste : aime le concret et les activités pratiques",
    "I": "Investigateur : aime analyser et comprendre",
    "A": "Artistique : aime créer et imaginer",
    "S": "Social : aime aider et accompagner",
    "E": "Entreprenant : aime diriger et convaincre",
    "C": "Conventionnel : aime organiser et structurer"
}

print("\nInterprétation :")
print(descriptions[dominant])

    