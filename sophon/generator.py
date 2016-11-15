# encoding: utf-8

from . import extractor
from inspect import ismethod


def generate_function_markdown(function):
    signature = extractor.extract_function_signature(function, ismethod(function))
    docstring = extractor.extract_function_docstring(function)
    md = []
    md.append('# ' + function.__name__ + '\n')
    md.append(extractor.code_snippet(signature))
    md.append(docstring)
    md.append('---')
    md = '\n'.join(md)
    return md

