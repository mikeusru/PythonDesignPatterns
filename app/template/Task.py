from app.template.AuditTrail import AuditTrail


class Task:
    def __init__(self):
        self.audit_trail = AuditTrail()

    def execute(self):
        self.audit_trail.record()
        self._do_execute()

    def _do_execute(self):
        raise NotImplementedError
