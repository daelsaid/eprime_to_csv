import os
import sys
import numpy as np
import pandas as pd
from collections import OrderedDict

# text_file=''


def remove_unicode(string):
        return ''.join([val for val in string if 31 < ord(val) < 127])


def eprimetxt_todf(text_file, out_file):

    with open(text_file, 'rb') as fo:
        text_data = list(fo)

    filtered_data = [remove_unicode(row.decode('utf-8', 'ignore')) for row in text_data]

    start_index = [i for i, row in enumerate(filtered_data) if row == '*** LogFrame Start ***']
    end_index = [i for i, row in enumerate(filtered_data) if row == '*** LogFrame End ***']
    if len(start_index) != len(end_index) or start_index[0] >= end_index[0]:
        print('Warning: LogFrame Starts and Ends do not match up.')

    n_rows = min(len(start_index), len(end_index))

    headers = []
    data_by_rows = []

    for i in range(n_rows):
        one_row = filtered_data[start_index[i]+1:end_index[i]]
        data_by_rows.append(one_row)
        for col_val in one_row:
            split_header_idx = col_val.index(':')
            headers.append(col_val[:split_header_idx])
    headers = list(OrderedDict.fromkeys(headers))
    data_matrix = np.empty((n_rows, len(headers)), dtype=object)
    data_matrix[:] = np.nan

    for i in range(n_rows):
        for cell_data in data_by_rows[i]:
            split_header_idx = cell_data.index(':')
            for k_header, header in enumerate(headers):
                if cell_data[:split_header_idx] == header:
                    data_matrix[i, k_header] = cell_data[split_header_idx+1:].lstrip()

    df = pd.DataFrame(columns=headers, data=data_matrix)
    df.to_csv(out_file, index=False)
    print 'output made'
    return df



#sub functions compiled and edited from https://github.com/tsalo/convert-eprime
