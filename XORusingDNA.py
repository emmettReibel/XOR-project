rule1 = ['C', 'T', 'A', 'G']


def encodeDNA(character):
  charIndex = rule1.index(character)
  return '{0:02b}'.format(charIndex)


def decodeDNA(binary):
  charIndex = int(binary, 2)
  return rule1[charIndex]

def XOR (bit1, bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"

def XORonByte (byte, key):
    encryptedByte = ""
    for bit in range(len(byte)):
        encryptedByte += (XOR(byte[bit], key[bit]))
    return encryptedByte
# finish the following function
def XOR_DNA(plainDNA, keyDNA):
  ePlain = encodeDNA(plainDNA)
  eKey = encodeDNA(keyDNA)
  
  eDNA = ""
  for base in range(len(plainDNA)):
    eDNA += XORonByte(ePlain[base], eKey[base])
  # return the encoded DNA based on the key and rule
  return decodeDNA(eDNA)

  # EXTRA CREDIT
print(encodeDNA("C"))
print(XOR_DNA("A", "C"))



# MODIFY THE METHODS SO THAT USERS CAN CHOOSE FROM THE EIGHT POSSIBLE DNA RULES
# TRY TO FIGURE OUT THE RULES YOURSELF FIRST! IF YOU GET STUCK COME ASK ME :)
# REMEMBER WATSON & CRICK SAYS A PAIRS WITH T & G PAIRS WITH C
