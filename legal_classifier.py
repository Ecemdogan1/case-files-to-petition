
def classify_dispute(texts):
    combined = " ".join(texts).lower()

    if "sözleşme" in combined or "contract" in combined:
        return "Contractual Dispute"
    if "fatura" in combined or "invoice" in combined:
        return "Payment / Debt Dispute"
    if "haksız" in combined or "tort" in combined:
        return "Tort / Unlawful Act"
    if "işçi" in combined or "employee" in combined:
        return "Labor Law Dispute"

    return "General Civil Dispute"
