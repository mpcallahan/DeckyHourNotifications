import asyncio
import time
import decky

class Plugin:
    task = None

    def seconds_until_next_hour(self):
        now = time.time()
        return 3600 - (int(now) % 3600)

    async def notifier(self):
        while True:
            await asyncio.sleep(self.seconds_until_next_hour())
            hour = time.localtime().tm_hour % 12 or 12
            await decky.emit("hour_notification", str(hour))

    def stop_notifier(self):
        if self.task:
            self.task.cancel()
            self.task = None

    def start_notifier(self):
        self.stop_notifier()
        self.task = asyncio.create_task(self.notifier())

    async def restart_notifier(self):
        self.start_notifier()

    async def _main(self):
        self.start_notifier()

    async def _unload(self):
        self.stop_notifier()
