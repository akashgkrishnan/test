import logging


def test_logginPractice():
    logger = logging.getLogger(__name__)
    log_format = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(name)s : %(message)s')  # create a format for logging so we know the format the log should be printed
    file_handler = logging.FileHandler('logfile.txt')  # create a file handler object so that we know where to log
    file_handler.setFormatter(log_format)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
