import os
import logging
import json

class JsonFormatter(logging.Formatter):
    """ Log Formatter for JSON output
    """
    def format(self, record):
        # Create a log record in JSON format
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
        }
        # Include exception info if present
        if record.exc_info:
            log_record['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_record)

# Set up logging
logger = logging.getLogger("jsonLogger")

# Set Custom log formatter
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
