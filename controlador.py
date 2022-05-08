import os
import webbrowser
import serializers.serializersContainer as ct
from serializers.xmlSerializer import xmlSerializer
from serializers.jsonSerializer import jsonSerializer
from serializers.yamlSerializer import yamlSerializer

file_folder = os.path.dirname(__file__)
output_folder = os.path.join(file_folder, "outputs")
REQUIRED_FIELDS = ["name", "address", "phone_number"]


class infoParser:
    """Class used to load and initialize serializers"""

    def __init__(self, basefile):
        """
        Args:
            basefile (str): file filepath to deserialize
        """
        self.basefile = basefile
        self.container = ct.container
        self.validInputFile()
        self.createOuputFolder()

    def createOuputFolder(self):
        """
        create folder for writing out files
        """
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def validInputFile(self):
        """
        validate if inputfile is a valid one
        """
        supported_types = infoParser.getSupportedFormats(self.container)
        if (
            not os.path.isfile(self.basefile)
            or not os.path.splitext(self.basefile)[-1][1:] in supported_types
        ):
            raise ValueError("no valid input:not a file or not valid extension")

    @property
    def fileFormat(self):
        """
        return the file extension

        Returns:
            str: file extension
        """
        extension = os.path.splitext(self.basefile)[-1]
        return extension[1:]

    @staticmethod
    def getSupportedFormats(container):
        """
        return a list with the serializers registered

        Args:
            container (SerializerContainer): container that register serializers

        Returns:
            str: valid formats
        """
        #
        return [k for k in container.serializers.keys()]

    def getDefaultSerializer(self):
        """
        gets the default serializer based on the input extension

        Returns:
            Serializer: default serializer
        """
        format = self.fileFormat
        return self.getSerializer(format)

    def getSerializer(self, format):
        """
        gets the default serializer based format provided
        Args:
            format (str): format to get serializer

        Returns:
            Serializer: chosen serializer
        """
        return self.container.get_serializer(format)

    def getData(self, serializer):
        """
        parses the input file using the correct serializer

        Args:
            serializer (Serializer): default serializer based on extension

        Raises:
            ValueError: if not all fiels are present

        Returns:
            dict: dictionary with name, address and phone_number info
        """
        data = serializer.read(self.basefile)
        if all(elem in data for elem in REQUIRED_FIELDS):
            return data
        raise ValueError("not enough fields provided")

    @staticmethod
    def writeData(serializer, data, output=None):
        """
        writes to an external file path
        the file name is based on the extension

        Args:
            serializer (Serializer): serializer object to use
            data (dict): dictionary with name, address and phone_number info
        """
        if not output:
            output_file = "output_{0}.{0}".format(serializer.format)
            output = os.path.join(output_folder, output_file)
        try:
            serializer.export(data, output)
            print("file saved to: %s" % output)
        except PermissionError:
            print("cant write to destination because of permissions")

    @staticmethod
    def toHtml(data, output=None):
        """
        parses the data provided and writes to a html file.

        Args:
            data (dict): dictionary with name, address and phone_number info
        """
        if not output:
            output_file = "output_html.html"
            output = os.path.join(output_folder, output_file)

        with open(output, "w") as f:
            message = """
            <html>
            <head><h1><center>Deserialized data</center></h1><head>
            <body>
            """

            for k, v in data.items():
                message += """<p><b>%s</b>: %s</p>
                                """ % (
                    k,
                    v,
                )
            message += "</body>"
            f.write(message)
        return output

    @staticmethod
    def showHtml(output):
        """
        launches in explorer the selected html file
        """
        webbrowser.open(output, new=2)
