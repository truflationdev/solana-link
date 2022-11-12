#!/usr/bin/env python3
"""Module to listen for link events"""

import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey

load_dotenv()

class LinkNode:
    """Class for link node"""
    def __init__(self, node, account, poll_interval):
        self.poll_interval = poll_interval
        self.last_signature = None
        self.last_block_time = None
        self.account = PublicKey(account)
        self.node = node
        self.client = AsyncClient(self.node)
    async def process(self):
        """Process event"""
        if self.last_signature is None:
            siglist = await self.client.get_signatures_for_address(
                self.account
            )
        else:
            siglist = await self.client.get_signatures_for_address(
                self.account, until=self.last_signature
            )
        for sig in siglist.value:
            txn = await self.client.get_transaction(sig.signature)
            self.process_txn(txn)
            if self.last_block_time is None or \
               sig.block_time > self.last_block_time:
                self.last_signature = sig.signature
                self.last_block_time = sig.block_time
    def process_txn(self, txn):
        """Process one txn"""
        print(txn.value)
    async def event_loop(self, poll_interval: int) -> None:
        """Run event loop"""
        while True:
            await self.process()
            await asyncio.sleep(poll_interval)
    def run(self) -> None:
        """Start run"""
        self.show_init_message()
        asyncio.run(self.event_loop(self.poll_interval))
    def show_init_message(self) -> None:
        """Show startup message"""
        print(f'solana node = {self.node}')
        print(f'solana address = {self.account}')

if __name__ == "__main__":
    ln = LinkNode(
        os.getenv('SOLANA_NODE', 'http://api.devnet.solana.com'),
        os.getenv('SOLANA_ADDRESS'),
        1
    )
    ln.run()
