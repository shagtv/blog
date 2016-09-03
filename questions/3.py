#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import asyncio
from aiohttp import web


# @asyncio.coroutine
def hello(request):
    return web.Response(body=b'Hello, world!')


app = web.Application()
app.router.add_route('GET', '/', hello)
web.run_app(app)
