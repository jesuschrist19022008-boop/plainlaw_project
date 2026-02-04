import json
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1",
    device=-1
)

labels = [
    "Payment/Terms",
    "Termination/Renewal",
    "Liability/Limitations",
    "Data Privacy/Usage",
    "Penalties/Fees",
    "Arbitration/Dispute Resolution",
    "User Obligations/Restrictions",
    "Warranty/Guarantees"
]

def classify_clauses(clauses):
    results = []
    for clause in clauses:
        res = classifier(clause, candidate_labels=labels)
        results.append({
            "clause": clause,
            "label": res["labels"][0],
            "score": float(res["scores"][0])
        })
    return results

if __name__ == "__main__":
    with open("clauses.json", "r", encoding="utf-8") as f:
        clauses = json.load(f)

    classified = classify_clauses(clauses)

    with open("classified_clauses.json", "w", encoding="utf-8") as f:
        json.dump(classified, f, indent=4)

    print("Classification done! Output saved in classified_clauses.json")
