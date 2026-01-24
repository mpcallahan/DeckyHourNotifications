import asyncio
from datetime import datetime, timedelta
import decky

class Plugin:
    task = None

    async def notifier(self):
        while True:
            now = datetime.now()
            next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            await asyncio.sleep((next_hour - now).total_seconds())
            await decky.emit("hour_notification", f"{next_hour.strftime('%-I')}:00")

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
