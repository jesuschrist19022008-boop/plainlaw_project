
import spacy
import json

nlp = spacy.load("en_core_web_sm")

def split_into_clauses(text):
    doc = nlp(text)
    clauses = [sent.text.strip() for sent in doc.sents]
    return clauses

if __name__ == "__main__":
    sample_text = """
    The tenant shall pay monthly rent of Rs. 10000 before the 7th of each month.
    The lease may be terminated by either party with 2 months notice.
    The landlord is not responsible for damages caused by natural disasters.
    """

    clauses = split_into_clauses(sample_text)

    # Save clauses in JSON
    with open("clauses.json", "w", encoding="utf-8") as f:
        json.dump(clauses, f, indent=4)

    print("Clauses extracted and saved in clauses.json")
