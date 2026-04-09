from langchain_core.embeddings import Embeddings

from config import EMBEDDING_PROVIDER, EMBEDDING_MODEL, GEMINI_EMBEDDING_MODEL


def get_embedding_model(model: str | None = None) -> Embeddings:
    """Return embedding model instance based on configured provider."""
    provider = (EMBEDDING_PROVIDER or "openai").lower()

    if provider == "gemini":
        from langchain_google_genai import GoogleGenerativeAIEmbeddings

        return GoogleGenerativeAIEmbeddings(model=model or GEMINI_EMBEDDING_MODEL)

    from langchain_openai import OpenAIEmbeddings

    return OpenAIEmbeddings(model=model or EMBEDDING_MODEL)
