import os
import json
import datetime
import logging


def get_datetime():
    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time,'%Y-%m-%d-%H-%M-%S')
    return time_str

# json
def load_json(path):
    res = {}
    with open(path, 'r') as f:
        res = json.load(f)
    return res

def get_abs_path(rel_path):
    BASE_PATH = os.environ['BASE_PATH'] if 'BASE_PATH' in os.environ else '/Users/taohuadao/Downloads/UU/semester3/R&D/OffensiveLanguage/'
    return os.path.join(BASE_PATH, rel_path)

# path
def check_dir(path):
    try:
        if path and not os.path.exists(path):
            check_dir('/'.join(path.split('/')[:-1]))
            os.mkdir(path)
    except:
        print(f'Error! When make dir {path}, the path status is:{os.path.exists(path)}')

def get_log_path(cfg):
    path = cfg['outputs_path'] + cfg['time_str'] + '/'
    path = get_abs_path(path)
    check_dir(path)
    path += cfg['task'] + '_run.log'
    return path

def get_logger(cfg):
    logger = logging.getLogger(cfg['task'])
    logger.setLevel(logging.DEBUG)
    file_handle = logging.FileHandler(get_log_path(cfg), encoding='utf-8')
    file_handle.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    return logger

def get_ckpt_path(cfg):
    path = cfg['outputs_path'] + cfg['time_str'] + '/'
    check_dir(path)
    path += cfg['task'] + '_' + '{}.pkl'
    return path