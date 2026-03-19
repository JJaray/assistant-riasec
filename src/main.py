import os
from pathlib import Path
from dotenv import load_dotenv
import json
from openai import OpenAI

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("../data/questions_riasec.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

scores = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

for q in questions:
    rep = input(q["question"] + " (o/n) : ")
    if rep.lower() == "o":
        scores[q["type"]] += 1

print("\nVotre profil RIASEC :")
for k, v in scores.items():
    print(k, ":", v)

dominant = max(scores, key=scores.get)

descriptions = {
    "R": "Réaliste : aime le concret et les activités pratiques",
    "I": "Investigateur : aime analyser et comprendre",
    "A": "Artistique : aime créer et imaginer",
    "S": "Social : aime aider et accompagner",
    "E": "Entreprenant : aime diriger et convaincre",
    "C": "Conventionnel : aime organiser et structurer"
}

print("\nProfil dominant :", dominant)
print("Interprétation simple :", descriptions[dominant])

with open("../prompts/interpretation.txt", "r", encoding="utf-8") as f:
    template = f.read()

prompt = template.format(scores=scores, dominant=dominant)

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\n--- Interprétation IA ---\n")
print(response.output_text)