#!/usr/bin/python3

password = input("Please enter your password: ")

import hashlib

def hash_password(password):

  # Encode the password string to bytes
  password_bytes = password.encode('utf-8')

  # Create a SHA-256 hash object
  sha256_hash = hashlib.sha256()

  # Update the hash object
  sha256_hash.update(password_bytes)

  # hexadecimal representation of the hash
  hashed_password = sha256_hash.hexdigest()

  return hashed_password

# Example usage:
password_to_hash = password
hashed_password = hash_password(password_to_hash)
print("The SHA-256 hash of " + password_to_hash + " is: " + hashed_password)
