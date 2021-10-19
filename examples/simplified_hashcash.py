"""
A simplified example of a hashing algorithm which may be used
as a proof of work for a blockchain
"""


from hashlib import sha256

# We want that the hash of a some integer `x` multiplied by another `y`
# must end in 0
# Eg.: hash(x * y) = ac1231....0

x = 5
y = 0  # we don't know the exact value yet


# example of a usage of hexdigest method:
# >>> sha256(f'blablabla'.encode()).hexdigest()
# '492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d'
#
# another example:
# >>> sha256(f'{5*21}'.encode()).hexdigest()[-1]
# '0'

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'The solution is  y = {y}')
