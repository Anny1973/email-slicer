import re

def slice_email(email):
  """Slices an email address and returns the username and domain."""
  match = re.match(r"^(.+)@(.+)$", email)
  if match:
    username = match.group(1)
    domain = match.group(2)
    return username, domain
  else:
    return None

if __name__ == "__main__":
  email = input("Enter an email address: ")
  username, domain = slice_email(email)
  print("Username:", username)
  print("Domain:", domain)
