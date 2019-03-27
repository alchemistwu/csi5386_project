import csv
from tqdm import tqdm

def read_data_raw():
    catid_list = []
    subcatid_list = []
    value_list = []
    original_list = []
    cat_dict = {}
    sub_cat_dict_2 = {}
    sub_cat_dict_3 = {}
    f = open('ads_en_us.csv', 'r')
    reader = csv.reader(f)
    i = 0
    for line in reader:
        if i == 0:
            print line
            i += 1
        else:
            if line[-1] not in value_list:
                if line[1] not in cat_dict.keys():
                    cat_dict[line[1]] = 1
                else:
                    cat_dict[line[1]] += 1
                if line[1] == '2':
                    if line[3] not in sub_cat_dict_2.keys():
                        sub_cat_dict_2[line[3]] = 1
                    else:
                        sub_cat_dict_2[line[3]] += 1
                elif line[1] == '3':
                    if line[3] not in sub_cat_dict_3.keys():
                        sub_cat_dict_3[line[3]] = 1
                    else:
                        sub_cat_dict_3[line[3]] += 1
                catid_list.append(line[1])
                subcatid_list.append(line[3])
                value_list.append(line[-1])
            original_list.append(line[-1])

    print len(value_list)
    print cat_dict
    print sub_cat_dict_2
    print sub_cat_dict_3
    return catid_list, subcatid_list, value_list

def write_data():

    data = []
    label = []

    f = open('ads_en_us.csv', 'r')
    reader = csv.reader(f)
    wf = open('picked_data.csv', 'w')
    writer = csv.writer(wf)

    i = 0
    for line in reader:
        if i == 0:
            print line
            i += 1
        else:
            if line[1] == '2':
                if line[3] == '16':
                    data.append(line[-1])
                    label.append('c1_main')
                elif line[3] == '28':
                    data.append(line[-1])
                    label.append('c1_minor')
            elif line[1] == '3':
                if line[3] == '2':
                    data.append(line[-1])
                    label.append('c2_main')
                elif line[3] == '51':
                    data.append(line[-1])
                    label.append('c2_minor')
    f.close()

    for i in tqdm(range(len(data))):
        data_item = data[i].split('<')[0]
        stop_punctuation = ['\r', '\n', '\t']
        for item in stop_punctuation:
            while item in data_item:
                data_item = data_item.replace(item, '')
        row = [data_item, label[i]]
        writer.writerow(row)
    wf.close()

def read_data_from_processed_data():
    f = open('picked_data.csv', 'r')
    reader = csv.reader(f)
    for line in reader:
        print len(line)
        print line[1]
        print line[0]




if __name__ == '__main__':
    # write_data()
    read_data_from_processed_data()