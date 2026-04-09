from chain import build_rag_chain

rag_chain = build_rag_chain()

while True:
    question = input("Enter a question: ")
    response = rag_chain.invoke(question)
    print(response)
    print("--------------------------------")
