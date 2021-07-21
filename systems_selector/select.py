import distro
from systems_selector.confs import systems, SelectSystemError
from systems_handlers.base import BaseHandler


def select_handler() -> BaseHandler:
    for handler_name in systems.keys():
        if distro.id() in systems[handler_name]["distros"]:
            return systems[handler_name]["handler"]

    raise SelectSystemError("Your distributive not support :(")


