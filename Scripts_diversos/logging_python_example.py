import logging

#logging.warning('o bagui tá sinistro. Cuidado!')
logging.basicConfig(filename='demolog.log',format='%(asctime)s %(message)s',level=logging.DEBUG)

logging.getLogger().setLevel(logging.DEBUG)
logging.info('Sistema rodando normalmente.')
