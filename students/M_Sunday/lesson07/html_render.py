#!/usr/bin/python


class Element:
    doctype = {'text': "<!DOCTYPE html>",
               'indent': 0}
    html_tag = {'text': "<html>",
                'indent': 0}

    def __init__(self, contents=None):
        if contents == None:
            self.HtmlStr = []
            self.HtmlStr.append(self.doctype['text'])
            self.HtmlStr.append(self.html_tag['text'])
        else:
            self.HtmlStr = contents

    #def write_to(self, file):
    #    FileStr = open(file, 'w+')
    #    for item in self.HtmlStr:
    #        FileStr.write("{}\n".format(item))
    #    FileStr.write(self.html_tag['text'].replace("<", "</"))
    #    FileStr.close()

    def append(self, text):
        self.HtmlStr.append(text)

    def render(self, file_out, cur_ind=""):
        for item in self.HtmlStr:
            file_out.write("{}\n".format(item))
        file_out.write(self.html_tag['text'].replace("<", "</"))
