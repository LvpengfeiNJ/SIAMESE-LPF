# encoding: utf-8
import os
import numpy as np
import cv2

# 选择第几个视频
# TODO:选择某个视频
video_num = 36

# TODO:数据集所在路径
# src_pic_path = '../data/OTB100'
src_pic_path = '/home/lpf/Desktop/dataset/OTB100'

all_pic = os.listdir(src_pic_path)  # 注意os.listdir获取到的路径是乱序的，要用.sort函数排序
all_pic.sort()

each_video_path = [os.path.join(src_pic_path, video_path) for video_path in all_pic]
# print(each_video_path)
# choose one video
one_video = each_video_path[video_num] # 
result = one_video.split('/')
video_name = result[len(result) - 1]
print('choosed video_name: ({})--'.format(video_num), video_name)

# TODO：算法评测结果所在路径
eval_result_path = './Results_OTB100'
all_eval_trackers = os.listdir(eval_result_path)
all_eval_trackers.sort()
each_eval_tracker = [os.path.join(eval_result_path, eval_tracker) for eval_tracker in all_eval_trackers]  # evaluation results of all trackers
each_eval_tracker.sort()
# print(each_eval_tracker)

# choose one tracker
one_tracker = each_eval_tracker[4]  # one_tracker is : ./Results_OTB100/ECO
print("one_tracker is : {}".format(one_tracker))
each_eval_result = os.listdir(one_tracker)
each_eval_result.sort()  # ['Basketball.txt', 'Biker.txt', 'Bird1.txt', ... ,'Walking2.txt', 'Woman.txt']
# print(each_eval_result)

# each_eval_result_path = [os.path.join(one_tracker, eval_result) for eval_result in each_eval_result]
# print(each_eval_result_path)
#
# ---------------------------------------------
all_trakcers_result = []
for tracker in each_eval_tracker:
    each_eval_result_path = [os.path.join(tracker, eval_result) for eval_result in each_eval_result]
    all_trakcers_result.append(each_eval_result_path)
# print('all_trackers_result', all_trakcers_result)  # [['./Results_OTB100/CCOT/Basketball.txt', ... ,], ...]
# ---------------------------------------------

print("all_trackers_result length is: {}".format(len(all_trakcers_result))) # 15 trackers
all_list = []  # a video of one tracker
for num in range(0, len(all_trakcers_result)):
    with open(all_trakcers_result[num][video_num]) as eval_result:  # choose a video of one tracker
        dataset = []
        lines = eval_result.readlines()

        # read datas in txt file, transform to String formation
        for line in lines:
            temp1 = line.strip('\n')
            temp2 = temp1.split('\t')
            dataset.append(temp2)

        new_dataset = [new_line[0].split(',') for new_line in dataset]  # .split(',')按逗号分割字符串
        # print('new_dataset', new_dataset)
        # str转化成int型
        for i in range(0, len(new_dataset)):
            for j in range(len(new_dataset[i])):
                new_dataset[i][j] = int(float(new_dataset[i][j]))
        all_list.append(new_dataset)

# print(all_list)
#
# every frame in a video
frames_list = os.listdir(os.path.join(one_video, 'img'))
frames_list.sort()
frames_path = [os.path.join(os.path.join(one_video, 'img'), frame_path) for frame_path in frames_list]

# print(frames_path)

# TODO：画图结果保存路径
dst_pic_path = './dst/'
dst_pic_path = dst_pic_path + video_name

# 判断是否有文件夹，如果没有则新建   如果有的话，说明已经生成过了。需要删除原文件后再次执行程序
f = os.path.exists(dst_pic_path)
if f is False:
    #
    os.makedirs(dst_pic_path)

    # show the tracking results
    for index, path in enumerate(frames_path):
        img = cv2.imread(path)
        # print(img.shape)
        # --------------------------------------
        # results of trackers
        # all_list[a][b] 解释：a为某个算法，b为某个算法的某帧结果
        # a 对应的算法 : CCOT CFNet DaSiamRPN DeepSRDCF ECO fDSST GradNet MDNet Ours OursOld SiamDWfc SiamDWrpn SiamFC SiamRPN SRDCF Staple
        # TODO:选择想要画的算法结果，注意：需要改all_list[a][index]中的a这一项
        # track_gt = all_list[15][index]  # Staple
        # # draw bounding boxes
        # cv2.rectangle(img, (track_gt[0], track_gt[1]), (track_gt[0] + track_gt[2], track_gt[1] + track_gt[3]), (255, 255, 255), thickness=2)  # 白色

        track_gt_1 = all_list[3][index]  # DeepSRDCF
        cv2.rectangle(img, (track_gt_1[0], track_gt_1[1]), (track_gt_1[0] + track_gt_1[2], track_gt_1[1] + track_gt_1[3]), (255, 0, 0), thickness=2)  # 蓝色

        track_gt_2 = all_list[13][index]  # SiamRPN
        cv2.rectangle(img, (track_gt_2[0], track_gt_2[1]), (track_gt_2[0] + track_gt_2[2], track_gt_2[1] + track_gt_2[3]), (0, 255, 0), thickness=2)  # 绿色

        # track_gt_3 = all_list[5][index]  # fDSST
        # cv2.rectangle(img, (track_gt_3[0], track_gt_3[1]), (track_gt_3[0] + track_gt_3[2], track_gt_3[1] + track_gt_3[3]), (0, 0, 255), thickness=1)

        # track_gt_4 = all_list[6][index]  # GradNet
        # cv2.rectangle(img, (track_gt_4[0], track_gt_4[1]), (track_gt_4[0] + track_gt_4[2], track_gt_4[1] + track_gt_4[3]), (255, 0, 255), thickness=2)  # 紫色
        #
        # track_gt_5 = all_list[8][index]  # Ours
        # cv2.rectangle(img, (track_gt_5[0], track_gt_5[1]), (track_gt_5[0] + track_gt_5[2], track_gt_5[1] + track_gt_5[3]), (0, 0, 255), thickness=2)  # 红色

        track_gt_6 = all_list[4][index]  # ECO
        cv2.rectangle(img, (track_gt_6[0], track_gt_6[1]), (track_gt_6[0] + track_gt_6[2], track_gt_6[1] + track_gt_6[3]), (0, 255, 255), thickness=2)  # 黄色

        track_gt_7 = all_list[12][index]  # SiamFC
        cv2.rectangle(img, (track_gt_7[0], track_gt_7[1]), (track_gt_7[0] + track_gt_7[2], track_gt_7[1] + track_gt_7[3]), (0, 0, 0), thickness=2)  # 黑色
        # --------------------------------------

        cv2.putText(img, '#{}'.format(index), (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        cv2.putText(img, video_name, (10, int(img.shape[0] * 0.9)), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

        cv2.imwrite(dst_pic_path + '/' + video_name + '_img_{}.jpg'.format(index), img)
       # cv2.imshow('src_img', img)
       # cv2.waitKey(0)
else:
    print('已经生成过({})，请删除原文件后重新执行程序'.format(video_name))
