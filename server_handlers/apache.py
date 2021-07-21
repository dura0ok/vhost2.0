import os
from collections import namedtuple
from typing import List

config_tuple = namedtuple("config", ["ServerName", "DocumentRoot"])


def pack_config(vhost_path):
    server_name, document_root = None, None
    with open(vhost_path) as f:
        for line in f.readlines():
            if line.strip().startswith("#"):
                continue
            if "ServerName" in line:
                server_name = line.replace("ServerName", "").strip()

            elif "DocumentRoot" in line:
                document_root = line.replace("DocumentRoot", "").strip()

    return config_tuple(server_name, document_root)


class ApacheService:

    @staticmethod
    def get_configs_files(hosts_path):
        if not os.path.isdir(hosts_path):
            raise NotADirectoryError("Directory with configs not found")
        return os.listdir(hosts_path)

    def get_parsed_configs(self, hosts_path) -> List[config_tuple]:
        configs = []
        for host_name in self.get_configs_files(hosts_path):
            if host_name == "default-ssl.conf":
                continue
            full_path = hosts_path + host_name

            configs.append(pack_config(full_path))

        return configs
