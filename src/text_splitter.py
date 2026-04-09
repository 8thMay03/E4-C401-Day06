from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(
    documents: list,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list:
    """Split documents into smaller chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunk(s)")
    return chunks
