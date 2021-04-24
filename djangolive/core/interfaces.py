import abc


class AbsStrategyBaseContext(object):
    def __init__(self, *args, **kwargs):
        # Override
        pass

    @property
    def data(self):
        # Override
        return None


class AbsBaseStrategy(metaclass=abc.ABCMeta):

    context_class = AbsStrategyBaseContext

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

        self.context = self._get_context(args, kwargs)

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def response(self):
        return dict()

    def _get_context(self, args, kwargs):
        return self.context_class(args, kwargs)


class DefaultStrategy(AbsBaseStrategy):
    name = "default_strategy"

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = kwargs.get("user", None)

    def execute(self, *args, **kwargs):
        pass


class AbsBaseCommand(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def strategy(self):
        pass


class DefaultCommand(AbsBaseCommand):
    name = "default_cmd"
    strategy = DefaultStrategy
