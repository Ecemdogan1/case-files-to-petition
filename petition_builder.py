
def build_petition(timeline, dispute_type):
    petition = []
    petition.append("PETITION DRAFT\n")
    petition.append(f"Estimated Dispute Type: {dispute_type}\n")
    petition.append("FACTUAL BACKGROUND:\n")

    for event in timeline:
        petition.append(f"- {event['date']}: {event['description']}")

    petition.append("\nEVIDENCE:")
    petition.append("- Contracts")
    petition.append("- Invoices")
    petition.append("- Correspondences")
    petition.append("- Other case documents")

    petition.append("\nLEGAL ASSESSMENT HEADINGS:")
    petition.append("- Legal relationship between parties")
    petition.append("- Breach analysis")
    petition.append("- Damage and causation")
    petition.append("- Claims and requests")

    return "\n".join(petition)
