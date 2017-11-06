class TagException(Exception):
    pass


class Tag(object):
    __slots__ = ('_name', '_attrs', '_parent', '_previous_sibling', '_next_sibling')


    def __init__(self, name, attrs={}):
        self._name = str(name)
        self._attrs = None
        self._parent = None
        self._previous_sibling = None
        self._next_sibling = None
        self.__set_attrs(attrs)


    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self._attrs.get(attr)


    def __setattr__(self, attr, value):
        try:
            super().__setattr__(attr, value)
        except AttributeError:
            self._attrs[attr] = value


    def __delattr__(self, attr):
        try:
            super().__delattr__(attr)
        except AttributeError:
            del self._attrs[attr]


    def __str__(self):
        attributes = ' '.join(['{}="{}"'.format(key, value) for key, value in self._attrs.items()])
        return '<{} {}>'.format(self._name, attributes)


    def __set_attrs(self, attrs):
        if not isinstance(attrs, dict):
            raise ValueError
        self._attrs = attrs

    @staticmethod
    def __is_html_tag(obj):
        if not (isinstance(obj, ContainerTag) or isinstance(obj, Tag)):
            raise TagException('{} Not an html tag!'.format(obj))

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if not isinstance(parent, ContainerTag):
            raise TagException('{} Not a container tag!'.format(parent))
        self._parent = parent

    @parent.deleter
    def parent(self):
        self._parent = None

    @property
    def previous_sibling(self):
        return self._previous_sibling

    @previous_sibling.setter
    def previous_sibling(self, previous_sibling):
        self.__is_html_tag(previous_sibling)
        self._previous_sibling = previous_sibling

    @previous_sibling.deleter
    def previous_sibling(self):
        self._previous_sibling = None

    @property
    def next_sibling(self):
        return self._next_sibling

    @next_sibling.setter
    def next_sibling(self, next_sibling):
        self.__is_html_tag(next_sibling)
        self._next_sibling = next_sibling

    @next_sibling.deleter
    def next_sibling(self):
        self._next_sibling = None

    @property
    def first_child(self):
        raise TagException('Not a container tag!')

    @property
    def last_child(self):
        raise TagException('Not a container tag!')

    @property
    def children(self):
        raise TagException('Not a container tag!')


class ContainerTag(Tag):
    pass


if __name__ == '__main__':
    a = Tag('a')
    a.href = 'www.python.org'
    a.name = 'Python Official Site'
    parent_tag = ContainerTag('head')
    next_tag = Tag('p')
    prev_tag = Tag('i')
    a.parent = parent_tag
    a.next_sibling = next_tag
    a.previous_sibling = prev_tag
    print(a, a.parent, a.next_sibling, a.previous_sibling)
