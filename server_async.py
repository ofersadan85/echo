import asyncio

HOST = "0.0.0.0"
PORT = 8888

http_response = """HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 13

Hello, World!"""


async def handle_echo(reader, writer):
    data = await reader.read(4096)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print(f"Client {addr} sent: {message}")
    if message.startswith("GET /"):
        response = http_response.encode()
    else:
        response = message.encode()
    print(f"Sending response to {addr}: {response}")
    writer.write(response)
    await writer.drain()
    print(f"Closing the connection with {addr}")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Listening on {addr}")
    async with server:
        await server.serve_forever()


asyncio.run(main())
