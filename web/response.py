from flask import g, jsonify


class JsonResponse:
    def __init__(self, status_code=200, code="SUCCESS", msg="OK", data=None):
        self.status_code = status_code
        self.code = code
        self.request_id = getattr(g, "X-REQUEST-ID", None)
        self.msg = msg
        self.data = data

    def build(self):
        return jsonify(dict(request_id=self.request_id, code=self.code, msg=self.msg, data=self.data)), self.status_code
