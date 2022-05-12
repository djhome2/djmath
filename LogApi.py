#!/usr/bin/env python3

import logging
import time
import ctp_argv
import sys
import os

__author__ = 'dj'

logLevel = logging.WARNING
if(ctp_argv.is_debug()):
    logLevel = logging.INFO    

datetime_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(format=datetime_format, level=logging.INFO)
log = logging.getLogger('ctp')
log.setLevel(logLevel)
log.propagate = False
now = time.localtime()
today = '{:04d}-{:02d}-{:02d}'.format(now.tm_year, now.tm_mon, now.tm_mday)
# print('today: ', today)
hour_min = '{:02d}-{:02d}'.format(now.tm_hour, int(now.tm_min / 15))
# filename = '/dev/null'

log_path = ctp_argv.directory + '/log/' + ctp_argv.pgname + '/' + str(now.tm_year) + '/' + str(now.tm_mon) + '/' + str(now.tm_mday) + '/' + str(now.tm_hour)

if(not os.path.exists(log_path)):
    os.makedirs(log_path) 

log_filename = log_path + '/' + str(now.tm_min) + '.log'

# print('log filename: ', log_filename)

err_filename = ctp_argv.directory + '/' + 'log/' + ctp_argv.pgname + '-' + today + '.err'
# print('error filename: ', err_filename)


def add_log_handler(filename, filter2):
    apps_handler = logging.FileHandler(filename=filename)
    apps_formatter = logging.Formatter(datetime_format)
    apps_handler.setFormatter(apps_formatter)
    info_filter = logging.Filter()
    info_filter.filter = filter2
    apps_handler.addFilter(info_filter)
    log.addHandler(apps_handler)    


add_log_handler(log_filename, lambda record: record.levelno <= logging.INFO)
add_log_handler(err_filename, lambda record: record.levelno > logging.INFO)

# logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stdout)
log.addHandler(handler)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))  # 重点


sys.excepthook = handle_exception  # 重点

log.info('start...')
# log.error('err...')

