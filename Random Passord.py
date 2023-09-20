import random

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "$%&*=?+!_-<>@[]()"

use_for = alphabet_lower + alphabet_upper + number + symbols
length_for_pass = 16

password = "".join(random.sample(use_for, length_for_pass))
print("Your new password is:", password)