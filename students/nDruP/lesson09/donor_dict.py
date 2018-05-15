from donor import Donor

class Donor_Dict():
    def __init__(self, donor, *args):
        self._dict = {donor.name.lower(): donor}
        for x in args:
            self._dict[x.name.lower()] = x

    def __contains__(self, donor):
        return (donor.lower() in self._dict.keys()) or (donor in self.donors)

    def __getitem__(self, key_name):
        return self._dict[key_name]
    
    def __len__(self):
        return len(self.donors)

    @classmethod
    def from_file(cls, file_path):
        #donor_name;history (history is comma-separated)
        first_donor = None
        donor_list = []
        
        with open(file_path, 'r') as text:
            end = text.tell()
            while True:
                some_str = text.readline()
                if text.tell() == end:
                    break
                donor_init = ["", ""]
                name_or_hist = 0
                gift = ""
                history = []
                
                for param in some_str:
                    if param == ';':
                        name_or_hist = 1
                        continue
                    donor_init[name_or_hist]+=param

                for hist in donor_init[1]:
                    if hist == ',':
                        history.append(float(gift))
                        gift = ""
                        continue
                    gift += hist
                history.append(float(gift))

                if first_donor == None:
                    first_donor = Donor(donor_init[0], history)
                else:
                    donor_list.append(Donor(donor_init[0], history))
                end = text.tell()
        return cls(first_donor, *donor_list)
    
    @property
    def names(self):
        d_names = []
        for x in self.donors:
            d_names.append(x.name)
        return d_names

    @property
    def avgs(self):
        averages = []
        for x in self.donors:
            averages.append(x.avg_gift)
        return averages

    @property
    def sums(self):
        sum_list = []
        for x in self.donors:
            sum_list.append(x.sum_gift)
        return sum_list

    @property
    def keys(self):
        return list(self._dict.keys())

    @property
    def donors(self):
        return [d for _, d in self._dict.items()]

    @property
    def col_len(self):
        name_col = len("Donor Name")
        hist_col = len("Gifts")
        avg_col = len("Avg Gift")
        sum_col = len("Total Given")
        for x in self.donors:
            name_col = max(name_col, len(x.name))
            hist_col = max(hist_col, len(str(len(x.history))))
            avg_col = max(avg_col, len(str(x.avg_gift)))
            sum_col = max(sum_col, len(str(x.sum_gift)))
        return [name_col, hist_col, avg_col, sum_col]

    def dict_to_txt(self):
        dict_txt = ""
        for d in self.donors:
            dict_txt += d.name + ';'
            dict_txt += ("{}" + (",{}"*(len(d.history)-1))).format(*d.history)
            dict_txt += '\n'
        return dict_txt
    
    def add_donor(self, d_name, contribution):
        key_name = d_name.lower()
        if key_name in self:
            self._dict[key_name].add_gift(contribution)
        else:
            self._dict[key_name] = Donor(d_name, contribution)

    def names_str(self, separator='\n'):
        return ((separator+"{}")*len(self)).format(*self.names)

    def all_donor_info(self):
        all_info = []
        for donor in self.donors:
            all_info.append(donor.info)
        return all_info

    def sort_by_name(self, d_info):
        return d_info[0].lower()

    def sort_by_hist(self, d_info):
        return d_info[1]
    
    def sort_by_avg(self, d_info):
        return d_info[2]

    def sort_by_sum(self, d_info):
        return d_info[3]

    def sort_all_donor_info(self, by=0):
        sort_dict = {0: self.sort_by_name,
                    1: self.sort_by_hist,
                    2: self.sort_by_avg,
                    3: self.sort_by_sum}
        return sorted(self.all_donor_info(), key=sort_dict[by], reverse=(by>0))

    def donor_report_row(self, header=0):
        donor_col = "{:<" + f"{self.col_len[0]}" + "}"
        hist_col = "{:>" + f"{self.col_len[1]}" + "}"
        avg_col = "{:>" + f"{self.col_len[2]}" + (".2f") * (not header) + "}"
        sum_col = "{:>" + f"{self.col_len[3]}" + (".2f") * (not header) + "}"
        return (donor_col+"\t"+hist_col+"\t"+avg_col+"\t"+sum_col)
    
    def donor_report(self, sort_by):
        if sort_by == 5:
            donor_list = self.all_donor_info()
        else:
            donor_list = self.sort_all_donor_info(sort_by-1)
        col_name_list = ["Donor Name", "Gifts", "Avg Gift", "Total Given"]
        report = self.donor_report_row(1).format(*col_name_list)
        row = self.donor_report_row()
        for name, hist, avg_gift, sum_gift in donor_list:
            row_data = [name, hist, avg_gift, sum_gift]
            report += "\n" + row.format(*row_data)
        return report
