from xivo_call_logs_client import Client

c = Client('dev', token='the-one-ring', verify_certificate=False)
c.pwet()
