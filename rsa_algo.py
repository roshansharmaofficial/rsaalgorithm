import random  # so that we don't have to static prime numbers
import math

# defining a helper function to check whether the no. is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:  # is not a prime no. since it's divisible by i
            return False
    return True


# helper function to generate prime no.
def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse doesn't exist")


# Now defining the p, q prime nos.

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)
while p == q:
    q = generate_prime(1000, 5000)

# getting the product n = p*q
n = p * q

# Now getting the totient function
phi_n = (p - 1) * (q - 1)

# generate public key e for encryption
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

# Generation of the Private Key
d = mod_inverse(e, phi_n)

print("public key:", e)
print("private key:", d)
print("n:", n)
print("phi(n):", phi_n)
print("P:", p)
print(" Q:", q)

message = "Hey Roshan!"

message_encoded = [ord(ch) for ch in message]

# Convert Message to Cipher Text: C = (M^e) mod n
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print("Cipher Text:", ciphertext)

# encrypting a message

message = "Hey Roshan Sharma"

#Decrypting in the receiver's end
message_encoded = [pow(ch, d, n) for ch in ciphertext]

#Concatenate the Encoded Message
message = "".join(chr(ch) for ch in message_encoded )

print("Decrypted Message:", message)
