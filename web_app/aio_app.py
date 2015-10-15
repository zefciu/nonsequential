import asyncio
from aiohttp import web
import aiopg

class App():
    async def hello(self, request):
        return web.Response(body='hello'.encode('utf-8'))
    
    async def init(self, loop):
        app = web.Application()
        app.router.add_route('GET', '/', self.hello)
        srv = await loop.create_server(app.make_handler(), '0.0.0.0', 8000)
        print('serving on', srv.sockets[0].getsockname())
        return srv

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = App()
    loop.run_until_complete(app.init(loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
