import logging
import os
import time
def callback():
    current_day=time.strftime('Y%-m%-d%',time.localtime())
    path='/c/Users/zhaoliang/var/log/python-'+str(current_day)
    os.chdir(path)
    if os.path.exists(path):
        os.chdir(path)
    with open('test.log','w+')as f:
        f.write(current_day)

    logging.basicConfig(filename='test.log',level=logging.DEBUG,datefmt='%Y-%M-%D %H:%M:%S',
    format='%(asctime)s %(name)-8s %(levelname)-8s[line:%(lineno)d]%(message)s')
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')
if __name__ == "__main__":
    callback()
    

