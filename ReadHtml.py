#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re

from bs4 import BeautifulSoup


class Clip:
    def __init__(self):
        pass

    title = "unknown"


class ParseHtml:
    def __init__(self):
        pass

    print_text = ""

    def parse(self, file_name):
        soup = BeautifulSoup(open(file_name))
        body_container = soup.body.div
        for child in body_container.children:
            if child == '\n':
                continue
            if len(child.attrs) == 0:
                continue
            if child['class'][0] == "sectionHeading":
                self.print_text += "\r\n\r\n\r\n"
                self.print_text += child.string.replace(' ', '')
                self.print_text += "\r\n"
            if child['class'][0] == "noteHeading":
                head = re.findall(r'Location\s+\d+', child.text)
                self.print_text += head[0]
            if child['class'][0] == "noteText":
                self.print_text += child.string.replace(' ', '')
                self.print_text += "\r\n"

    def out_text(self, out_file_name):
        fp = open(out_file_name, 'w')
        fp.write(self.print_text)


parseHtml = ParseHtml()
parseHtml.parse("/Users/dongyan/Downloads/自卑与超越：你要清楚自己应该怎样过好这一生 (Chinese Edition) - Notebook.html")
parseHtml.out_text("/Users/dongyan/Downloads/自卑与超越：你要清楚自己应该怎样过好这一生-format.txt")
print('success')
