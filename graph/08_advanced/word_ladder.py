"""
Word Ladder   (Difficulty: Hard)
Asked at: Amazon, Google, LinkedIn — "graph in disguise" question

Problem:
Given a beginWord, an endWord, and a wordList, find the length of the
shortest transformation sequence from beginWord to endWord such that:
  - Only one letter can be changed at a time.
  - Each transformed word must exist in wordList.
Return 0 if no such sequence exists.

Example:
    beginWord = "hit", endWord = "cog"
    wordList  = ["hot","dot","dog","lot","log","cog"]

Flow diagram (each word is a node, edge = differs by exactly 1 letter):
    hit --- hot --- dot --- dog --- cog
                 \\         /
                  lot --- log

    Shortest path hit -> cog:  hit -> hot -> dot -> dog -> cog  (length 5)

Approach:
- The word list is an IMPLICIT graph: two words are connected if they
  differ by exactly one character. We never build this graph explicitly
  (too expensive) — instead we generate neighbors on the fly.
- Since we want the SHORTEST transformation, this is unweighted shortest
  path -> BFS.
- Neighbor generation trick: for each position in the word, try all 26
  letters instead of comparing against every other word in the list —
  turns an O(n^2 * L) neighbor search into O(L * 26) per word.

Time Complexity:  O(N * L * 26) where N = len(wordList), L = word length.
Space Complexity: O(N * L)
"""

from collections import deque
import string


def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()

        if word == end_word:
            return steps

        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                candidate = word[:i] + letter + word[i + 1:]
                if candidate in word_set and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))

    return 0


if __name__ == "__main__":
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("Shortest transformation length:",
          ladder_length(begin_word, end_word, word_list))

    print("No path case:",
          ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
