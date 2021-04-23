from .interfaces import AbsBaseStrategy, DefaultStrategy
from typing import List


def generate_strategy_map(strategies: List[AbsBaseStrategy]):
    return dict([cls.name, cls] for cls in strategies)


def perform_strategy(strategy, view, request, strategy_map):
    data = request.data
    if isinstance(data, list):
        params = {"data": data}
    elif isinstance(data, dict):
        params = data
    else:
        params = {}

    strategy_cls = strategy_map.setdefault(strategy, DefaultStrategy)
    strategy = strategy_cls(view, request, **params)
    strategy.execute()
    return strategy
