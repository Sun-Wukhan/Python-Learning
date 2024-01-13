import asyncio
import asyncpg
import aiohttp
import ssl  # Import the ssl module

async def fetch_status(session, url):
    async with session.get(url) as response:
        
        if response.status == 200:
            print("Everything is fine and Dandy")
        else: 
            print("Something is wrong in the force")
            
        return response.status
    
async def record_status(db_conn, url, status_code):
    await db_conn.execute('INSERT INTO website_status (url, status_code) VALUES ($1, $2)',
        url, status_code
    )

async def monitor_website(url, db_conn):
    # Create an SSLContext object with no certificate verification
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Use the SSLContext in the TCPConnector
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        while True:
            status_code = await fetch_status(session, url)
            await record_status(db_conn, url, status_code)
            await asyncio.sleep(120)

async def main(): 
    db_conn = await asyncpg.connect('')
    url = ""
    await monitor_website(url, db_conn)

if __name__ == '__main__':
    asyncio.run(main())