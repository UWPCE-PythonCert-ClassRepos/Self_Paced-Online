class Element():
    def indent(self, tab_cnt):
        tab = "\t"
        results = ""
        cnt = 0
        while cnt < tab_cnt:
            if tab_cnt == 0:
                break
            else:
                results += f"{tab}"
                cnt = cnt + 1
        return results

    def __init__(self, content_list=""):
        self.content_list = [content_list]

    def append_to_list(self, appended_txt):
        self.content_list.append(appended_txt)

    def render(self, file_out, cur_ind=""):
        file_out.write(
            f"{cur_ind}".join(self.content_list))

    def html(self, tag_type, cur_ind=""):
        if tag_type == "open":
            self.append_to_list(f"{cur_ind}<html>\n")
        elif tag_type == "close":
            self.append_to_list(f"{cur_ind}</html>\n")

    def head(self, tag_type, cur_ind="", att_list=[]):
        if tag_type == "open":
            self.append_to_list(f"{cur_ind}<head>\n")
        elif tag_type == "close":
            self.append_to_list(f"{cur_ind}</head>\n")

    def title(self, title_txt="", cur_ind=""):
        self.append_to_list(f"{cur_ind}<title>{title_txt}</title>\n")

    def body(self, tag_type, cur_ind="", att_list=[]):
        if tag_type == "open":
            self.append_to_list(f"{cur_ind}<body>\n")
        elif tag_type == "close":
            self.append_to_list(f"{cur_ind}</body>\n")

    def br(self, cur_ind=""):
        self.append_to_list(f"{cur_ind}</br>\n")

    def p(self, tag_type, cur_ind="", att_list=[]):
        if tag_type == "open":
            self.append_to_list(f"{cur_ind}<p>")
        elif tag_type == "close":
            self.append_to_list(f"{cur_ind}</p>\n")
