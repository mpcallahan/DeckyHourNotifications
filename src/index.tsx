import { definePlugin, toaster, callable, addEventListener, removeEventListener } from "@decky/api";
import { staticClasses } from "@decky/ui";
import { findModuleExport } from "@decky/ui";
import { FaClock } from "react-icons/fa";

interface SleepManager {
  RegisterForNotifyResumeFromSuspend: (cb: () => void) => () => void;
}

const sleepManager = findModuleExport(
  (mod) => mod.RegisterForNotifyResumeFromSuspend
) as SleepManager | undefined;

const restartNotifier = callable<[], void>("restart_notifier");

export default definePlugin(() => {
  const unregisterResume =
    sleepManager?.RegisterForNotifyResumeFromSuspend(() => {
      restartNotifier();
    });

  const listener = addEventListener<[hour: string]>(
    "hour_notification",
    (hour) => {
      toaster.toast({ title: hour, body: "" });
    }
  );

  return {
    name: "Hour Notifications",
    titleView: <div className={staticClasses.Title}>Hour Notifications</div>,
    icon: <FaClock />,
    content: <div />,
    onDismount() {
      unregisterResume?.();
      removeEventListener("hour_notification", listener);
    },
  };
});
