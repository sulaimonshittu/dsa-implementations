def most_shared_account(connections):
    max_seen = ("", float("-inf"))
    name_freq_map = {}
    for _, name in connections:
        if name in name_freq_map:
            name_freq_map[name] += 1
        else:
            name_freq_map[name] = 1
        if name_freq_map[name] >= max_seen[1]:
            max_seen = (name, name_freq_map[name])
    return max_seen[0] if connections else None

def run_tests():
  tests = [
      # Example
      ([("203.0.113.10", "mike"), ("208.51.100.25", "bob"),
        ("202.0.2.5", "mike"), ("203.0.113.15", "bob2")], "mike"),
      # Additional test cases
      ([], None),
      ([("1.1.1.1", "alice")], "alice"),
      ([("1.1.1.1", "alice"), ("1.1.1.2", "bob"),
        ("1.1.1.3", "alice"), ("1.1.1.4", "bob")], "alice"),
  ]
  for connections, want in tests:
    got = most_shared_account(connections)
    assert got == want or (want and got and
                           len([(ip, u) for ip, u in connections if u == got]) ==
                           len([(ip, u) for ip, u in connections if u == want])), \
        f"\nmost_shared_account({connections}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()