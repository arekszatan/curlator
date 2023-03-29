import logging
import FrontQT

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logi.log', filemode='w',
                        format='%(asctime)s::%(levelname)s >>> %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Starting main ...')
    FrontQT.startAplication()


