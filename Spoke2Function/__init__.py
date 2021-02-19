import logging
import datetime
# import json

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    timestamp = datetime.datetime.now()
    
    logging.info('Python ServiceBus queue trigger processed\n\ttime:\t%s\n\tmid:\t%s\n\tmsg:\t%s', 
        timestamp, 
        msg.message_id,
        msg.get_body().decode('utf-8')
    )