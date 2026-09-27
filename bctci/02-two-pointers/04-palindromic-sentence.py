def palindromic_sentence(s):
    left, right = 0, len(s) - 1
    while right > left:
        while left < len(s) and not s[left].isalpha():
            left += 1
        while right > -1 and not s[right].isalpha():
            right -= 1
        if left < len(s) and right >= 0 and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def run_tests():
  tests = [
      # Example from the book
      ("Bob wondered, 'Now, Bob?'", True),
      # Additional test cases
      ("", True),
      ("a", True),
      ("A man, a plan, a canal: Panama", True),
      ("race a car", False),
      ("Was it a car or a cat I saw?", True),
      ("hello", False),
      (".,?!'", True),
  ]
  for s, want in tests:
    got = palindromic_sentence(s)
    assert got == want, f"\npalindromic_sentence({s}): got: {
        got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()