import numpy as np
import os
from math import *
import argparse

def dssp_generate(path,name):
    name+='.dssp'
    f=open(os.path.join(path,name),'r')

    rows = f.readlines()
    row = rows[1][:-1]
    str_sec_str = rows[2][:-1]
    l=len(row)

    seq=[]
    sec_str=[]
    for j in range(l):
        if row[j] == 'A':
            x = 0
        if row[j] == 'R':
            x = 1
        if row[j] == 'N':
            x = 2
        if row[j] == 'D':
            x = 3
        if row[j] == 'C':
            x = 4
        if row[j] == 'Q':
            x = 5
        if row[j] == 'E':
            x = 6
        if row[j] == 'G':
            x = 7
        if row[j] == 'H':
            x = 8
        if row[j] == 'I':
            x = 9
        if row[j] == 'L':
            x = 10
        if row[j] == 'K':
            x = 11
        if row[j] == 'M':
            x = 12
        if row[j] == 'F':
            x = 13
        if row[j] == 'P':
            x = 14
        if row[j] == 'S':
            x = 15
        if row[j] == 'T':
            x = 16
        if row[j] == 'W':
            x = 17
        if row[j] == 'Y':
            x = 18
        if row[j] == 'V':
            x = 19
        seq.append(x)

    y = []
    for j in range(l):
        if str_sec_str[j] == 'C':
            x = 1
        else:
            x = 0
        y.append(x)
    n0 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'G':
            x = 1
        else:
            x = 0
        y.append(x)
    n1 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'H':
            x = 1
        else:
            x = 0
        y.append(x)
    n2 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'I':
            x = 1
        else:
            x = 0
        y.append(x)
    n3 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'T':
            x = 1
        else:
            x = 0
        y.append(x)
    n4 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'E':
            x = 1
        else:
            x = 0
        y.append(x)
    n5 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'B':
            x = 1
        else:
            x = 0
        y.append(x)
    n6 = np.array(y)
    y = []
    for j in range(l):
        if str_sec_str[j] == 'S':
            x = 1
        else:
            x = 0
        y.append(x)
    n7 = np.array(y)

    sec_str = np.stack((n0, n1, n2, n3, n4, n5, n6, n7))

    f.close()
    return seq, sec_str

def om_generate(path,name):
    name += '.om'
    f = open(os.path.join(path, name), 'r')
    rows = f.readlines()[2:]

    m0 = []
    m1=[]
    m2=[]
    m3=[]
    m4=[]
    m5 = []

    for row in rows:
        arr = row.split(' ')
        m0.append(sin(float(arr[2])/180*pi))
        m1.append(cos(float(arr[2])/180*pi))
        m2.append(sin(float(arr[3])/180*pi))
        m3.append(cos(float(arr[3])/180*pi))
        m4.append(sin(float(arr[4])/180*pi))
        m5.append(cos(float(arr[4])/180*pi))
    om = np.stack((m0, m1, m2, m3, m4, m5))
    f.close()
    return om


def theta_generate(path, name):
    name += '.t'
    f = open(os.path.join(path, name), 'r')
    rows = f.readlines()[1:]

    m0 = []
    m1 = []
    m2 = []
    m3 = []

    for row in rows:
        arr = row.split(' ')
        m0.append(sin(float(arr[2])/180*pi))
        m1.append(cos(float(arr[2])/180*pi))
        m2.append(sin(float(arr[3])/180*pi))
        m3.append(cos(float(arr[3])/180*pi))
    om = np.stack((m0, m1, m2, m3))
    f.close()
    return om


def energy_generate(path, name):
    name += '.en'
    f = open(os.path.join(path, name), 'r')
    rows = f.readlines()[1:]

    en=[]
    for row in rows:
        arr = row.split(' ')
        s=[]
        for a in arr[2:]:
            s.append(float(a))
        en.append(s)
    en = np.array(en).T
    f.close()
    return en


def fragment_generate(path, name):
    name += '.frag'
    f = open(os.path.join(path, name), 'r')
    rows = f.readlines()

    fr=[]
    for row in rows:
        arr = row.split(' ')
        s=[]
        for a in arr[:-1]:
            s.append(float(a))
        fr.append(s)
    fr = np.array(fr).T
    f.close()
    return fr

def dssp(path,name):
    name+='.d'
    f=open(os.path.join(path,name),'r')

    rows = f.readlines()
    row = rows[1][:-1]
    str_sec_str = rows[2][:-1]
    l=len(row)

    # y0 = 0
    # y1 = 0
    # y2 = 0
    # for j in range(l):
    #     if str_sec_str[j] == 'G':
    #         y0 += 1
    #     elif str_sec_str[j] == 'H':
    #         y0 += 1
    #
    #     elif str_sec_str[j] == 'I':
    #         y1 += 1
    #
    #     elif str_sec_str[j] == 'E':
    #         y1 += 1
    #
    #     elif str_sec_str[j] == 'B':
    #         y1 += 1
    #     else:
    #         y2 += 1
    # y=y0+y1+y2

    y0=0
    y=0
    for j in range(l):
        if row[j] == 'G' or row[j] == 'P':
            y0 += 1
        y+=1

    return y0/y

def f2dgenerate(path,name):
    file = open(os.path.join(path, name), 'r')
    # file = gzip.open(os.path.join('chains', '1a0tP.gz'), 'r')
    num = -9999
    trans = []
    x = 0.0
    y = 0.0
    z = 0.0
    flag = 0
    for row in file:
        if row[:3] == 'TER':
            break
        elif row[:4]=='ATOM':
            now = int(row[22:26])
            # print(str(row[11:17]))
            # print(float(row[26:38]))
            # print(float(row[38:46]))
            # print(float(row[46:54]))
            if (num != -9999 and num != now):
                trans.append([x, y, z])
                flag = 0
            num = now
            if (row[11:17] == '  CB  '):
                x = float(row[27:38])
                y = float(row[38:46])
                z = float(row[46:54])
                flag = 1
            if (row[11:17] == '  CA  ' and flag == 0):
                x = float(row[27:38])
                y = float(row[38:46])
                z = float(row[46:54])
    trans.append([x, y, z])
    Trans = np.array(trans)

    y = []
    for i in range(Trans.__len__()):
        y.append(Trans)
    y = np.array(y)
    # print(y)
    x = y.transpose(1, 0, 2)
    # print(x)
    a = np.linalg.norm(np.array(x) - np.array(y), axis=2)

    a = 2 / (1 + a / 4)
    for i in range(len(a)):
        a[i, i] = 1
    return a

def main(name,pdb_path,features_path,input_path,target_path):
    seq, sec_str = dssp_generate('raw_features/', name)
    target = seq

    f150 = np.array(sec_str)
    f150 = np.concatenate((f150, om_generate(features_path, name)), axis=0)
    f150 = np.concatenate((f150, theta_generate(features_path, name)), axis=0)

    f150 = np.concatenate((f150, energy_generate(features_path, name)),axis=0)
    f150 = np.concatenate((f150, fragment_generate(features_path, name)), axis=0)

    np.save(f'{input_path}sequential_features/{name}.npy', f150)

    target = np.array(target)
    np.save(f'{target_path}{name}.npy', target)

    a=f2dgenerate(pdb_path,name)
    np.save(f'{input_path}pairwise_features/{name}.npy', a)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--preprocess_list', type=str, required=True, help='the path of a preprocess pdb list')
    parser.add_argument('--pdb_path', type=str, default='raw_pdbs/', help='the path of pdb')
    parser.add_argument('--features_path', type=str, default='raw_features/', help='the path of features')
    parser.add_argument('--input_path', type=str, default='input/test/', help='the path of input to save')
    parser.add_argument('--target_path', type=str, default='target/test/', help='the path of target to save')

    config = parser.parse_args()
    with open(config.preprocess_list) as f:
        nameList=f.readlines()
    for name in nameList:
        main(name,config.pdb_path,config.features_path,config.input_path,config.target_path)
