# encoding: utf-8


import inspect
import re

from . import utils


class Parser(object):
    def __init__(self):
        pass

    def parse_from_docstring(self, docstring, **kwargs):
        pass

    def parse_from_function(self, function, **kwargs):
        pass

    def parse_from_class(self, class_, **kwargs):
        pass


class SophonParser(Parser):
    def __init__(self):
        super(SophonParser, self).__init__()

    def parse_from_docstring(self, docstring, **kwargs):
        docstring = re.sub(r'\n# (.*)\n',
                           r'\n**\1**\n\n',
                           docstring)
        docstring = re.sub(r'\n    (\S*):(.*)',
                           r'\n- **\1**:\2',
                           docstring)
        docstring = docstring.replace('\n    ', '\n')
        return docstring

    def parse_from_function(self, function, **kwargs):
        signature = utils.extract_class_signature(function)
        docstring = inspect.getdoc(function)
        if docstring:
            docstring = self.parse_from_docstring(docstring)
        else:
            docstring = ''

        md = []
        if kwargs.get('repo_url'):
            link = utils.generate_repo_link(function, kwargs.get('repo_url'), kwargs.get('branch'))
            md.append('<span style="float:right;">{}</span>'.format(link))

        md.append('## {}'.format(function.__name__))
        md.append(utils.code_snippet(signature))
        md.append(docstring)
        md.append('---\n\n')

        md = '\n\n'.join(md)
        return md

    def parse_from_class(self, class_, **kwargs):
        signature = utils.extract_class_signature(class_)
        docstring = inspect.getdoc(class_)
        if docstring:
            docstring = self.parse_from_docstring(docstring)
        else:
            docstring = ''

        md = []
        if kwargs.get('repo_url'):
            link = utils.generate_repo_link(class_, kwargs.get('repo_url'), kwargs.get('branch'))
            md.append('<span style="float:right;">{}</span>'.format(link))

        md.append('## {}'.format(class_.__name__))
        md.append(utils.code_snippet(signature))
        md.append(docstring)
        md.append('---\n\n')

        md = '\n\n'.join(md)
        return md


class ReStructuredTextParser(Parser):
    def __init__(self):
        super(ReStructuredTextParser, self).__init__()

    def parse_from_docstring(self, docstring, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_function(self, function, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_class(self, class_, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')


class GoogleDocParser(Parser):
    def __init__(self):
        super(GoogleDocParser, self).__init__()

    def parse_from_docstring(self, docstring, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_function(self, function, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_class(self, class_, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')


class NumPyDocParser(Parser):
    def __init__(self):
        super(NumPyDocParser, self).__init__()

    def parse_from_docstring(self, docstring, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_function(self, function, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')

    def parse_from_class(self, class_, **kwargs):
        raise NotImplementedError(self.__class__.__name__ + '.' + inspect.stack()[0][3]
                                  + 'is not implemented!')


_dict = {
    'sophon': SophonParser,

    'reStructuredText': ReStructuredTextParser,
    'rst': ReStructuredTextParser,
    'reST': ReStructuredTextParser,

    'Google': GoogleDocParser,
    'google': GoogleDocParser,

    'NumPy': NumPyDocParser,
    'numpy': NumPyDocParser,
}


def get(name):
    class_ = _dict.get(name)
    if class_:
        return class_()
    else:
        return None

