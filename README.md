# Detectron_FocalLoss
add focal loss to fpn
# install caffe2
https://github.com/caffe2/caffe2
# install Detectron_FocalLoss
git clone https://github.com/withyou1771/Detectron_FocalLoss.git
install Detectron_FocalLoss refer to https://github.com/facebookresearch/Detectron
# train your data
(1)convert xml to json
python tools/xml_to_json.py
you should change
xml_path = ''
json_file = ''

(2)set catalog
add yourdata to
lib/datasets/dataset_catalog.py

(3)download model and save to experiments

(4)experiments/faster_rcnn_R-50-FPN_Focalloss.yaml
NUM_CLASSES:
STEPS: 
WEIGHTS:
DATASETS:
LOSS_GAMMA: 2.0
LOSS_ALPHA: 0.25

(5)run
cd run_train
sh train_faster_fpn_fl.sh

(6)analysis loss
python tools/draw_loss_one.py
you should change
log_path =''
img_path = ''

(7)test one model
CUDA_VISIBLE_DEVICES=0 python2 tools/test_net.py --cfg det_logo_all/publish_logo_6_faster_rcnn_R-50-FPN_fl.yaml TEST.WEIGHTS output/train/yourdata/generalized_rcnn/model_final.pkl NUM_GPUS 1

(8)Batch test model
Save once every iteration 4000 times
Batch test model and choose the best one
python tools/test_list.py --model_root /path/to/model --yaml_path experiments/faster_rcnn_R-50-FPN_Focalloss.yaml --res_path /path/to/result.txt
