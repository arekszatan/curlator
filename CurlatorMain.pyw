import logging
from datetime import datetime
import FrontQT

if __name__ == "__main__":
    logName = datetime.today().strftime('%Y_%m_%d_logging.log')
    logging.basicConfig(level=logging.INFO, filename=logName, filemode='w',
                        format='%(asctime)s::%(levelname)s >>> %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Starting main ...')
    FrontQT.startAplication()


