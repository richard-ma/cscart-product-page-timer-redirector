#!/usr/bin/env python
# -*- conding: utf-8 -*-


import sys, getopt, os, re

# get current path
# https://blog.csdn.net/vitaminc4/article/details/78702852
current_path = os.path.split(os.path.realpath(__file__))[0]
# set working directory
os.chdir(current_path)

def generate_tag(keyword, value):
    return '/*{{'+keyword+'}}*/'+value+'/*{{/'+keyword+'}}*/'

def generate_tag_expression(keyword):
    expr = '\/\*{{'+keyword+'}}\*\/.*\/\*{{\/'+keyword+'}}\*\/'
    return expr

opts, args = getopt.getopt(sys.argv[1:], '-o:-t:', ["output=", "target_domain="])

replace_dict = dict()

for opt_name, opt_value in opts:
    # output filename
    if opt_name in ('-o', '--output'):
        output_filename = opt_value
        # todo: print and log
        print("OUTPUT Filename: %s" % (output_filename))

    # target_domain_with_protocol
    if opt_name in ('-t', '--target_domain'):
        replace_dict['target_domain'] = '\''+opt_value+'\''
        # todo: print and log
        print("target domain: %s" % (replace_dict['target_domain']))

template_filename = output_filename
generated_lines = list()
with open(template_filename, 'r') as f:
    for line in f.readlines():
        for k, v in replace_dict.items():
            line = re.sub(generate_tag_expression(k), generate_tag(k, v), line)
        generated_lines.append(line)

with open(output_filename, 'w') as f:
    f.writelines(generated_lines)