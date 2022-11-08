import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient

load_dotenv()

solana_node = os.getenv('SOLANA_NODE', 'http://api.devnet.solana.com')

async def main():
    async with AsyncClient(solana_node) as client:
        res = await client.is_connected()
    print(res)  # True

if __name__ == "__main__":
    asyncio.run(main())
