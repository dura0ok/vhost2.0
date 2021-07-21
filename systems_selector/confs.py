from systems_handlers.deb import DebHandler
from systems_handlers.rpm import RpmHandler

systems = {
    "deb_based": {"distros": ["linuxmint", "ubuntu"], "handler": DebHandler()},
    "rpm": {"distros": ["centos", "fedora"], "handler": RpmHandler()},
}


class SelectSystemError(Exception):
    pass
