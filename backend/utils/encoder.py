import base64


class Encoder:
    """
    This class provides methods for encoding and decoding strings using base64 encoding.
    """

    def encode(self, string):
        """
        Encodes the given string using base64 encoding.

        Args:
                string (str): The string to be encoded.

        Returns:
                str: The encoded string.
        """
        return base64.b64encode(string.encode('ascii'))

    def decode(self, string):
        """
        Decodes the given string using base64 decoding.

        Args:
                string (str): The string to be decoded.

        Returns:
                str: The decoded string.
        """
        return base64.b64decode(string.decode('ascii'))
