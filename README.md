xivo-call-logs-client
===================

A python library to connect to xivo-call-logd. HTTPS is used by default. Certificates are verified by default. To disable certificate verification, use the verify_certificate argument when instantiating the client.

Usage:

```python
from xivo_call_logs_client import Client

c = Client('localhost', token='the-one-ring', verify_certificate=False)

```

## Tests

Running unit tests
------------------

```
pip install tox
tox --recreate -e py27
```

## How to implement a new command

Someone trying to implement a new command to the client would have to implement a new class, sub-classing the RESTCommand (available in xivo-lib-rest-client). The new class must be in the setup.py in the entry points under call_logs_client.commands. The name of the entry point is used as the handle on the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'call_logs_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```
