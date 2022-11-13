#!/usr/bin/env python3
"""Module to listen for link events"""
import os
from dotenv import load_dotenv
import solana_link_node

load_dotenv()
ln = solana_link_node.LinkNode(
    os.getenv('SOLANA_HOST', 'http://api.devnet.solana.com'),
    os.getenv('SOLANA_ADDRESS'),
    os.getenv('API_ADAPTER', 'http://api-adapter:8081'),
    1
)
ln.run()
