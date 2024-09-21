import re

def test_regex(regex, test_strings):
    pattern = re.compile(regex)
    results = {s: bool(pattern.match(s)) for s in test_strings}
    return results

test_strings = test_strings = [
    "",              # Empty string (should not match)
    "a",             # Single 'a' (should not match)
    "b",             # Single 'b' (should match)
    "ab",            # Simple "ab" (should match)
    "aab",           # Multiple 'a's followed by 'b' (should match)
    "aabb",          # Multiple 'a's followed by 'bb' (should match)
    "aaaab",         # Many 'a's followed by 'b' (should match)
    "bbaa",          # Starts with 'bb' then 'aa' (should not match)
    "aabbaa",        # Alternating 'a's and 'b's (should not match)
    "aaab",          # Should match based on the regex
    "baab",          # Should match
    "bba",           # Should not match (ends in 'a')
    "bb",            # Two 'b's (should not match)
    "baaab",         # Should match
    "aaabbaa",       # Should not match
    "bbbaaabb",      # Should match
    "aaabbbaaab",    # Should match
    "baa",           # Should not match (ends in 'a')
    "abab",          # Should not match
    "aaaaa",         # Should not match (no 'b')
    "bbaaab",        # Should match
    "baaaabb",       # Should match
    "b",             # Single 'b' (should match)
    "aaaaabbb",      # Should not match (too many 'b's)
    "ba",            # Should not match (ends in 'a')
    "abbbb",         # Should match
    "abbaa",         # Should not match (ends in 'a')
    "bbbb",          # Should match
    "bab",           # Should match
    "bbabb",         # Should match
    "aaabbb",        # Should not match
    "babb",          # Should match
    "bbaaaab",       # Should match
    "abbbbb",        # Should match
    "bbbbb",         # Should match
    "aaabbbb",       # Should match
    "abaaaaab",      # Should match
    "bba",           # Should not match
    "bbbbbbbbb",     # Should match
    "baaabb",        # Should match
    "aabbbb",        # Should match
    "abbbbbb",       # Should match
    "aaaaaaaab",     # Should match
    "abaaaa",        # Should not match
    "babba",         # Should not match
    "aabbaabb",      # Should match
    "abababab",      # Should not match
    "ab",            # Should match
    "bbbbaaaab",     # Should match
    "aa",            # Should not match
]



regex = r'a*b(a*)(b(baa*b|baa*b))*b'
print(test_regex(regex, test_strings))
