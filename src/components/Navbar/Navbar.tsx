import { theme } from "@/styles/theme";
import { BlurView } from "expo-blur";
import { SymbolView } from "expo-symbols";
import { Image, Pressable, Text, View } from "react-native";

import { styles } from "./Navbar.styles";

const navigationItems = [
  {
    id: "home",
    label: "Home",
    icon: { ios: "house", android: "home", web: "home" },
  },
  {
    id: "calendar",
    label: "Calendar",
    icon: { ios: "calendar", android: "calendar_month", web: "calendar_month" },
  },
  {
    id: "courses",
    label: "Courses",
    icon: { ios: "book", android: "menu_book", web: "menu_book" },
  },
  {
    id: "user",
    label: "User",
    icon: { ios: "person", android: "person", web: "person" },
  },
] as const;

type NavbarProps = {
  mode: "desktop" | "logo" | "navigation";
  activeItem: string;
  onSelect: (item: string) => void;
};

export default function Navbar({ mode, activeItem, onSelect }: NavbarProps) {
  if (mode === "logo") {
    return (
      <View style={styles.mobileLogo}>
        <Image
          source={require("../../../assets/logo/supastudy_logo.png")}
          style={styles.logo}
          resizeMode="contain"
          accessibilityLabel="SupaStudy logo"
        />

        <Text style={styles.tagline}>Your study space.</Text>
      </View>
    );
  }

  return (
    <BlurView
      intensity={25}
      tint="light"
      style={[
        styles.container,
        mode === "navigation" && styles.bottomContainer,
      ]}
    >
      {mode !== "navigation" && (
        <View style={[styles.brand, mode === "desktop" && styles.side]}>
          <Image
            source={require("../../../assets/logo/supastudy_logo.png")}
            style={styles.logo}
            resizeMode="contain"
            accessibilityLabel="SupaStudy logo"
          />

          <Text style={styles.tagline}>Your study space.</Text>
        </View>
      )}

      <View style={[styles.links, styles.side]}>
        {navigationItems.map((item) => (
          <Pressable
            key={item.id}
            accessibilityRole="button"
            accessibilityState={{ selected: activeItem === item.id }}
            onPress={() => onSelect(item.id)}
            style={({ pressed }) => [
              styles.link,
              (pressed || activeItem === item.id) && styles.pressedLink,
            ]}
          >
            <SymbolView
              name={item.icon}
              size={22}
              tintColor={theme.colors.primary}
              accessible={false}
            />
            <Text style={styles.linkText}>{item.label}</Text>
          </Pressable>
        ))}
      </View>

      {mode === "desktop" && <View style={styles.side} />}
    </BlurView>
  );
}
