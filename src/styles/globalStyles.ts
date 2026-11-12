import { StyleSheet } from "react-native";
import { theme } from "./theme";

export const globalStyles = StyleSheet.create({
  screen: {
    flex: 1,
    backgroundColor: theme.colors.background,
  },

  scrollArea: {
    flex: 1,
    minHeight: 0,
  },

  content: {
    padding: theme.spacing.lg,
  },

  bodyText: {
    color: theme.colors.text,
    fontSize: theme.typography.bodySize,
    lineHeight: theme.typography.bodyLineHeight,
  },

  heading: {
    color: theme.colors.text,
    fontSize: theme.typography.headingSize,
    lineHeight: theme.typography.headingLineHeight,
  },
});
