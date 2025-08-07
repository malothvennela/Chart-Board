from sklearn.metrics.pairwise import cosine_similarity
import torch

def find_best_match(usser_query,peompts,responses,embeddings,model):
    query_embedding=model.encode([user_query],)