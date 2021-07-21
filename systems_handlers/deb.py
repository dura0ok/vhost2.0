from systems_handlers.base import BaseHandler


class DebHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.hosts_path = "/etc/apache2/sites-available/"

    def show_hosts(self):
        hosts = self.server.get_parsed_configs(self.hosts_path)
        for host in hosts:
            print(host.ServerName, host.DocumentRoot)
