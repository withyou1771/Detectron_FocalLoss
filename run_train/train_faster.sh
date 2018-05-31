#!/usr/bin/env bash
cd ..
CUDA_VISIBLE_DEVICES=0 python tools/train_net.py --cfg experiments/faster_rcnn_R-50 OUTPUT_DIR output >run_train/train_faster.log