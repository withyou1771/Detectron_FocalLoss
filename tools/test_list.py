#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
import commands
def parse_args():
    parser = argparse.ArgumentParser(description='Test a Fast R-CNN network')
    parser.add_argument(
        '--model_root',
        dest='model_root',
        default=None,
        type=str
    )
    parser.add_argument(
        '--yaml_path',
        dest='yaml_path',
        default=None,
        type=str
    )
    parser.add_argument(
        '--res_path',
        dest='res_path',
        default=None,
        type=str
    )
    return parser.parse_args()


def get_modellist(model_root):
    """ 生成模型列表 """
    model_list = [os.path.join(model_root, f) for f in os.listdir(model_root) if f.endswith('.pkl')]
    return model_list

def main(model_root,yaml_path,res_path):
    model_list = get_modellist(model_root)
    res_list = []

    for item in model_list:
        model_weight = os.path.basename(item)
        print model_weight
        cmd = 'CUDA_VISIBLE_DEVICES=2 python2 tools/test_net.py \
        --cfg '+yaml_path +' TEST.WEIGHTS '+item+' NUM_GPUS 1'
        (status, output) = commands.getstatusoutput(cmd)
        output = output.split('\n')
        res = output[-1].split(': ')[-1].split(',')

        res = [float(i) for i in res]
        print res
        res_list.append([model_weight] +res)
    print res_list
    res_list.sort(key=lambda x:x[1],reverse=True)
    print res_list
    f = open(res_path, 'w')
    for i in res_list:
        f.write(str(i) + '\n')







if __name__ == '__main__':
    args = parse_args()
    model_root = args.model_root
    yaml_path = args.yaml_path
    res_path = args.res_path
    main(model_root, yaml_path,res_path)
