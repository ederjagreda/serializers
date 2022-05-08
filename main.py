import argparse
from controlador import infoParser
import serializers.serializersContainer as ct


def getArgs():
    """
    function to parse args

    Returns:
        string[]: returns the input file, and the console y export values if provided
    """
    parser = argparse.ArgumentParser(description="Json/xml/yaml Serializer")
    parser.add_argument("input", help="file to process")
    parser.add_argument(
        "--show", help="show deserialized data", choices=["console", "explorer"]
    )
    supported_types = infoParser.getSupportedFormats(ct.container)
    parser.add_argument(
        "--export", help="export to specific format", choices=supported_types
    )
    args = parser.parse_args()
    return (args.input, args.show, args.export, supported_types)


def workWithAttrs(input, show, export, supported_types):
    """
    function that works with the args provided.
    will conect to controlador.py based on args.

    Args:
        input (str): input file in the sopported formats
        show (str): option to show the deserialized data in console or in a explorer
        export (str): format to which, you want to export the data
        supported_types (list): list of valid extensions

    Raises:
        ValueError: if the input is not a file or one not having a vida extension
    """
    parse_file = infoParser(input)
    d_deserializer = parse_file.getDefaultSerializer()
    d_data = parse_file.getData(d_deserializer)
    if d_data:
        if show:
            if show == "console":
                print(parse_file.getData(d_deserializer))
            elif show == "explorer":
                html_file = infoParser.toHtml(d_data)
                infoParser.showHtml(html_file)

        if export:
            serializer = parse_file.getSerializer(export)
            infoParser.writeData(serializer, d_data)


if __name__ == "__main__":
    input, show, export, supported_types = getArgs()
    workWithAttrs(input, show, export, supported_types)
