import json
from .serializersContainer import container
from .baseSerializer import Serializer


class jsonSerializer(Serializer):
    @property
    def format(self):
        return "json"

    def read(self, file):
        with open(file) as f:
            return json.load(f)


    def export(self, data, output_file):
        with open(output_file, "w") as f:
            json.dump(data, f, indent=3)


container.register_format("json", jsonSerializer)
