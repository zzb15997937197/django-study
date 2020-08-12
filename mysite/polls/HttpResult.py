import json
import time
import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d: %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


class Result:
    code = 200
    message = 'OK'

    def __init__(self, code=200, message='OK', data=None, data_count=None):
        self.code = code
        self.message = message
        self.clock = time.time()

        if data is not None:
            self.data = data

        if data_count is not None:
            self.data_count = data_count

    def to_json_string(self):
        self.elapsed = int((time.time() - self.clock) * 1000)
        self.__dict__.pop('clock')
        out = json.dumps(self.__dict__, sort_keys=False, indent=4, ensure_ascii=False)
        print(out)
        return out

    def db_error(self, message):
        self.code = -4
        self.message = message

    def file_error(self, message):
        self.code = -3
        self.message = message

    def error(self, exception):
        self.code = -9
        self.message = str(exception)
        log.error('[HTTP RESULT] error: %s' % self.message)

    def status(self):
        if self.code == 0:
            return 200
        else:
            return 500
