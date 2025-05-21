
import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self, embedding_dim=1536):
        """
        Initializes a FAISS index for cosine similarity search.

        Args:
            embedding_dim (int): Dimension of the embedding vectors.
        """
        self.embedding_dim = embedding_dim
        # IndexFlatIP for cosine similarity (when vectors are normalized)
        self.index = faiss.IndexFlatIP(self.embedding_dim)
        self.documents = []  # To store corresponding documents/chunks

    def add_embeddings(self, embeddings, documents):
        """
        Add embeddings and their associated documents to the index.

        Args:
            embeddings (List[np.array]): List or array of embedding vectors.
            documents (List[str]): Corresponding list of text documents/chunks.
        """
        embeddings_array = np.array(embeddings).astype('float32')
        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings_array)
        self.index.add(embeddings_array)
        self.documents.extend(documents)

    def retrieve(self, query_embedding, k=5):
        """
        Retrieves top-k documents most similar to the query embedding.

        Args:
            query_embedding (np.array): Embedding vector of the query.
            k (int): Number of top results to retrieve.

        Returns:
            List of tuples: (document_text, similarity_score)
        """
        query_vec = np.array([query_embedding]).astype('float32')
        faiss.normalize_L2(query_vec)
        distances, indices = self.index.search(query_vec, k)
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(dist)))
        return results

    def size(self):
        return self.index.ntotal
