# echo

A simple example of echo server and client in Python.

## Usage

Use the following command to run the server:

```bash
python server.py
```

- The server listens on port 8888 (so connect to it with `localhost:8888`).
- The server will only accept one client at a time. Creating more clients will cause some interesting conflicts and blocking.
- The server will echo back whatever the client sends it.

Use the following command to run the client:

```bash
python client.py
```

And write messages to the server. You should see the server echo back your messages. Open additional clients to see how the server handles multiple clients (badly).

There is also a [server_async.py](server_async.py) that handles multiple clients using the `asyncio` library. It is a bit more complicated, but it is also more robust. It can also handle a very simple HTTP GET request and will return an actual HTTP response.

Run it with:

```bash
python server_async.py
```

And connect to it either from one of the clients or with a browser at this address: [http://localhost:8888/](http://localhost:8888/).
