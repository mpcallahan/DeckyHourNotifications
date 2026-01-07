import decky
import asyncio
from datetime import datetime, timedelta

class Plugin:
    hourly_task: asyncio.Task | None = None

    async def hourly_notifier(self):
        while True:
            now = datetime.now()
            next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            await asyncio.sleep((next_hour - now).total_seconds())
            await decky.emit("hour_notification", f"{next_hour.strftime('%-I')}:00")

    def start_notifier(self):
        if self.hourly_task is None or self.hourly_task.done():
            self.hourly_task = asyncio.create_task(self.hourly_notifier())

    def stop_notifier(self):
        if self.hourly_task and not self.hourly_task.done():
            self.hourly_task.cancel()
        self.hourly_task = None

    async def _main(self):
        self.loop = asyncio.get_event_loop()
        self.start_notifier()
        decky.add_event_listener("deck_suspend", lambda: asyncio.create_task(self.stop_notifier()))
        decky.add_event_listener("deck_resume", lambda: asyncio.create_task(self.start_notifier()))

    async def _unload(self):
        self.stop_notifier()

    async def _uninstall(self):
        pass

    async def _migration(self):
        pass
