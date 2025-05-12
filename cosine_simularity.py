import numpy as np

def cosine_similarity(v1, v2):
    # Ensure vectors have the same dimensions
    if v1.shape != v2.shape:
        raise ValueError("Arrays must be the same shape")

    # Flatten in case inputs are matrices
    v1_flat = v1.flatten()
    v2_flat = v2.flatten()

    # Dot product of the vectors
    dot_product = np.dot(v1_flat, v2_flat)
    
    # Magnitude (Euclidean norm) of each vector
    magnitude1 = np.sqrt(np.sum(v1_flat**2))
    magnitude2 = np.sqrt(np.sum(v2_flat**2))

    # Handle edge case: zero magnitude
    if magnitude1 == 0 or magnitude2 == 0:
        raise ValueError("Vectors cannot have magnitude 0")
    
    # Cosine similarity = dot product / product of magnitudes
    return round(dot_product / (magnitude1 * magnitude2), 3)


v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(cosine_similarity(v1, v2))
