from abc import ABC, abstractmethod

from server_handlers.apache import ApacheService
from server_handlers.nginx import NginxService


class BaseHandler(ABC):

    def __init__(self):
        self.server = None

    def set_server(self, server_name):
        if server_name == "apache":
            self.server = ApacheService()
        elif server_name == "nginx":
            self.server = NginxService()
        else:
            raise Exception("server")

    @abstractmethod
    def show_hosts(self):
        pass
