import base64
from urllib.parse import unquote, quote


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
            return decoded_id
        except Exception as e:
            print(f"Error decoding the ID: {e}")
            return None

    @staticmethod
    def encode_id(id_to_encode: str) -> str | None:
        """
        Encode the given ID to a URL-safe Base64 representation.
        :param id_to_encode: The ID to encode.
        :return: The encoded ID, or None if encoding fails.
        """
        try:
            # URL-encode the ID before Base64 encoding to handle special characters
            encoded_id = quote(id_to_encode)
            encoded_bytes = encoded_id.encode('utf-8')
            encoded_bytes = base64.urlsafe_b64encode(encoded_bytes)
            encoded_id = encoded_bytes.decode('utf-8')
            return encoded_id
        except Exception as e:
            print(f"Error encoding the ID: {e}")
            return None
