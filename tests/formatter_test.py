import unittest, logging, json
from datetime import datetime

from json_formatter.formatter import JSONFormatter


class JsonLogFormatter(unittest.TestCase):
    formatter = JSONFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    default_formatter = logging.Formatter()

    def test_produced_json_matches_the_record(self):
        test_record = logging.LogRecord(name='test',
                                        level=logging.DEBUG,
                                        pathname='test',
                                        lineno=666,
                                        msg='Log message',
                                        args={},
                                        exc_info=None)
        actual_message = json.loads(self.formatter.format(test_record))

        self.assertDictEqual(self.expected_message(test_record), actual_message)

    def expected_message(self, record):
        message = {
            '@timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'description': record.getMessage(),
            'source_file': record.pathname,
            'pid': record.process,
            'thread': record.threadName,
            'severity': record.levelname,
            'module': record.module,
            'log_type': 'application_log'
        }
        if record.exc_info:
            message['stacktrace'] = self.default_formatter.formatException(record.exc_info)
        return message


if __name__ == '__main__':
    unittest.main()
