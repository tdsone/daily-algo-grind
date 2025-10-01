import pytest

"""
Ok, what's the general idea behind Needleman-Wunsch? 

It's an alignment algorithm that uses DP to derive an alignment 
between two sequences that minimises their Levenshtein distance.

Levenshtein distance: 
- Minimal hamming distance between two aligned strings when gaps are allowed

How does the DP approach work here? 

First key insight: let's say we have FLIEGEN and LIEBE as a and b to be aligned.
Then, any alignment will end in one of three ways: 
1. matching on the last char: 
...N
...E
2. matching gap and last char of a: 
...N
...-
3. matching gap and last char of b:
...-
...E

There is no possible other ending. If it was: 
...-
...- 

we could simply remove that to get an alignment of equal quality.

You can also recognize how this allows us to formulate some kind of recursion here:
The optimal alignment will end with one of the three endings. 
Thus, we just have to find the optimal alignment of strings, for each of the possible endings.
To do so, let's find a score S that describes optimal: 

S = min(match, up, down) where match is case1, up is case2 and down is case3

-> lower score is better
define 
match = 0 + score(a[0:n-2], b[0:m-2]) # i.e. the score of the best alignment when everything is equal up to here
up = gap_penalty + score(a[0:n-2], b[0:m-1])
down = gap_penalty + score(a[0:n-1], b[0:m-2])

Ok, what's the issue with this? Potentially, we compute score(a[0:i], b[0:j]) many times. 
We now have two options: 
- compute score once and cache
- transform into dp

As computing score once is trivial with @cache, let's instead think about how we can transform this into DP problem: 

let len(a) = N and len(b) = M

We realise that we compute N*M scores: 
e.g.: 
for i in range(0, N): 
    for j in range(0, M):
        score(a[0:i], b[0:j])
"""


class Alignment:
    pass


def needleman_wunsch(a: str, b: str) -> Alignment:
    pass


TEST_CASES = [("ACGATCAGCGACTACG", "ACGATCAGCGACTACG")]


@pytest.mark.parametrize("a, b, expected", TEST_CASES)
def test_needleman_wunsch(a, b, expected):
    assert needleman_wunsch(a, b) == expected


if __name__ == "__main__":
    pass
