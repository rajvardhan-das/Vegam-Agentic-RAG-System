import re
from collections import Counter


def tokenize(text: str):
    return re.findall(r"\w+", text.lower())


def keyword_search(query: str, chunks: list[str], k: int = 5):
    """
    Simple TF-style keyword overlap scoring
    """

    q_tokens = tokenize(query)
    q_counter = Counter(q_tokens)

    scores = []

    for chunk in chunks:
        c_tokens = tokenize(chunk)
        c_counter = Counter(c_tokens)

        score = 0
        for word in q_counter:
            score += min(q_counter[word], c_counter.get(word, 0))

        scores.append((score, chunk))

    scores.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scores[:k]]
