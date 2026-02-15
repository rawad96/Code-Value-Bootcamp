import pytest
from aes_encryption import encrypt, decrypt


class TestEncryptor:
    key = 'hPaGuMHLLGwqEqttJRzELDhAmjvGWYH8SPpbAV5T7'
    plaintext = 'Hello World'

    def test_functionality(self):
        cypher_text = encrypt(self.key, self.plaintext)
        assert cypher_text is not None
        assert isinstance(cypher_text, str)

        decrypted = decrypt(self.key, cypher_text)
        assert decrypted == self.plaintext
