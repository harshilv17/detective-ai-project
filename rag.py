from vector import search

def answer_question(query):
    # Retrieve relevant documents
    retrieved_docs = search(query, k=2)

    # Build context string with source labels
    context = ""
    for doc in retrieved_docs:
        context += f"\nSource: {doc['source']}\n{doc['content']}\n"

    # Simple grounded answer construction (no LLM needed)
    answer_parts = []

    for doc in retrieved_docs:
        sentences = doc["content"].split(".")
        for sentence in sentences:
            if any(word.lower() in sentence.lower() for word in query.split()):
                cleaned = sentence.strip()
                if cleaned:
                    answer_parts.append(f"{cleaned}. ({doc['source']})")

    if not answer_parts:
        return "No relevant information found in the retrieved documents."

    return " ".join(answer_parts)


if __name__ == "__main__":
    user_question = input("Enter your question: ")
    answer = answer_question(user_question)
    print("\nAnswer:")
    print(answer)
