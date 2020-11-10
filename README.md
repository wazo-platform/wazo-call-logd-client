wazo-call-logd-client
===================

A python library to connect to wazo-call-logd. HTTPS is used by default. Certificates are verified by default. To disable certificate verification, use the verify_certificate argument when instantiating the client.

Usage:

```python
from wazo_call_logd_client import Client

c = Client('localhost', token='the-one-ring', verify_certificate=False)

cdr = c.cdr.list(limit=10, offset=20)
cdr = c.cdr.list_for_user(user_uuid='my-user')
cdr = c.cdr.list_from_user()  # with user token only

cdr = c.cdr.list_csv(limit=10, offset=20)
cdr = c.cdr.list_for_user_csv(user_uuid='my-user')
cdr = c.cdr.list_from_user_csv()  # with user token only

cdr = c.cdr.get_by_id(1234)
cdr = c.cdr.get_by_id_csv(1234)

status = c.status.get()

queue_statistics = c.queue_statistics.get_by_id(
    queue_id=123, from_='2020-03', until='2020-04', qos_threshold='10',
    day_start_time='08:00', day_end_time='17:00', interval='day'
)
all_queues_statistics = c.queue_statistics.list(
    from_='2020-03', until='2020-04', qos_threshold='10', day_start_time='08:00', day_end_time='17:00'
)

agent_statistics = c.agent_statistics.get_by_id(
    agent_id=123, from_='2020-03', until='2020-04',
    day_start_time='08:00', day_end_time='17:00', interval='day'
)
all_agent_statistics = c.agent_statistics.list(
    from_='2020-03', until='2020-04', day_start_time='08:00', day_end_time='17:00'
)
```

## Tests

Running unit tests
------------------

```
pip install tox
tox --recreate -e py27
```

## How to implement a new command

Someone trying to implement a new command to the client would have to implement a new class, sub-classing the RESTCommand (available in wazo-lib-rest-client). The new class must be in the setup.py in the entry points under `wazo_call_logd_client.commands`. The name of the entry point is used as the handle on the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'wazo_call_logd_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```
