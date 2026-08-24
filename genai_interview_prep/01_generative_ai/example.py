"""
Autoregressive Text Generation - Toy N-Gram Language Model   (Topic: Generative AI)

Problem:
Demonstrate, with no external dependencies, the actual mechanism behind
Fig. 1 in interview_qa.md: context -> model -> probability distribution over
the next token -> sample -> append -> loop, until a stop condition. A real
LLM does this with a transformer's learned weights; this toy version does it
with n-gram character frequency counts, so the loop itself is easy to trace
by hand while debugging.

Approach:
- Build a frequency table: for every (n-1)-character context seen in the
  training corpus, count which character follows it (build_ngram_model).
- At generation time, look up the current context's distribution over next
  characters (next_char_distribution), falling back to a uniform
  distribution over the vocabulary for a context never seen in training -
  the toy equivalent of a real model "hallucinating" on out-of-distribution
  input.
- Reshape that distribution with temperature and sample one character
  (sample_with_temperature), append it to the running context, and repeat
  (generate) until a stop character or max length is reached.

Time Complexity:  O(max_length) generation steps, each an O(1) average dict
                   lookup; O(len(corpus)) to build the model.
Space Complexity: O(distinct (n-1)-character contexts x alphabet size),
                   which grows roughly exponentially with n for a fixed
                   alphabet - the toy analogue of why real models need
                   learned dense representations instead of lookup tables.
"""

import random
from collections import defaultdict, Counter


def build_ngram_model(corpus: str, n: int = 3) -> dict:
    model = defaultdict(Counter)
    padded_context = "~" * (n - 1)
    padded = padded_context + corpus
    for i in range(len(corpus)):
        context = padded[i:i + n - 1]
        next_char = corpus[i]
        model[context][next_char] += 1
    return model


def next_char_distribution(model: dict, context: str, vocab: list) -> dict:
    counts = model.get(context)
    if not counts:
        # unseen context: no learned signal, fall back to uniform -- this is
        # the toy analogue of a real model hallucinating on OOD input (see Q M2)
        return {ch: 1 / len(vocab) for ch in vocab}
    total = sum(counts.values())
    return {ch: c / total for ch, c in counts.items()}


def sample_with_temperature(distribution: dict, temperature: float) -> str:
    if temperature <= 0:
        # the limit as T -> 0+: probability mass collapses onto the single
        # most likely token, i.e. plain greedy decoding (see Q P2)
        return max(distribution, key=distribution.get)
    chars = list(distribution.keys())
    scaled = [p ** (1 / temperature) for p in distribution.values()]
    total = sum(scaled)
    probs = [s / total for s in scaled]
    return random.choices(chars, weights=probs, k=1)[0]


def generate(model: dict, n: int, vocab: list, max_length=200, temperature=1.0, stop_char=".") -> str:
    context = "~" * (n - 1)
    output = []
    for _ in range(max_length):
        dist = next_char_distribution(model, context, vocab)
        next_char = sample_with_temperature(dist, temperature)
        output.append(next_char)
        if next_char == stop_char:
            break
        context = (context + next_char)[-(n - 1):]
    return "".join(output)


if __name__ == "__main__":
    corpus = (
        "the cat sat on the mat. the cat sat on the rug. the cat ran to the dog. "
        "the dog sat on the log. the dog ran to the cat. the dog barked at the cat. "
        "the cat barked at the dog. the mat was on the rug."
    )
    vocab = sorted(set(corpus))
    n = 3
    model = build_ngram_model(corpus, n=n)

    print(f"Trained a {n}-gram model on {len(corpus)} characters, "
          f"{len(model)} distinct contexts, vocab size {len(vocab)}.\n")

    print("Same random seed, three temperatures -- watch how the SAME random\n"
          "draws lead to more (or less) varied text as temperature changes:\n")
    for seed in range(3):
        print(f"seed={seed}:")
        for temp in (0.2, 1.0, 2.0):
            random.seed(seed)
            text = generate(model, n, vocab, temperature=temp)
            print(f"  temperature={temp}: {text!r}")
