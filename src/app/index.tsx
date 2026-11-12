import { useState } from "react";
import { ScrollView, Text, View } from "react-native";

import Navbar from "@/components/Navbar/Navbar";
import { useCompactLayout } from "@/hooks/useCompactLayout";
import { globalStyles } from "@/styles/globalStyles";

export default function HomeScreen() {
  const isCompact = useCompactLayout();
  const [activeItem, setActiveItem] = useState("home");

  return (
    <View style={globalStyles.screen}>
      <Navbar
        mode={isCompact ? "logo" : "desktop"}
        activeItem={activeItem}
        onSelect={setActiveItem}
      />

      <ScrollView
        style={globalStyles.scrollArea}
        contentContainerStyle={globalStyles.content}
      >
        <Text style={globalStyles.heading}>SupaStudy</Text>
        <Text style={globalStyles.bodyText}>Your study space.</Text>
      </ScrollView>

      {isCompact && (
        <Navbar
          mode="navigation"
          activeItem={activeItem}
          onSelect={setActiveItem}
        />
      )}
    </View>
  );
}
