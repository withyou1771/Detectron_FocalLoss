# -*-coding:utf-8-*-
# Created Time: 2018-05-28
# Version:02

from PIL import ImageDraw, Image
import glob
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import simplejson
# from  ggplot import  *

def get_loss_list(log_path):
    log_path = open(log_path, 'r')

    log_list = []
    for i in log_path:
        log_list.append(i)

    i_list = []
    loss_list = []

    for i in range(0, len(log_list)):
        i = int(i)
        # print test_list[i]
        if (log_list[i].startswith('json_stats')):
            log =log_list[i][12:]
            log_dic = eval(log)
            i_list.append(log_dic['iter'])
            loss_list.append(log_dic['loss'])
    print i_list,loss_list
    return i_list,loss_list


def draw_loss(i_list,loss1,save_path):
    plt.xlabel('iteration')
    plt.ylabel('loss')
    plt.plot(i_list, loss1, markersize='1', label='FPN')
    plt.legend(loc='upper right')
    plt.savefig(save_path)
if __name__ == '__main__':
    log_path =''
    img_path = ''
    i_list, loss1 = get_loss_list(log_path)
    draw_loss(i_list, loss1, img_path)
