import os

def load_documents(folder_path):
    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, "r") as f:
                text = f.read()

            document = {
                "content": text,
                "source": file_name
            }

            documents.append(document)

    return documents


if __name__ == "__main__":
    docs = load_documents("data")

    # milestone check
    print(docs[0])
