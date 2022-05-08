class SerializerContainer:
    """Class used to load and initialize serializers"""
    def __init__(self):
        self.serializers = {}

    def register_format(self, format, serializer):
        """
        register a serializer format
        """
        self.serializers[format] = serializer

    def get_serializer(self, format):
        """
        get serializer based on file format provided
        """
        serialiser = self.serializers.get(format)
        if not serialiser:
            raise ValueError("lalal", format)
        return serialiser()


container = SerializerContainer()
