#!/usr/bin/env python3
"""Module to listen for link events"""

import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey

load_dotenv()

solana_node = os.getenv('SOLANA_NODE', 'http://api.devnet.solana.com')
pk = PublicKey(
    os.getenv('SOLANA_ADDRESS')
)

class LinkNode:
    """Class for link node"""
    def __init__(self, poll_interval):
        self.poll_interval = poll_interval
        self.last_signature = None
        self.last_block_time = None
    async def process(self):
        """Process event"""
        async with AsyncClient(solana_node) as client:
            if self.last_signature is None:
                siglist = await client.get_signatures_for_address(pk)
            else:
                siglist = await client.get_signatures_for_address(
                    pk, until=self.last_signature
                )
            for sig in siglist.value:
                tx = await client.get_transaction(sig.signature)
                print(tx.value)
                if self.last_block_time is None or \
                   sig.block_time > self.last_block_time:
                    self.last_signature = sig.signature
                    self.last_block_time = sig.block_time

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

