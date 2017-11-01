from abc import ABCMeta, abstractmethod
import os
import json


class ParamHandlerException(ValueError):
    pass


class ParamHandler(metaclass=ABCMeta):
    __types = {}

    def __init__(self, source):
        self.source = None
        self.__source_exists(source)
        self.params = {}


    def __source_exists(self, source):
        if not os.path.exists(source):
            raise ParamHandlerException('No source file found')

        self.source = source


    @abstractmethod
    def read(self): # чтение из файла
        pass


    @abstractmethod
    def write(self): # запись в файл
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))

        cls.types[name] = klass


    @classmethod
    def get_instance(source, *args, **kwargs):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = ParamHandler.__types.get(ext)

        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))

        return klass(source, *args, **kwargs)


class JsonParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.conf = json.loads(f.read())


    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.conf, f, indent=4)
