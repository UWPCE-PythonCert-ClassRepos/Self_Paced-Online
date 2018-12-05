class Element:
    html_open = "<html>"
    html_close = "</html>"
    indent = "   "

    def __init__(self, content=None):
        """
        initialize the Element instance
        :param content: optional input, string to create single line of content
        """
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        """
        append another line to content
        :param content: string to append
        :return: none
        """
        if content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """
        render Element instance
        :param file_out: object to write rendering to
        :param cur_ind: indentation level to apply to each line
        :return: none
        """
        file_out.write(cur_ind+Element.html_open+'\n')
        for line in self.content:
            file_out.write(cur_ind+Element.indent+line+'\n')
        file_out.write(cur_ind+Element.html_close+'\n')

