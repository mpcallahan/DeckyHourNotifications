import { definePlugin, addEventListener, removeEventListener, toaster } from "@decky/api";
import { FaClock } from "react-icons/fa";

export default definePlugin(() => {
  const listener = addEventListener<[message: string]>(
    "hour_notification",
    (message) => {
      toaster.toast({
        title: message,
        body: ""
      });
    }
  );

  return {
    name: "Hourly Notification",
    icon: <FaClock />,
    onDismount() {
      removeEventListener("hour_notification", listener);
    },
  };
});
