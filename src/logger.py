import logging

# 1. Create / get a logger
logger = logging.getLogger('OpenClimateAI')
logger.setLevel(logging.DEBUG)

# 2. Create handlers (console + file for example)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


# 3. Create formatters and attach to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# 4. Add handlers to logger
logger.addHandler(ch)
