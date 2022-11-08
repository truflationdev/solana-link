#!/usr/bin/env python3
"""Module to listen for link events"""

import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient

load_dotenv()

solana_node = os.getenv('SOLANA_NODE', 'http://api.devnet.solana.com')

class LinkNode:
    def __init__(self, poll_interval):
        self.poll_interval = poll_interval
    async def process(self):
        """Process event"""
        async with AsyncClient(solana_node) as client:
            res = await client.is_connected()
            print(res)  # True
    async def event_loop(self, poll_interval):
        """Run event loop"""
        while True:
            await self.process()
            await asyncio.sleep(poll_interval)
    def run(self):
        """Start run"""
        asyncio.run(self.event_loop(self.poll_interval))

if __name__ == "__main__":
    ln = LinkNode(1)
    ln.run()

