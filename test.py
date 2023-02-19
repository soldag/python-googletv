import asyncio
from googletv.device import AdbKey, GoogleTv


async def main():
    key = AdbKey("key")
    device = GoogleTv(key, "10.0.0.66")
    await device.connect()
    while True:
        await device.update()
        print(device.state)
        # await asyncio.sleep(1)


asyncio.run(main())
