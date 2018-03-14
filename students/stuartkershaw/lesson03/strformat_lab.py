#!/usr/bin/env python3

#Task One

seq_in = (2, 123.4567, 10000, 12345.67)

file_out = ''.join(['file_', format(seq_in[0], '03')])
float_dec_out = format(seq_in[1], '.2f')
sci_out = format(seq_in[2], '.2e')
sci_sig_out = format(seq_in[3], '.2e')

out_msg = '{}: {}, {}, {}'.format(file_out, float_dec_out, sci_out, sci_sig_out)

print(out_msg)

