class Element (object):
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None):
        self.content = []
        if content is not None:
            self.content.append(content)

    def append(self, new_cont):
        """add another string to the content"""
        self.content.append(new_cont)

    def render(self, file_out, cur_ind=""):
        """renders tag and strings in the content"""
        file_out.write("{}<{tag}>\n".format(cur_ind, tag=self.tag_name))
        for i in self.content:
            file_out.write("{}{}\n".format(cur_ind, i))
        file_out.write("{}</{tag}>".format(cur_ind, tag=self.tag_name))
