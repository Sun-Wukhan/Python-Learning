import asyncio
import asyncpg
import aiohttp
import ssl  
from send_message import send_alert_message

async def fetch_status(session, url):
    async with session.get(url) as response:
        
        if response.status == 200:
            status_body = response.reason
            status_code = response.status
            print(f"Response Status: {status_code} Response Body: {status_body}")  
        else: 
            status_code = response.status
            status_reason = response.reason
            error_body = await response.text()
            print(f"Status: {status_code} Error Body: {error_body}")
            send_alert_message(f"Status: {status_code} Error Body: {status_reason} Additional Details: {error_body}")
            
            
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
    db_conn = await asyncpg.connect('postgresql://arc:YXJjLXBzc3dk@cnpg-rw.dse.cloud.arc.ninjaneers.net:5432/arcdb')
    url = "https://pl-acegit01.as12083.net/"
    await monitor_website(url, db_conn)

if __name__ == '__main__':
    asyncio.run(main())