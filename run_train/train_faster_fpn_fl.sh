#!/usr/bin/env bash
cd ..
CUDA_VISIBLE_DEVICES=0 python tools/train_net.py --cfg experiments/faster_rcnn_R-50-FPN_Focalloss.yaml OUTPUT_DIR output >run_train/train_FPN_fl_2_25.log