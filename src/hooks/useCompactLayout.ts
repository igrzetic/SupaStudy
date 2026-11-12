import { useSyncExternalStore } from "react";
import { useWindowDimensions } from "react-native";

function subscribe() {
  return () => {};
}

function getClientSnapshot() {
  return true;
}

function getServerSnapshot() {
  return false;
}

export function useCompactLayout() {
  const { width } = useWindowDimensions();

  const isHydrated = useSyncExternalStore(
    subscribe,
    getClientSnapshot,
    getServerSnapshot,
  );

  return !isHydrated || width < 1000;
}
