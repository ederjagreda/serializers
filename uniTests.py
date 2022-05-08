import os
import unittest
import tempfile
from controlador import infoParser
from serializers.xmlSerializer import xmlSerializer
from serializers.jsonSerializer import jsonSerializer
from serializers.yamlSerializer import yamlSerializer


class tests(unittest.TestCase):
    def setUp(self):
        self.xml_file = r"test_files\xml_file.xml"
        self.json_file = r"test_files\json_file.json"
        self.yaml_file = r"test_files\yaml_file.yaml"
        self.folder = os.path.dirname(__file__)
        self.data = {
            "name": "Eder Agreda",
            "address": "San Benito st, 5",
            "phone_number": "123456789",
        }

    def test_invalidInpuFileRaisesException(self):
        with self.assertRaisesRegex(
            ValueError, "no valid input:not a file or not valid extension"
        ):
            value = infoParser(self.folder)

    def test_xmlFileSerializer(self):
        value = infoParser(self.xml_file)
        self.assertIsInstance(value.getDefaultSerializer(), xmlSerializer)

    def test_jsonFileSerializer(self):
        value = infoParser(self.json_file)
        self.assertIsInstance(value.getDefaultSerializer(), jsonSerializer)

    def test_yamlFileSerializer(self):
        value = infoParser(self.yaml_file)
        self.assertIsInstance(value.getDefaultSerializer(), yamlSerializer)

    def test_deserializeJsonFile(self):
        value = infoParser(self.json_file)
        serializer = value.getDefaultSerializer()
        data = value.getData(serializer)
        self.assertEqual(data, self.data)

    def test_deserializeYamlFile(self):
        value = infoParser(self.yaml_file)
        serializer = value.getDefaultSerializer()
        data = value.getData(serializer)
        self.assertEqual(data, self.data)

    def test_deserializeXmlFile(self):
        value = infoParser(self.xml_file)
        serializer = value.getDefaultSerializer()
        data = value.getData(serializer)
        self.assertEqual(data, self.data)

    def test_writeToXml(self):
        temp_name = "%s.xml" % next(tempfile._get_candidate_names())
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, temp_name)
            infoParser.writeData(xmlSerializer(), self.data, path)
            self.assertTrue(os.path.isfile(path))

    def test_writeToYaml(self):
        temp_name = "%s.yaml" % next(tempfile._get_candidate_names())
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, temp_name)
            infoParser.writeData(yamlSerializer(), self.data, path)
            self.assertTrue(os.path.isfile(path))

    def test_writeToJson(self):
        temp_name = "%s.json" % next(tempfile._get_candidate_names())
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, temp_name)
            infoParser.writeData(jsonSerializer(), self.data, path)
            self.assertTrue(os.path.isfile(path))

    def test_writeHtml(self):
        temp_name = "%s.html" % next(tempfile._get_candidate_names())
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, temp_name)
            infoParser.toHtml(self.data, path)
            self.assertTrue(os.path.isfile(path))
