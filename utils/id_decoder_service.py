import base64
from urllib.parse import unquote


class IDDecoderService:

    @staticmethod
    def decode_id(encoded_id: str) -> str | None:
        """
        Decode the URL-encoded ID.
        \f
        :param encoded_id:  The URL-encoded ID.
        :return: The decoded ID, or None if decoding fails.
        """
        try:
            decoded_bytes = base64.urlsafe_b64decode(encoded_id)
            # print(f"Decoded bytes: {decoded_bytes}")
            decoded_id = decoded_bytes.decode('utf-8')
            decoded_id = unquote(decoded_id)
            # print(f"Decoded ID: {decoded_id}")
            return decoded_id
        except Exception as e:
            # print(f"Error decoding the ID: {e}")
            return None
