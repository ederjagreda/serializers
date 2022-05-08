import abc


class Serializer(abc.ABC):
    """
    Class that defines required Methods for serializer
    """    

    @property
    def format(self):
        """
        file format that this serializer represents
        """
        pass

    @abc.abstractmethod
    def read(self):
        """
        function to deserialized input data
        """
        pass

    @abc.abstractmethod
    def export(self):
        """
        function to serialize to an external file
        """
        pass