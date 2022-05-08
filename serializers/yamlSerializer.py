import yaml
from .serializersContainer import container
from .baseSerializer import Serializer


class yamlSerializer(Serializer):
    def read(self, file):
        with open(file, "r") as f:
            return yaml.load(f, Loader=yaml.loader.SafeLoader)

    def export(self, data, output_file):
        with open(output_file, "w") as f:
            yaml.dump(data, f, allow_unicode=False, explicit_start=True)

    @property
    def format(self):
        return "yaml"


container.register_format("yaml", yamlSerializer)
