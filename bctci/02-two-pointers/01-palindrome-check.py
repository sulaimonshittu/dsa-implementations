def palindrome(s):
    start, end = 0, len(s) - 1
    while end > start:
        if s[end] == s[start]:
            start += 1
            end -= 1
        else:
            return False
    return True

def run_tests():
  tests = [
      # Example from the book
      ("level", True),
      ("naan", True),
      # Additional test cases
      ("", True),
      ("a", True),
      ("ab", False),
      ("abc", False),
      ("abba", True),
      ("abcba", True),
  ]

  for s, want in tests:
    got = palindrome(s)
    assert got == want, f"\npalindrome({s}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()