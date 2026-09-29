def most_frequent_octet(ips):
    first_octet = dict()
    most_common_first_octet = ("", 0)
    for ip in ips:
        octets = ip.split(".")
        if octets[0] in first_octet:
            first_octet[octets[0]] += 1
        else:
            first_octet[octets[0]] = 1
        if first_octet[octets[0]] > most_common_first_octet[1]:
            most_common_first_octet = (octets[0], first_octet[octets[0]])
    return most_common_first_octet[0] if ips else None

def run_tests():
  tests = [
      # Example
      (["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"], "203"),
      # Additional test cases
      ([], None),
      (["192.168.1.1"], "192"),
      (["10.0.0.1", "10.0.0.2", "192.168.1.1"], "10"),
      (["172.16.0.1", "172.16.0.2", "172.17.0.1", "172.16.0.3"], "172"),
  ]
  for ips, want in tests:
    got = most_frequent_octet(ips)
    assert got == want, f"\nmost_frequent_octet({ips}): got: {
        got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()