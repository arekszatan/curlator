import logging
import FrontQT

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='logi.log', filemode='w',
                        format='%(asctime)s::%(levelname)s >>> %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.debug('Starting main ...')
    FrontQT.startAplication()


