# -*- coding: utf-8 -*-
# @Author       : William
# @Project      : TextGAN-william
# @FileName     : run_seqgan.py
# @Time         : Created at 2019-05-27
# @Blog         : http://zhiweil.ml/
# @Description  : 
# Copyrights (C) 2018. All Rights Reserved.
import nltk
nltk.download('punkt')

import sys
from subprocess import call
import argparse

import os

def parse_args():
    parser = argparse.ArgumentParser(description='Author Text Classifier')
    
    # parser.add_argument('--job-id', type=int, default=3)
    parser.add_argument('--dataset', type=str, default='shakespeare', help='Name of dataset to use. Must match with the file in ./dataset/ and ./dataset/testdata/.')
    parser.add_argument('--real-data', type=int, default=1, help='Set to 0 if synthetic data. Set to 1 for real data.')
    parser.add_argument('--vocab-size', type=int, default=0, help='Vocab size. Set 0 for real data.')
    args = parser.parse_args()
    return args

seqgan_args = parse_args()

# Executables
executable = 'python'  # specify your own python interpreter path here
rootdir = '../'
scriptname = 'main.py'

# ===Program===
if_test = int(False)
run_model = 'seqgan'
CUDA = int(True)
oracle_pretrain = int(True)
gen_pretrain = int(False)
dis_pretrain = int(False)
MLE_train_epoch = 120
ADV_train_epoch = 200
tips = 'SeqGAN experiments'

# ===Oracle  or Real===
# if_real_data = [int(False), int(True), int(True), int(True)]
# dataset = ['oracle', 'image_coco', 'emnlp_news', 'shakespeare']
# vocab_size = [5000, 0, 0, 0]

# ===Basic Param===
data_shuffle = int(False)
model_type = 'vanilla'
gen_init = 'normal'
dis_init = 'uniform'
samples_num = 10000
batch_size = 64
max_seq_len = 20
gen_lr = 0.01
dis_lr = 1e-4
pre_log_step = 10
adv_log_step = 1

# ===Generator===
ADV_g_step = 1
rollout_num = 16
gen_embed_dim = 32
gen_hidden_dim = 32

# ===Discriminator===
d_step = 5
d_epoch = 3
ADV_d_step = 4
ADV_d_epoch = 2
dis_embed_dim = 64
dis_hidden_dim = 64

# ===Metrics===
use_nll_oracle = int(True)
use_nll_gen = int(True)
use_nll_div = int(True)
use_bleu = int(True)
use_self_bleu = int(True)
use_ppl = int(False)

args = [
    # Program
    '--if_test', if_test,
    '--run_model', run_model,
    '--cuda', CUDA,
    # '--device', gpu_id,  # comment for auto GPU
    '--ora_pretrain', oracle_pretrain,
    '--gen_pretrain', gen_pretrain,
    '--dis_pretrain', dis_pretrain,
    '--mle_epoch', MLE_train_epoch,
    '--adv_epoch', ADV_train_epoch,
    '--tips', tips,

    # Oracle or Real
    # '--if_real_data', if_real_data[args2.job_id],
    # '--dataset', dataset[args2.job_id],
    # '--vocab_size', vocab_size[args2.job_id],
    
    '--if_real_data', seqgan_args.real_data,
    '--dataset', seqgan_args.dataset,
    '--vocab_size', seqgan_args.vocab_size,

    # Basic Param
    '--shuffle', data_shuffle,
    '--model_type', model_type,
    '--gen_init', gen_init,
    '--dis_init', dis_init,
    '--samples_num', samples_num,
    '--batch_size', batch_size,
    '--max_seq_len', max_seq_len,
    '--gen_lr', gen_lr,
    '--dis_lr', dis_lr,
    '--pre_log_step', pre_log_step,
    '--adv_log_step', adv_log_step,

    # Generator
    '--adv_g_step', ADV_g_step,
    '--rollout_num', rollout_num,
    '--gen_embed_dim', gen_embed_dim,
    '--gen_hidden_dim', gen_hidden_dim,

    # Discriminator
    '--d_step', d_step,
    '--d_epoch', d_epoch,
    '--adv_d_step', ADV_d_step,
    '--adv_d_epoch', ADV_d_epoch,
    '--dis_embed_dim', dis_embed_dim,
    '--dis_hidden_dim', dis_hidden_dim,

    # Metrics
    '--use_nll_oracle', use_nll_oracle,
    '--use_nll_gen', use_nll_gen,
    '--use_nll_div', use_nll_div,
    '--use_bleu', use_bleu,
    '--use_self_bleu', use_self_bleu,
    '--use_ppl', use_ppl,
]

args = list(map(str, args))
my_env = os.environ.copy()
call([executable, scriptname] + args, env=my_env, cwd=rootdir, shell=True)
# call(['python', 'print.py'], env=my_env, cwd='D:/Dewen/GitHub/EEE486-Project/textGAN/', shell=True)
