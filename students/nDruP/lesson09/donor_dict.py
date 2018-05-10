import os
from donor import Donor

class Donor_Dict():

    name_len = len("Name")
    num_len = len("# of Gifts")
    avg_len = len("Average")
    sum_len = len("Total")
    
    def __init__(self, donor, *args):
        self._dict = {donor.name.lower(): donor}
        for x in args:
            self._dict[x.name.lower()] = x

    def __contains__(self, d_name):
        return d_name.lower() in self._dict.keys()

    def __getitem__(self, key_name):
        return self._dict[key_name]
    
    def __len__(self):
        return len(self.names)
    
    @property
    def names(self):
        d_names = []
        for x in self._dict:
            d_names.append(self._dict[x].name)
        return d_names

    @property
    def avgs(self):
        averages = []
        for x in self._dict:
            averages.append(self._dict[x].avg_gift)
        return averages

    @property
    def sums(self):
        sums = []
        for x in self._dict:
            sums.append(self._dict[x].sum_gift)
        return sums

    @property
    def col_len(self):
        name_col = len("Donor Name")
        hist_col = len("Gifts")
        avg_col = len("Avg Gift")
        sum_col = len("Total Given")
        for x in self:
            name_col = max(name_col, len(x.name))
            hist_col = max(hist_col, len(len(x.history)))
            avg_col = max(avg_col, len(x.avg_gift))
            sum_col = max(sum_col, len(x.sum_gift))
        return [name_col, hist_col, avg_col, sum_col]
    
    def add_donor(self, d_name, contribution):
        key_name = d_name.lower()
        if key_name in self:
            self._dict[key_name].add_gift(contribution)
        else:
            self._dict[key_name] = Donor(d_name, contribution)

    def names_str(self, separator='\n'):
        return (("{}"+separator)*len(self)).format(*self.names)
            
    def donor_info(self, name):
        info = self[name]
        return (info.name, info.history, info.avg_gift, info.sum_gift)

    def all_donor_info(self):
        all_info = []
        for x in self._dict:
            all_info.append(self.donor_info(x))
        return all_info

    def sort_by_name(self, d_info):
        return d_info[0]

    def sort_by_hist(self, d_info):
        return len(d_info[1])
    
    def sort_by_avg(self, d_info):
        return d_info[2]

    def sort_by_sum(self, d_info):
        return d_info[3]

    def sort_all_donor_info(self, by=0):
        key_dict = {0: self.sort_by_name,
                    1: self.sort_by_hist,
                    2: self.sort_by_avg,
                    3: self.sort_by_sum}
        return sorted(self.all_donor_info(), key=key_dict[by], reverse=(by>0))
        
    def thank_u_str(self, d_name, most_recent = 0):
        thank = self[d_name.lower()]
        if most_recent:
            thank_gift = thank.history[len(thank.history)-1]
        else:
            thank_gift = thank.sum_gift
        return (divider + f"Dearest {thank.name},\n"
                f"\tThank you for your donation(s) of ${thank_gift:.2f}!\n"
                "We will use your donation(s) to create real living Pokemon.\n"
                "You now have our eternal loyalty. Use it wisely.\n"
                "Sincerely,\n"
                f"We're a Pyramid Scheme & so is {thank.name}"
                + divider)
