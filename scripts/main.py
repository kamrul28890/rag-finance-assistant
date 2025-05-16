from rag_pipeline import get_rag_chain

def run():
    chain = get_rag_chain()
    print("💬 Finance Assistant Ready. Type your question (type 'exit' to quit):")
    while True:
        query = input("\n> ")
        if query.lower() in ["exit", "quit"]:
            break
        result = chain.invoke({"query": query})
        print("\nAnswer:", result['result'])

if __name__ == "__main__":
    run()
