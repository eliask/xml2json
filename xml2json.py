#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert XML to JSON."""

from argparse import ArgumentParser, FileType
from json import dump
from sys import stdin, stdout

parser = ArgumentParser(description='Convert an XML file to JSON.')
parser.add_argument('--unsafe', action='store_true',
                    help='do not use defusedxml: only for known-safe XML!')
parser.add_argument('infile', nargs='?', type=FileType('rt'),
                    default=stdin)


def xml_element_to_dict(elem):
    """Convert XML Element to a simple dict."""
    inner = dict(elem.attrib)
    children = list(map(xml_element_to_dict, list(elem)))
    text = elem.text and elem.text.strip()
    if text:
        inner['@text'] = text
    if children:
        inner['@children'] = children

    return {elem.tag: inner}


def main(arg):
    """Dump JSON-from-parsed-XML to stdout."""
    if arg.unsafe:
        from xml.etree.cElementTree import parse
    else:
        from defusedxml.cElementTree import parse

    xml_parser = parse(arg.infile)
    root = xml_parser.getroot()

    dump(xml_element_to_dict(root), stdout, indent=2)
    print()


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
