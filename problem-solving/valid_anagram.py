# Problem: Valid Anagram
# Approach: Dui string er protita character koto bar ashche ta gune (dictionary te) milai.
# Time: O(n)
# Space: O(1) (shudhu limited characters thake)

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False
print(is_anagram("a", "ab"))           # False