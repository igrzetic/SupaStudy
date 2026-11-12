import { StyleSheet } from "react-native";

import { theme } from "@/styles/theme";

export const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    alignItems: "center",
    gap: theme.spacing.md,

    margin: theme.spacing.lg,
    padding: theme.spacing.md,

    borderWidth: 1,
    borderColor: "rgba(255, 255, 255, 0.65)",
    borderRadius: 20,

    backgroundColor: "rgba(255, 255, 255, 0.12)",
    overflow: "hidden",
  },

  bottomContainer: {
    marginTop: 0,
    marginHorizontal: theme.spacing.md,
    marginBottom: theme.spacing.md,
    padding: theme.spacing.sm,
  },

  side: {
    flex: 1,
    minWidth: 0,
  },

  brand: {
    flexDirection: "row",
    alignItems: "center",
    gap: theme.spacing.sm,
  },

  mobileLogo: {
    flexDirection: "row",
    alignItems: "center",
    gap: theme.spacing.sm,
    margin: theme.spacing.lg,
  },

  logo: {
    width: 44,
    height: 44,
    borderRadius: 12,
    borderWidth: 1.2,
    borderColor: theme.colors.navigationActiveBorder,
    backgroundColor: theme.colors.logoBackground,
    justifyContent: "center",
    alignItems: "center",
  },

  logoText: {
    color: "#FFFFFF",
    fontSize: 24,
    fontWeight: "700",
  },

  tagline: {
    color: theme.colors.text,
    fontSize: 16,
  },

  links: {
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    flexWrap: "wrap",
    gap: theme.spacing.sm,
  },

  link: {
    width: 84,
    height: 68,
    alignItems: "center",
    gap: 4,
    paddingVertical: theme.spacing.sm,
    paddingHorizontal: theme.spacing.sm,
    justifyContent: "center",
    borderRadius: 12,
    borderWidth: 1.2,
    borderColor: "transparent",
    overflow: "hidden",
  },

  linkText: {
    color: theme.colors.primary,
    fontSize: 14,
    fontWeight: "500",
  },

  pressedLink: {
    backgroundColor: theme.colors.navigationActiveBackground,
    borderColor: theme.colors.navigationActiveBorder,
  },
});
