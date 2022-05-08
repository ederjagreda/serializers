import xml.etree.ElementTree as et
from .serializersContainer import container
from .baseSerializer import Serializer


class xmlSerializer(Serializer):
    @property
    def format(self):
        return "xml"

    def read(self, file):
        tree = et.parse(file)
        root = tree.getroot()
        data = {}
        for item in root.iter():
            if item.text:
                data[item.tag] = item.text
        return data

    def export(self, data, output_file):
        root = et.Element("data")
        for k, v in data.items():
            et.SubElement(root, k).text = v
        tree = et.ElementTree(root)
        tree.write(output_file)


container.register_format("xml", xmlSerializer)
