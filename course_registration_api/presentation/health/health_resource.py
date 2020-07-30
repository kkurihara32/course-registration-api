class HealthResource(object):
    def __init__(self, status=None):
        if status is None:
            self._status = "up"
        else:
            self._status = status

    def to_dict(self):
        return {"status": self.status}

    @property
    def status(self):
        return self._status
