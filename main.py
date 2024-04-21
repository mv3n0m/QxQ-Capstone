from src import text_to_bits, bits_to_text
from src.encryption import encrypt_message
from src.decryption import decrypt_message
from random import choices

message = "My journey with The Coding School - Qubit by Qubit, has been truly unique and exceptional."

message_bits = text_to_bits(message)
num_bits = len(message_bits)

base_options = ['Z', 'X']

encryption_bases = choices(base_options, k=num_bits)
encrypted_circuit = encrypt_message(message_bits, num_bits, encryption_bases)

private_key = 'some random key'
decryption_bases =  choices(base_options, k=num_bits)
decrypted_bits = decrypt_message(encrypted_circuit, num_bits, private_key, decryption_bases)

##### Comparing bases #####
encrypted = []
decrypted = []
for idx in range(num_bits):
    if encryption_bases[idx] == decryption_bases[idx]:
        encrypted.append(message_bits[idx])
        decrypted.append(decrypted_bits[idx])

###########################

#### Checking for Eve ####
if encrypted[0] == decrypted[0]:
    encrypted = encrypted[1:]
    decrypted = decrypted[1:]
    print('Keys are not compromised.')
else:
    print('Eve was listening, we need to use a different channel!')
###########################


######### I wanted to retrieve the actual message string passed in the beginning,
# however I am failing to do so.
# I might need someone's help to understand if this is possible. ################

# decrypted_message = bits_to_text(decrypted_bits)
# print(decrypted_message)
