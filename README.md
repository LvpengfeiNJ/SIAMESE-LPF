# SIAMESE-LPF
Siamese系列

1、[SiamBAN](https://github.com/hqucv/siamban)
The full paper is available here. The raw results are here or here, extraction code: um9k. The code based on the PySOT.

# Other trackers
- UDT: Unsupervised Deep Tracking
- code: [matlab version](https://github.com/594422814/UDT), [pytorch version](https://github.com/594422814/UDT_pytorch)
---
- UDT: Unsupervised Deep Tracking
- code: [matlab version](https://github.com/594422814/UDT), [pytorch version](https://github.com/594422814/UDT_pytorch)

---
# Single-Object Visual Tracking: A Paper List [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

*A complete paper list of Single-Object Visual Tracking Algorithms, Surveys and Benchmarks of recent years. Different from existing paper list, this project doesn't simply category the papers by publishment, but from a tracking process perspective. Main Contributions and Novelties of each tracker paper is carefully studied, forming our taxonomy criteria. The investigation covers top conferences as AAAI, CVPR, ECCV, ICCV, ICML, IJCAI, NIPS and top journals as IJCV, TIP, PAMI, CSVT. Note that the list is not bijective, namely a single paper may appear in diverse contents.* 

## 1 Popular Benchmarks

- **A Refined Note for 7 Benchmarks**, Yuzhe Shi. [[project](https://github.com/YuzheSHI/Benchmarks-for-Single-Object-Visual-Tracking)]
- **OTB2015** Yi Wu, Jongwoo Lim, and Ming-Hsuan Yang, "Object Tracking Benchmark", PAMI, 2015. [[paper](https://ieeexplore.ieee.org/document/7001050)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/pami/WuLY15)] [[project](http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html)]
- **UAV123** Matthias Mueller, Neil Smith, and Bernard Ghanem, "A Benchmark and Simulator for UAV Tracking", ECCV, 2016. [[paper](https://link.springer.com/chapter/10.1007%2F978-3-319-46448-0_27)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/MuellerSG16)] [[project](https://uav123.org/)]
- **NFS** Hamed Kiani Galoogahi, Ashton Fagg, Chen Huang, Deva Ramanan and Simon Lucey, "Need for Speed: A Benchmark for Higher Frame Rate Object Tracking", ICCV, 2017.[[paper](https://arxiv.org/abs/1703.05884)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/GaloogahiFHRL17)] [[project](http://ci2cv.net/nfs/index.html)]
- **TrackingNet** Matthias Müller, Adel Bibi, Silvio Giancola, Salman Al-Subaihi, Bernard Ghanem, "TrackingNet: A Large-Scale Dataset and Benchmark for Object Tracking in the Wild", ECCV, 2018.[[paper](https://link.springer.com/chapter/10.1007%2F978-3-030-01246-5_19)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/MullerBGAG18)]  [[project](https://tracking-net.org/)]
- **LaSOT** Heng Fan, Liting Lin, Fan Yang, Peng Chu, Ge Deng, Sijia Yu, Yong Xu, Chunyuan Liao, Haibin Ling, "LaSOT: A High-quality Benchmark for Large-scale Single Object Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Fan_LaSOT_A_High-Quality_Benchmark_for_Large-Scale_Single_Object_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/FanLYCDYBXLL19)]  [[project](https://cis.temple.edu/lasot/)]
- **GOT-10k** Lianghua Huang, Xin Zhao and Kaiqi Huang, "GOT-10k: A Large High-Diversity Benchmark
  for Generic Object Tracking in the Wild", PAMI, 2019.[[paper](http://arxiv.org/abs/1810.11981)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1810-11981)] [[project](http://got-10k.aitestunion.com/)]
- **VOT** Matej Kristan, Jiri Matas, Aleš Leonardis, Tomáš Vojı́ř, Roman Pflugfelder, Gustavo Fernández, Georg Nebehay, Fatih Porikli and Luka Čehovin, "A Novel Performance Evaluation Methodology
  for Single-Target Trackers", PAMI, 2016. [[paper](https://ieeexplore.ieee.org/document/7379002)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/pami/KristanMLVPFNPC16)] [[challenge](http://votchallenge.net/)] [[project](https://github.com/votchallenge/vot-toolkit)] [[publications](https://prints.vicos.si/publications/groups/vot/)]

## 2 Reviews and Survey Papers

- Alper Yilmaz, Omar Javed, Mubarak Shah, "Object Tracking: A Survey", CSUR, 2006.
  [[paper](https://doi.org/10.1145/1177352.1177355)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/csur/YilmazJS06)] 

- Xi Li, Weiming Hu, Chunhua Shen, Zhongfei Zhang, Anthony Dick, Anton van den Hengel, "A Survey of Appearance Models in Visual Object Tracking", ACM IST, 2013.
  [[paper](https://doi.org/10.1145/2508037.2508039)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tist/LiHSZDH13)] 

- Seyed Mojtaba Marvasti-Zadeh, Li Cheng, Hossein Ghanei-Yakhdan, and Shohreh Kasaei, "Deep Learning for Visual Tracking: A Comprehensive Survey", IEEE Access, 2019.
  [[paper](https://link.springer.com/chapter/10.1007%2F978-3-030-01246-5_19)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/MullerBGAG18)] 

- MUSTANSAR FIAZ, ARIF MAHMOOD, SAJID JAVED, SOON KI JUNG, "Handcrafted and Deep Trackers: Recent Visual Object Tracking Approaches and Trends", CSUR, 2019

  [[paper](https://doi.org/10.1145/3309665)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/csur/FiazMJJ19)] 

- Shaoze You, Hua Zhu, Menggang Li, Yutan Li, "A Review of Visual Trackers and Analysis of its Application to Mobile Robot", CoRR/abs, 2019
  .[[paper](http://arxiv.org/abs/1910.09761)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1910-09761)] 

- RUI YAO, GUOSHENG LIN, SHIXIONG XIA, JIAQI ZHAO and YONG ZHOU, "Video Object Segmentation and Tracking: A Survey", CoRR/abs, 2019
  [[paper](http://arxiv.org/abs/1904.09172)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1904-09172)] 

## 3 Recent Trackers

### 3.1 Data Augmentation 

#### 3.1.1 Sampling

- **SINT++** Xiao Wang, Chenglong Li, Bin Luo, Jin Tang, "SINT++: Robust Visual Tracking via Adversarial Positive Instance Generation", CVPR, 2018. [[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Wang_SINT_Robust_Visual_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangL0T18)] 

- **VITAL** Yibing Song, Chao Ma, Xiaohe Wu, Lijun Gong, Linchao Bao, Wangmeng Zuo, Chunhua Shen, Rynson W.H. Lau and Ming-Hsuan Yang, "VITAL: VIsual Tracking via Adversarial Learning", CVPR, 2018. [[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Song_VITAL_VIsual_Tracking_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Song0WGBZSL018)] [[code](https://github.com/ybsong00/Vital_release)]

- **PAT** Rey Reza Wiyatno, Anqi Xu, "Physical Adversarial Textures That Fool Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1904.11042)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1904-11042)] 

  #### 3.1.2 Offline Training

- **SINT** Ran Tao, Efstratios Gavves, Arnold W.M. Smeulders, "Siamese Instance Search for Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.158)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/TaoGS16)] [[code](https://github.com/taotaoorange/SINT)]

- **STCT** Lijun Wang, Wanli Ouyang, Xiaogang Wang and Huchuan Lu, "STCT: Sequentially Training Convolutional Networks for Visual Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.153)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangOWL16)] [[code](https://github.com/scott89/STCT)]

- **GOTURN** David Held, Sebastian Thrun, Silvio Savarese, "Learning to Track at 100 FPS with Deep
  Regression Networks", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-46448-0_45)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/HeldTS16)] [[code](https://github.com/davheld/GOTURN)]

- **SiameseFC** Luca Bertinetto, Jack Valmadre, João F. Henriques, Andrea Vedaldi, Philip H. S. Torr, "Fully-Convolutional Siamese Networks for Object Tracking", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-48881-3_56)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/BertinettoVHVT16)] [[code](https://github.com/rafellerc/Pytorch-SiamFC)]

- **CFNet** Luca Bertinetto, Jack Valmadre, João F. Henriques, Andrea Vedaldi, Philip H. S. Torr, "End-to-end representation learning for Correlation Filter based tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.531)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ValmadreBHVT17)] [[code](https://github.com/bertinetto/cfnet)]

- **UCT** Zheng Zhu, Guan Huang, Wei Zou, Dalong Du, Chang Huang, "UCT: Learning Unified Convolutional Networks for Real-time Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.231)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/ZhuHZDH17)] [[code](https://github.com/zhengzhugithub/UCT)]

- **DSLT** Xiankai Lu, Chao Ma, Bingbing Ni, Xiaokang Yang, Ian Reid and Ming-Hsuan Yang, "Deep Regression Tracking with Shrinkage Loss", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01264-9_22)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/LuMNYRY18)]  [[code](https://github.com/chaoma99/DSLT)]

- **RTINet** Yingjie Yao, Xiaohe Wu, Lei Zhang, Shiguang Shan and Wangmeng Zuo, "Joint Representation and Truncated Inference Learning for Correlation Filter based Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01240-3_34)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/YaoWZSZ18)] [[code](https://github.com/tourmaline612/RTINet)]

- **DATRL** Shi Pu, Yibing Song, Chao Ma, Honggang Zhang, Ming-Hsuan Yang, "Deep Attentive Tracking via Reciprocative Learning", NIPS, 2018.[[paper](http://papers.nips.cc/paper/7463-deep-attentive-tracking-via-reciprocative-learning)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/nips/PuS0Z018)] [[code](https://ybsong00.github.io/nips18_tracking/index)]

- **SILOT** Eric Crawford, Joelle Pineau, "Exploiting Spatial Invariance for Scalable Unsupervised Object Tracking", AAAI, 2020.[[paper](http://arxiv.org/abs/1911.09033)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1911-09033)] [[code](https://github.com/e2crawfo/silot)]

###### Unsupervised-Trained

- **UDT** Ning Wang, Yibing Song, Chao Ma, Wengang Zhou, Wei Liu, Houqiang Li, "Unsupervised Deep Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Unsupervised_Deep_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangS0ZLL19)] [[code](https://github.com/594422814/UDT)]

###### Meta-Learning Based

- **Meta-Tracker** Eunbyung Park, Alexander C. Berg, "Meta-Tracker: Fast and Robust Online Adaptation for Visual Object Trackers", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01219-9_35)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/ParkB18)] [[code](https://github.com/silverbottlep/meta_trackers)]
- **MLT** Janghoon Choi, Junseok Kwon, Kyoung Mu Lee, "Deep Meta Learning for Real-Time Target-Aware Visual Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1712.09153)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1712-09153)] 
- **RT-MLT** Ilchae Jung, Kihyun You, Hyeonwoo Noh, Minsu Cho, Bohyung Han, "Real-Time Object Tracking via Meta-Learning: Efficient Model Adaptation and One-Shot Channel Pruning", AAAI, 2020.[[paper](http://arxiv.org/abs/1911.11170)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1911-11170)] 

###### Reinforcement Learning Based Method:

- **ADNet** Sangdoo Yun, Jongwon Choi, Youngjoon Yoo, Kimin Yun and Jin Young Choi, "Action-Decision Networks for Visual Tracking with Deep Reinforcement Learning", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.148)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/YunCYYC17)]  [[code](https://github.com/hellbell/ADNet)]
- **EAST** Chen Huang, Simon Lucey, Deva Ramanan, "Learning Policies for Adaptive Tracking with Deep Feature Cascades", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.21)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/HuangLR17)] 
- **p-tracker** James Supančič III, Deva Ramanan, "Tracking as Online Decision-Making: Learning a Policy from Streaming Videos with Reinforcement Learning", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.43)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/SupancicR17)] 
- **HP** Xingping Dong, Jianbing Shen, Wenguan Wang, Yu Liu, Ling Shao, and Fatih Porikli, "Hyperparameter Optimization for Tracking with Continuous Deep Q-Learning", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Dong_Hyperparameter_Optimization_for_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/DongSWL0P18)] 
- **ACT** Boyu Chen, Dong Wang, Peixia Li, Shuang Wang and Huchuan Lu, "Real-time ‘Actor-Critic’ Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01234-2_20)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/ChenWLWL18)] [[code](https://github.com/bychen515/ACT)]
- **DRL-IS** Liangliang Ren, Xin Yuan, Jiwen Lu, Ming Yang, Jie Zhou, "Deep Reinforcement Learning with Iterative Shift for Visual Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01240-3_42)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/RenYLYZ18)] 
- **ConvNet-LSTM** Wenhan Luo, Peng Sun, Fangwei Zhong, Wei Liu, Tong Zhang, Yizhou Wang, "End-to-end Active Object Tracking via Reinforcement Learning", ICML, 2018.[[paper](http://proceedings.mlr.press/v80/luo18a.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/icml/LuoSZLZW18)] 
- **EDCF-EDSiam** Qiang Wang, Mengdan Zhang, Junliang Xing, Jin Gao, Weiming Hu, Steve Maybank, "Do not Lose the Details: Reinforced Representation Learning for High Performance Visual Tracking", IJCAI, 2018.[[paper](https://doi.org/10.24963/ijcai.2018/137)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/WangZXGHM18)] 
- **UJDPT** Xiaobai Liu, Donovan Lo, Chau Thuan, "Unsupervised Learning based Jump-Diffusion Process for Object Tracking in Video Surveillance", IJCAI, 2018.[[paper](https://doi.org/10.24963/ijcai.2018/702)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/LiuLT18)] 
- **JDPT** Xiaobai Liu, Qian Xu, Thuan Chau, Yadong Mu, Lei Zhu, Shuicheng Yan, "Revisiting Jump-Diffusion Process for Visual Tracking: A Reinforcement Learning Approach", CSVT, 2018.[[paper](https://doi.org/10.1109/TCSVT.2018.2862891)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tcsv/LiuXCMZY19)] 

### 3.2 Online Tracking

#### 3.2.1 Model Learning

- **RCF** Yao Sui, Ziming Zhang, Guanghui Wang, Yafei Tang, Li Zhang, "Real-Time Visual Tracking: Promoting the Robustness of Correlation Filter Learning", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-46484-8_40)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/SuiZWTZ16)] 
- **LearNet** Luca Bertinetto, Jack Valmadre, João F. Henriques, Andrea Vedaldi, Philip H. S. Torr, "Learning feed-forward one-shot learners", NIPS, 2016.[[paper](http://papers.nips.cc/paper/6068-learning-feed-forward-one-shot-learners)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/nips/BertinettoHVTV16)] 
- **CFNN** Yang Li, Zhan Xu and Jianke Zhu, "CFNN: Correlation Filter Neural Network for Visual Object Tracking", IJCAI, 2017.[[paper](https://doi.org/10.24963/ijcai.2017/309)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/LiXZ17)] [[code](https://github.com/zhan-xu/CFNN)]
- **MKCFup** Ming Tang, Bin Yu, Fan Zhang and Jinqiao Wang, "High-speed Tracking with Multi-kernel Correlation Filters", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Tang_High-Speed_Tracking_With_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/TangYZW18)] [[code](https://github.com/tominute/MKCFup)]
- **DiMP** Goutam Bhat, Martin Danelljan, Luc Van Gool, Radu Timofte, "Learning Discriminative Model Prediction for Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1904.07220)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1904-07220)] [[code](https://github.com/visionml/pytracking)]
- **RT-MLT** Ilchae Jung, Kihyun You, Hyeonwoo Noh, Minsu Cho, Bohyung Han, "Real-Time Object Tracking via Meta-Learning: Efficient Model Adaptation and One-Shot Channel Pruning", AAAI, 2020.[[paper](http://arxiv.org/abs/1911.11170)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1911-11170)] 

#### 3.2.2 Input: Target Representation

- **HDT** Yuankai Qi, Shengping Zhang, Lei Qin, Hongxun Yao, Qingming Huang, Jongwoo Lim, Ming-Hsuan Yang, "Hedged Deep Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.466)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/QiZQYHL016)] [[code](https://github.com/JHvisionchen/HDT-matlab)]
- **SCT** Jongwon Choi, Hyung Jin Chang, Jiyeoup Jeong, Yiannis Demiris, Jin Young Choi, "Visual Tracking Using Attention-Modulated Disintegration and Integration", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.468)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ChoiCJDC16)] [[code](https://github.com/jongwon20000/SCT)]
- **Staple** Luca Bertinetto, Jack Valmadre, Stuart Golodetz, Ondrej Miksik, Philip H.S. Torr, "Staple: Complementary Learners for Real-Time Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.156)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/BertinettoVGMT16)] [[code](https://github.com/bertinetto/staple)]
- **BranchOut** Bohyung Han, Jack Sim, Hartwig Adam, "BranchOut: Regularization for Online Ensemble Tracking with Convolutional Neural Networks", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.63)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/HanSA17)] 
- **SANet** Heng Fan, Haibin Ling, "SANet: Structure-Aware Network for Visual Tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPRW.2017.275)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/FanL17)] [[code](https://github.com/JHvisionchen/SANet-matlab)]
- **CFWCR** Zhiqun He, Yingruo Fan, Junfei Zhuang, Yuan Dong, HongLiang Bai, "Correlation Filters with Weighted Convolution Responses", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.233)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/HeFZDB17)] [[code](https://github.com/JHvisionchen/CFWCR-matlab)]
- **RFL** Tianyu Yang, Antoni B. Chan, "Recurrent Filter Learning for Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.235)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/YangC17)] [[code](https://github.com/skyoung/RFL)]
- **DNT** Zhizhen Chi, Hongyang Li, Huchuan Lu and Ming-Hsuan Yang, "Dual Deep Network for Visual Tracking", TIP, 2017.[[paper](https://doi.org/10.1109/TIP.2017.2669880)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tip/ChiLL017)] [[code](https://github.com/chizhizhen/DNT)]
- **adaDDCF** Zhenjun Han, Pan Wang, Qixiang Ye, "Adaptive Discriminative Deep Correlation Filter for
  Visual Object Tracking", CSVT, 2018.[[paper](https://doi.org/10.1109/TCSVT.2018.2888492)] [[bib](hhttps://dblp.uni-trier.de/rec/bibtex/journals/tcsv/HanWY20)] 
- **MCCT** Ning Wang, Wengang Zhou, Qi Tian, Richang Hong, Meng Wang, Houqiang Li, "Multi-Cue Correlation Filters for Robust Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Wang_Multi-Cue_Correlation_Filters_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangZ0H0L18)] [[code](https://github.com/JHvisionchen/MCCT-matlab)]
- **SA-Siam** Anfeng He, Chong Luo, Xinmei Tian, and Wenjun Zeng, "A Twofold Siamese Network for Real-Time Object Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/He_A_Twofold_Siamese_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/HeLTZ18)] [[code](https://github.com/HaHuangChan/SA-Siam)]
- **TRACA** Jongwon Choi, Hyung Jin Chang, Tobias Fischer, Sangdoo Yun, "Context-aware Deep Feature Compression for High-speed Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Choi_Context-Aware_Deep_Feature_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ChoiC0YLJD018)] [[code](https://github.com/jongwon20000/TRACA)]
- **Siam-tri** Xingping Dong and Jianbing Shen, "Triplet Loss in Siamese Network for Object Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01261-8_28)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/DongS18)] [[code](https://github.com/shenjianbing/TripletTracking)]
- **UPDT** Goutam Bhat, Joakim Johnander, Martin Danelljan, Fahad Shahbaz Khan and Michael Felsberg, "Unveiling the Power of Deep Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01216-8_30)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/BhatJDKF18)] [[code](https://github.com/visionml/pytracking)]
- **CFWFI** Aishi Li, Ming Yang, Wanqi Yang, "Feature Integration with Adaptive Importance Maps for Visual Tracking", IJCAI, 2018.[[paper](https://doi.org/10.24963/ijcai.2018/108)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/LiYY18)] 
- **EDCF-EDSiam** Qiang Wang, Mengdan Zhang, Junliang Xing, Jin Gao, Weiming Hu, Steve Maybank, "Do not Lose the Details: Reinforced Representation Learning for High Performance Visual Tracking", IJCAI, 2018.[[paper](https://link.springer.com/chapter/10.1007%2F978-3-030-01246-5_19)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/WangZXGHM18)] 
- **HCFT** Chao Ma, Jia-Bin Huang, Xiaokang Yang, and Ming-Hsuan Yang, "Robust Visual Tracking via Hierarchical Convolutional Features", PAMI, 2019. [[paper](https://ieeexplore.ieee.org/document/8434334)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/pami/0004HY019)] [[code](https://github.com/chaoma99/HCFTstar)]
- **LASRT** Yuankai Qi, Shengping Zhang, Weigang Zhang, Li Su, Qingming Huang, Ming-Hsuan Yang, "Learning Attribute-Specific Representations for Visual Tracking", AAAI, 2019.[[paper](https://doi.org/10.1609/aaai.v33i01.33018835)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/aaai/QiZZSH019)] 
- **CIR (SiamDW)** Zhipeng Zhang, Houwen Peng, Qiang Wang, Bing Li, "Deeper and Wider Siamese Networks for Real-Time Visual Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Zhang_Deeper_and_Wider_Siamese_Networks_for_Real-Time_Visual_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ZhangP19)] [[code](https://github.com/researchmm/SiamDW)]
- **C-RPN** Heng Fan, Haibin Ling, "Siamese Cascaded Region Proposal Networks for Real-Time Visual Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Fan_Siamese_Cascaded_Region_Proposal_Networks_for_Real-Time_Visual_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/FanL19)] 
- **OTR** Uğur Kart, Alan Lukežič, Matej Kristan, Joni-Kristian Kämäräinen and Jiřı́ Matas, "Object Tracking by Reconstruction with View-Specific Discriminative Correlation Filters", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Kart_Object_Tracking_by_Reconstruction_With_View-Specific_Discriminative_Correlation_Filters_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/KartLKKM19)] 
- **SiamRPN++** Bo Li, Wei Wu, Qiang Wang, Fangyi Zhang, Junliang Xing, Junjie Yan, "SiamRPN++: Evolution of Siamese Visual Tracking with Very Deep Networks", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Li_SiamRPN_Evolution_of_Siamese_Visual_Tracking_With_Very_Deep_Networks_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LiWWZXY19)] [[code](https://github.com/PengBoXiangShang/SiamRPN_plus_plus_PyTorch)]
- **GFS-DCF** Tianyang Xu, Zhen-Hua Feng, Xiao-Jun Wu, Josef Kittler, "Joint Group Feature Selection and Discriminative Filter Learning for Robust Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1907.13242)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1907-13242)] [[code](https://github.com/XU-TIANYANG/GFS-DCF)]
- **MLT** Janghoon Choi, Junseok Kwon, Kyoung Mu Lee, "Deep Meta Learning for Real-Time Target-Aware Visual Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1712.09153)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1712-09153)] 
- **LADCF** Tianyang Xu, Zhen-Hua Feng, Xiao-Jun Wu, and Josef Kittler, "Learning Adaptive Discriminative Correlation Filters via Temporal Consistency Preserving Spatial Feature Selection for Robust Visual Object Tracking", TIP, 2019. [[paper](https://ieeexplore.ieee.org/document/8728173)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tip/XuFWK19)] [[code](https://github.com/XU-TIANYANG/LADCF)]

#### 3.2.3 Input: Spatial Information

- **EBT** Gao Zhu, Fatih Porikli, and Hongdong Li, "Beyond Local Search: Tracking Objects Everywhere with Instance-Specific Proposals", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.108)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ZhuPL16)] [[code](https://github.com/GaoCode/EBT)]
- **C-COT** Martin Danelljan, Andreas Robinson, Fahad Shahbaz Khan, Michael Felsberg, "Beyond Correlation Filters: Learning Continuous Convolution Operators for Visual Tracking", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-46454-1_29)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/DanelljanRKF16)] [[code](https://github.com/martin-danelljan/Continuous-ConvOp)]
- **CFAT** Adel Bibi, Matthias Mueller, Bernard Ghanem, "Target Reponse Adaption for Correlation Filter Tracking", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-46466-4_25)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/BibiMG16)] 
- **LGCF** Heng Fan, Jinhai Xiang, "Robust Visual Tracking via Local-Global Correlation Filter", AAAI, 2017.[[paper](http://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14351)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/aaai/FanX17)] 
- **CACF** Matthias Mueller, Neil Smith, Bernard Ghanem, "Context-Aware Correlation Filter Tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.152)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/MuellerSG17)] [[code](https://ivul.kaust.edu.sa/Pages/pub-ca-cf-tracking.aspx)]
- **CSR-DCF** Alan Lukežič, Tomáš Vojı́ř, Luka Čehovin Zajc, Jiřı́ Matas and Matej Kristan, "Discriminative Correlation Filter with Channel and Spatial Reliability", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.515)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LukezicVZMK17)]  [[code](https://github.com/alanlukezic/csr-dcfnakan)]

- **BACF** Hamed Kiani Galoogahi, Ashton Fagg and Simon Lucey, "Learning Background-Aware Correlation Filters for Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.129)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/GaloogahiFL17)] [[code](https://github.com/4kubo/bacf_python)]
- **DRT** Junyu Gao, Tianzhu Zhang, Xiaoshan Yang and Changsheng Xu, "Deep Relative Tracking", TIP, 2017.[[paper](https://doi.org/10.1109/TIP.2017.2656628)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tip/GaoZYX17)] 
- **HART** Adam R. Kosiorek, Alex Bewley, Ingmar Posner, "Hierarchical Attentive Recurrent Tracking", NIPS, 2017.[[paper](http://papers.nips.cc/paper/6898-hierarchical-attentive-recurrent-tracking)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/nips/KosiorekBP17)] [[code](https://github.com/akosiorek/hart)]
- **DRT** Chong Sun, Dong Wang, Huchuan Lu, Ming-Hsuan Yang, "Correlation Tracking via Joint Discrimination and Reliability Learning", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Sun_Correlation_Tracking_via_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Sun0L018)] [[code](https://github.com/cswaynecool/DRT)]
- **LSART** Chong Sun, Dong Wang, Huchuan Lu, Ming-Hsuan Yang, "Learning Spatial-Aware Regressions for Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Sun_Learning_Spatial-Aware_Regressions_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Sun0L018a)] [[code](https://github.com/cswaynecool/LSART/tree/master/LSART)]
- **RASNet** Qiang Wang, Zhu Teng, Junliang Xing, Jin Gao, Weiming Hu, Stephen Maybank, "Learning Attentions: Residual Attentional Siamese Network for High Performance Online Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Wang_Learning_Attentions_Residual_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangTXGHM18)] [[code](https://github.com/HaHuangChan/RASNet)]
- **STRCF** Feng Li, Cheng Tian, Wangmeng Zuo, Lei Zhang, and Ming-Hsuan Yang, "Learning Spatial-Temporal Regularized Correlation Filters for Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Li_Learning_Spatial-Temporal_Regularized_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LiTZ0018)] [[code](https://github.com/lifeng9472/STRCF)]
- **DaSiamRPN** Zheng Zhu, Qiang Wang, Bo Li, Wei Wu, Junjie Yan and Weiming Hu, "Distractor-aware Siamese Networks for Visual Object Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01240-3_7)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/ZhuWLWYH18)] [[code](https://github.com/foolwood/DaSiamRPN)]
- **SACF** Mengdan Zhang, Qiang Wang, Junliang Xing, Jin Gao, Peixi Peng, "Visual Tracking via Spatially Aligned Correlation Filters Network", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01219-9_29)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/ZhangWXGPHM18)] 
- **StructSiam** Yunhua Zhang, Lijun Wang, Jinqing Qi, Dong Wang, Mengyang Feng and Huchuan Lu, "Structured Siamese Network for Real-Time Visual Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01240-3_22)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/ZhangWQWFL18)] [[code](https://github.com/xiaobai1217/StructSiam)]
- **DATRL** Shi Pu, Yibing Song, Chao Ma, Honggang Zhang, Ming-Hsuan Yang, "Deep Attentive Tracking via Reciprocative Learning", NIPS, 2018.[[paper](http://papers.nips.cc/paper/7463-deep-attentive-tracking-via-reciprocative-learning)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/nips/PuS0Z018)] [[code](https://ybsong00.github.io/nips18_tracking/index)]
- **RSST** Tianzhu Zhang, Changsheng Xu, and Ming-Hsuan Yang, "Robust Structural Sparse Tracking", PAMI, 2018.[[paper](https://doi.org/10.1109/TPAMI.2018.2797082)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/pami/ZhangXY19a)] [[code](http://nlpr-web.ia.ac.cn/mmc/homepage/tzzhang/rsst.html)]
- **ASRCF** Kenan Dai, Dong Wang, Huchuan Lu, Chong Sun, Jianhua Li, "Visual Tracking via Adaptive Spatially-Regularized Correlation Filters", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Dai_Visual_Tracking_via_Adaptive_Spatially-Regularized_Correlation_Filters_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Dai0LSL19)] [[code](https://github.com/Daikenan/ASRCF)]
- **GCT** Junyu Gao, Tianzhu Zhang and Changsheng Xu, "Graph Convolutional Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Gao_Graph_Convolutional_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/GaoZX19)] [[code](https://github.com/leoandeol/graph-convolutional-tracking)]
- **RPCF** Yuxuan Sun, Chong Sun, Dong Wang, You He, Huchuan Lu, "ROI Pooled Correlation Filters for Visual Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Sun_ROI_Pooled_Correlation_Filters_for_Visual_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/SunSWHL19)] [[code](https://github.com/rumsyx/RPCF)]
- **TADT** Xin Li, Chao Ma, Baoyuan Wu, Zhenyu He, Ming-Hsuan Yang, "Target-Aware Deep Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Li_Target-Aware_Deep_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Li0WH019)] [[code](https://github.com/XinLi-zn/TADT)]
- **ARCF** Ziyuan Huang, Changhong Fu, Yiming Li, Fuling Lin and Peng Lu, "Learning Aberrance Repressed Correlation Filters for Real-Time UAV Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1908.02231)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1908-02231)] [[code](https://github.com/vision4robotics/ARCF-tracker)]
- **GFS-DCF** Tianyang Xu, Zhen-Hua Feng, Xiao-Jun Wu, Josef Kittler, "Joint Group Feature Selection and Discriminative Filter Learning for Robust Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1907.13242)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1907-13242)] [[code](https://github.com/XU-TIANYANG/GFS-DCF)]
- **SPST** Qintao Hu, Lijun Zhou, Xiaoxiao Wang, Yao Mao, Jianlin Zhang, Qixiang Ye, "SPSTracker: Sub-Peak Suppression of Response Map for Robust Object Tracking", AAAI, 2020.[[paper](http://arxiv.org/abs/1912.00597)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1912-00597)] [[code](https://github.com/TrackerLB/SPSTracker)]

#### 3.2.4 Input: Temporal Information

- **AMCT** Donghun Yeo, Jeany Son, Bohyung Han, Joon Hee Han, "Superpixel-based Tracking-by-Segmentation using Markov Chains", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.62)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/YeoSHH17)] [[code](https://github.com/hanulbogo/AMCT)]
- **DSiam** Qing Guo, Wei Feng, Ce Zhou, Rui Huang, Liang Wan, Song Wang, "Learning Dynamic Siamese Network for Visual Object Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.196)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/Guo0ZHWW17)] [[code](https://github.com/tsingqguo/DSiam)]
- **TSN** Zhu Teng, Junliang Xing, Qiang Wang, Congyan Lang, Songhe Feng, Yi Jin, "Robust Object Tracking based on Temporal and Spatial Deep Networks", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.130)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/TengXWLFJ17)] 
- **FlowTrack** Zheng Zhu, Wei Wu, Wei Zou, Junjie Yan, "End-to-end Flow Correlation Tracking with Spatial-temporal Attention", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Zhu_End-to-End_Flow_Correlation_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ZhuWZY18)] [[code](https://github.com/zhengzhugithub/FlowTrack)]
- **RASNet** Qiang Wang, Zhu Teng, Junliang Xing, Jin Gao, Weiming Hu, Stephen Maybank, "Learning Attentions: Residual Attentional Siamese Network for High Performance Online Visual Tracking", CVPR, 2018. [[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Wang_Learning_Attentions_Residual_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangTXGHM18)] [[code](https://github.com/HaHuangChan/RASNet)]
- **STRCF** Feng Li, Cheng Tian, Wangmeng Zuo, Lei Zhang, and Ming-Hsuan Yang, "Learning Spatial-Temporal Regularized Correlation Filters for Visual Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Li_Learning_Spatial-Temporal_Regularized_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LiTZ0018)] [[code](https://github.com/lifeng9472/STRCF)]
- **MemTrack** Tianyu Yang and Antoni B. Chan, "Learning Dynamic Memory Networks for Object
  Tracking", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01240-3_10)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/YangC18)] [[code](https://github.com/skyoung/MemTrack)]
- **LCT+** Chao Ma, Jia-Bin Huang, Xiaokang Yang, Ming-Hsuan Yang, "Adaptive Correlation Filters with Long-Term and Short-Term Memory for Object Tracking", IJCV, 2018.[[paper](https://doi.org/10.1007/s11263-018-1076-4)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/ijcv/MaHYY18)]  [[code](https: //sites.google.com/site/chaoma99/cf-lstm)]
- **GCT** Junyu Gao, Tianzhu Zhang and Changsheng Xu, "Graph Convolutional Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Gao_Graph_Convolutional_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/GaoZX19)] [[code](https://github.com/leoandeol/graph-convolutional-tracking)]
- **GFS-DCF** Tianyang Xu, Zhen-Hua Feng, Xiao-Jun Wu, Josef Kittler, "Joint Group Feature Selection and Discriminative Filter Learning for Robust Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1907.13242)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1907-13242)] [[code](https://github.com/XU-TIANYANG/GFS-DCF)]
- **GradNet** Peixia Li, Boyu Chen, Wanli Ouyang, Dong Wang, Xiaoyun Yang, Huchuan Lu, "GradNet: Gradient-Guided Network for Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1909.06800)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1909-06800)] [[code](https://github.com/LPXTT/GradNet-Tensorflow)]
- **DSTN** Zhu Teng, Junliang Xing, Qiang Wang, Baopeng Zhang and Jianping Fan, "Deep Spatial and Temporal Network for Robust Visual Object Tracking", TIP, 2020.[[paper](https://doi.org/10.1109/TIP.2019.2942502)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/tip/TengXWZF20)] [[code](https://github.com/oywtece/dstn)]

#### 3.2.5 Output: Localization

- **MDNet** Hyeonseob Nam, Bohyung Han, "Learning Multi-Domain Convolutional Neural Networks for Visual Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.465)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/NamH16)] [[code](https://github.com/hyeonseobnam/MDNet)]
- **TrackingCompletion** Yao Sui, Guanghui Wang, Yafei Tang, Li Zhang, "Tracking Completion", ECCV, 2016.[[paper](https://doi.org/10.1007/978-3-319-46484-8_12)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/SuiWTZ16)] 
- **AFCN** Jongwon Choi, Hyung Jin Chang,Sangdoo Yun, Tobias Fischer, Yiannis Demiris, Jin Young Choi, "Attentional Correlation Filter Network for Adaptive Visual Tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.513)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ChoiCYFDC17)] [[code](https://github.com/jongwon20000/ACFN)]
- **LMCF** Mengmeng Wang, Yong Liu, Zeyi Huang, "Large Margin Object Tracking with Circulant Feature Maps", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.510)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangLH17)] [[code](https://github.com/sallymmx/LMCF)]
- **MCPF** Tianzhu Zhang, Changsheng Xu, Ming-Hsuan Yang, "Multi-task Correlation Particle Filter for Robust Object Tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.512)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ZhangX017)] [[code](http://nlpr-web.ia.ac.cn/mmc/homepage/tzzhang/mcpf.html)]
- **RaF** Le Zhang, Jagannadan Varadarajan, Ponnuthurai Nagaratnam Suganthan, Narendra Ahuja and Pierre Moulin, "Robust Visual Tracking Using Oblique Random Forests", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.617)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/ZhangVSAM17)] [[code](https://github.com/ZhangLeUestc/Incremental-Oblique-Random-Forest)]
- **CREST** Yibing Song, Chao Ma, Lijun Gong, Jiawei Zhang, Rynson W.H. Lau and Ming-Hsuan Yang, "CREST: Convolutional Residual Learning for Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.279)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/SongMGZL017)] [[code](https://github.com/ybsong00/CREST-Release)]
- **DSiam** Qing Guo, Wei Feng, Ce Zhou, Rui Huang, Liang Wan, Song Wang, "Learning Dynamic Siamese Network for Visual Object Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.196)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/Guo0ZHWW17)] [[code](https://github.com/tsingqguo/DSiam)]
- **PTAV** Heng Fan, Haibin Ling, "Parallel Tracking and Verifying: A Framework for Real-Time and High
  Accuracy Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.585)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/FanL17)] [[code](http://www.dabi.temple.edu/~hbling/code/PTAV/ptav.htm)]
- **SP-KCF** Xin Sun, Ngai-Man Cheung, Hongxun Yao, Yiluan Guo, "Non-Rigid Object Tracking via Deformable Patches using Shape-Preserved KCF and Level Sets", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCV.2017.586)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccv/SunCYG17)] 
- **MDSLT** Kunpeng, Yu Kong and Yun Fu, "Multi-Stream Deep Similarity Learning Networks for Visual Tracking", IJCAI, 2017.[[paper](https://doi.org/10.24963/ijcai.2017/301)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/LiKF17)] 
- **AOGT** Tianfu Wu, Yang Lu and Song-Chun Zhu, "Online Object Tracking, Learning and Parsing
  with And-Or Graphs", PAMI, 2017.[[paper](https://doi.org/10.1109/TPAMI.2016.2644963)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/pami/WuLZ17)] [[code](https://github.com/tfwu/RGM-AOGTracker)]
- **DEDT** Kourosh Meshgi, Shigeyuki Oba, Shin Ishii, "Efficient Diverse Ensemble for Discriminative Co-Tracking", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Meshgi_Efficient_Diverse_Ensemble_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/MeshgiOI18)] [[code](http://ishiilab.jp/member/meshgi-k/dedt.html#)]
- **SiamRPN** Bo Li, Junjie Yan, Wei Wu, Zheng Zhu, Xiaolin Hu, "High Performance Visual Tracking with Siamese Region Proposal Network", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Li_High_Performance_Visual_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LiYWZH18)] [[code](https://github.com/huanglianghua/siamrpn-pytorch)]
- **RT-MDNet** Ilchae Jung, Jeany Son, Mooyeol Baek and Bohyung Han, "Real-Time MDNet", ECCV, 2018.[[paper](https://doi.org/10.1007/978-3-030-01225-0_6)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/eccv/JungSBH18)] [[code](https://github.com/IlchaeJung/RT-MDNet)]
- **GPRT** Linyu Zheng, Ming Tang and Jinqiao Wang, "Learning Robust Gaussian Process Regression for Visual Tracking", IJCAI, 2018.[[paper](https://doi.org/10.24963/ijcai.2018/170)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/ijcai/ZhengTW18)] 
- **LDES** Yang Li, Jianke Zhu, Steven C.H. Hoi, Wenjie Song, Zhefeng Wang, Hantang Liu, "Robust Estimation of Similarity Transformation for Visual Object Tracking", AAAI, 2019.[[paper](https://doi.org/10.1609/aaai.v33i01.33018666)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/aaai/LiZHSWL19)] [[code](https://github.com/ihpdep/LDES)]
- **SPM** Guangting Wang, Chong Luo, Zhiwei Xiong, Wenjun Zeng, "SPM-Tracker: Series-Parallel Matching for Real-Time Visual Object Tracking", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Wang_SPM-Tracker_Series-Parallel_Matching_for_Real-Time_Visual_Object_Tracking_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/WangLXZ19)] [[code](https://github.com/microsoft/SPM-Tracker)]
- **Bridge** Lianghua Huang, Xin Zhao, Kaiqi Huang, "Bridging the Gap Between Detection and Tracking: A Unified Approach", ICCV, 2019.[[paper](http://arxiv.org/abs/1912.08531)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1912-08531)] 
- **SPLT** Bin Yan, Haojie Zhao, Dong Wang, Huchuan Lu and Xiaoyun Yang, "‘Skimming-Perusal’ Tracking: A Framework for Real-Time and Robust Long-term Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1909.01840)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1909-01840)] [[code](https://github.com/iiau-tracker/SPLT)]
- **SiamFC++** Yinda Xu, Zeyu Wang, Zuoxin Li, Ye Yuan, Gang Yu, "SiamFC++: Towards Robust and Accurate Visual Tracking with Target Estimation Guidelines", AAAI, 2020.[[paper](http://arxiv.org/abs/1911.06188)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1911-06188)] [[code](https://github.com/MegviiDetection/video_analyst)]
- **GlobalTrack** LianghuaHuang, XinZhao, KaiqiHuang, "GlobalTrack:ASimpleandStrongBaselineforLong-termTracking", AAAI, 2020. [[paper](https://arxiv.org/pdf/1912.08531.pdf)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1912-08531)] [[code](https://github.com/huanglianghua/GlobalTrack)]

#### 3.2.6 Output: Appearance

- **IBCCF** Feng Li, Yingjie Yao, Peihua Li, David Zhang, Wangmeng Zuo, and Ming-Hsuan Yang, "Integrating Boundary and Center Correlation Filters for Visual Tracking with Aspect Ratio Variation", ICCV Workshops, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.234)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/LiYLZZY17)] [[code](https://github.com/lifeng9472/IBCCF)]
- **PWSeg** Tobias Böttger, Patrick Follmann, "The Benefits of Evaluating Tracker Performance using Pixel-wise Segmentations", ICCV Workshops, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.232)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/BottgerF17)] 
- **SiamRPN** Bo Li, Junjie Yan, Wei Wu, Zheng Zhu, Xiaolin Hu, "High Performance Visual Tracking with Siamese Region Proposal Network", CVPR, 2018.[[paper](http://openaccess.thecvf.com/content_cvpr_2018/html/Li_High_Performance_Visual_CVPR_2018_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/LiYWZH18)] [[code](https://github.com/huanglianghua/siamrpn-pytorch)]
- **LDES** Yang Li, Jianke Zhu, Steven C.H. Hoi, Wenjie Song, Zhefeng Wang, Hantang Liu, "Robust Estimation of Similarity Transformation for Visual Object Tracking", AAAI, 2019.[[paper](https://doi.org/10.1609/aaai.v33i01.33018666)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/aaai/LiZHSWL19)]  [[code](https://github.com/ihpdep/LDES)]
- **ATOM** Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg, "ATOM: Accurate Tracking by Overlap Maximization", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Danelljan_ATOM_Accurate_Tracking_by_Overlap_Maximization_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/DanelljanBKF19)] [[code](https://github.com/visionml/pytracking)]
- **SiamMask** Qiang Wang, Li Zhang, Luca Bertinetto, Weiming Hu, Philip H.S. Torr, "Fast Online Object Tracking and Segmentation: A Unifying Approach", CVPR, 2019.[[paper](http://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Fast_Online_Object_Tracking_and_Segmentation_A_Unifying_Approach_CVPR_2019_paper.html)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/Wang0BHT19)] [[code](https://github.com/foolwood/SiamMask)]

#### 3.2.7 Updating: Sample

- **SRDCFdecon** Martin Danelljan, Gustav Häger, Fahad Shahbaz Khan, Michael Felsberg, "Adaptive Decontamination of the Training Set: A Unified Formulation for Discriminative Visual Tracking", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.159)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/DanelljanHKF16)] [[code](https://github.com/JHvisionchen/SRDCFdecon-matlab)]

#### 3.2.8 Updating: Model

- **DLSSVM** Jifeng Ning, Jimei Yang, Shaojie Jiang, Lei Zhang and Ming-Hsuan Yang, "Object Tracking via Dual Linear Structured SVM and Explicit Feature Map", CVPR, 2016.[[paper](https://doi.org/10.1109/CVPR.2016.462)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/NingYJZ016)] [[code](https://github.com/JHvisionchen/DLSSVM-matlab)]
- **ECO** Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, Michael Felsberg, "ECO: Efficient Convolution Operators for Tracking", CVPR, 2017.[[paper](https://doi.org/10.1109/CVPR.2017.733)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/cvpr/DanelljanBKF17)] [[code](https://github.com/martin-danelljan/ECO)]
- **UCT** Zheng Zhu, Guan Huang, Wei Zou, Dalong Du, Chang Huang, "UCT: Learning Unified Convolutional Networks for Real-time Visual Tracking", ICCV, 2017.[[paper](https://doi.org/10.1109/ICCVW.2017.231)] [[bib](https://dblp.uni-trier.de/rec/bibtex/conf/iccvw/ZhuHZDH17)] [[code](https://github.com/zhengzhugithub/UCT)]
- **Re^2EMA** Jianglei Huang, Wengang Zhou, "Re^2EMA: Regularized and Reinitialized Exponential
  Moving Average for Target Model Update in Object Tracking", AAAI, 2019.[[paper](https://doi.org/10.1007/s11042-019-7219-y)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/mta/HuangZTL19)] 
- **Bridge** Lianghua Huang, Xin Zhao, Kaiqi Huang, "Bridging the Gap Between Detection and Tracking: A Unified Approach", ICCV, 2019.[[paper](http://arxiv.org/abs/1912.08531)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1912-08531)] [[code-SSD](https://github.com/lufficc/SSD)] [[code-FasterRCNN](https://github.com/yingxingde/FasterRCNN-pytorch)]

###### Template Updating in Siamese-based Tracker

- **UpdateNet** Lichao Zhang, Abel Gonzalez-Garcia, Joost van de Weijer, Martin Danelljan, Fahad Shahbaz Khan, "Learning the Model Update for Siamese Trackers", ICCV, 2019.[[paper](https://arxiv.org/abs/1908.00855)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1908-00855)] [[code](https://github.com/zhanglichao/updatenet)]
- **GradNet** Peixia Li, Boyu Chen, Wanli Ouyang, Dong Wang, Xiaoyun Yang, Huchuan Lu, "GradNet: Gradient-Guided Network for Visual Object Tracking", ICCV, 2019.[[paper](http://arxiv.org/abs/1909.06800)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1909-06800)] [[code](https://github.com/LPXTT/GradNet-Tensorflow)]
- **DROL-RPN**  Jinghao Zhou, Peng Wang, Haoyang Sun, " Discriminative and Robust Online Learning for Siamese Visual Tracking ", AAAI, 2020. [[paper](https://arxiv.org/pdf/1909.02959.pdf)] [[bib](https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1909-02959)] [[code](https://github.com/shallowtoil/DROL)]
