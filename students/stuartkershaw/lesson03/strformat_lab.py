#!/usr/bin/env python3

#Task One

seq_in = (2, 123.4567, 10000, 12345.67)

file_out = ''.join(['file_', format(seq_in[0], '03')])
float_dec_out = format(seq_in[1], '.2f')
sci_out = format(seq_in[2], '.2e')
sci_sig_out = format(seq_in[3], '.2e')

out_msg = '{}: {}, {}, {}'.format(file_out, float_dec_out, sci_out, sci_sig_out)

print(out_msg)

#Task Two

file_out_alt = f"file_{seq_in[0]:03}"
float_dec_out_alt = f"{seq_in[1]:.2f}"
sci_out_alt = f"{seq_in[2]:.2e}"
sci_sig_out_alt = f"{seq_in[3]:.2e}"

out_msg_alt = f"{file_out_alt}: {float_dec_out_alt}, {sci_out_alt}, {sci_sig_out_alt}"

print(out_msg_alt)

#Task Three

def formatter(tuple_in):
    t = tuple_in
    fstring = []
    for i in t:
        fstring.append('{:d}')
    out_msg = 'the {} numbers are: '.format(len(t))
    return out_msg + ', '.join(fstring).format(*t)

print(formatter((2,3,5,7,9)))

