from .interfaces import AbsBaseStrategy, DefaultStrategy
from typing import List


def generate_command_map(commands: List):
    return dict([cls.name, cls] for cls in commands)


def perform_strategy(command: str, view, request, command_map):
    data = request.data
    if isinstance(data, list):
        params = {"data": data}
    elif isinstance(data, dict):
        params = data
    else:
        params = {}

    command_cls = command_map.setdefault(command, DefaultStrategy)
    command = command_cls(view, request, **params)
    command.execute()
    return command
