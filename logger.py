import logging
import datetime

class LoggerClass:

    def __init__(self,clsname):
        self.clsname=clsname

    def getLogger(self):
        logger=logging.getLogger(self.clsname)
        logger.setLevel(logging.INFO)

        c_handler=logging.StreamHandler()
        nw=datetime.datetime.now()
        file_name=f'{nw.year}_{nw.month}_{nw.day}_{nw.hour}_{nw.minute}_{nw.second}'
        f_handler=logging.FileHandler(f'logs/{file_name}.log')
        c_handler.setLevel(logging.ERROR)
        f_handler.setLevel(logging.ERROR)
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)

        c_format=logging.Formatter('%(name)s-%(levelname)s-%(message)s')
        f_format=logging.Formatter('%(asctime)s::%(name)s::%(levelname)s::%(message)s',datefmt='%m-%d-%y-%H-%M-%S')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger