from library.aes_encryption import decrypt


key = '<Answer to question asked in class>'

cypher_text = ('wau1qbrSmT/Zc5pGBW1222/24nBeOmhbJbsgmZgvV2ETRUzFkkO7r'
               'WeDGzBf5ppUGNCAIspbf49W59EYEW21p0ghY2teT3PEO3FNwSqJyQ'
               'X4rs71lbnK41IOTtM2VXWeku0eheQt5t5n9xd3TwrevA==')
plain_text = decrypt(key, cypher_text)
print(plain_text)