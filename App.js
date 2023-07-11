import { StyleSheet, View } from "react-native";
import { Text } from "@rneui/base";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Home from "./screens/Home";
import Info from "./screens/Info";
import Analytics from "./screens/Analytics";
import {
  ThemeProvider,
  useTheme,
} from "/Users/sathvikm/Documents/nflRandomTeamGen/DarkTheme/ThemeProvider.js";

const Stack = createNativeStackNavigator();

//Every screen will follow these styles for their headers
const globalScreenOptions = {
  headerStyle: { backgroundColor: "#1c5cff" },
  headerTitleStyle: { color: "white" },
  headerTintColor: "white",
};

//Titles in functions
function HeaderTitle({ navigation }) {
  return (
    <Text
      style={{ fontSize: 23, color: "white", fontWeight: 500, marginLeft: -10 }}
    >
      NFL Random Team Generator
    </Text>
  );
}

function InfoTitle({ navigation }) {
  return (
    <Text style={{ fontSize: 23, color: "white", fontWeight: 500 }}>
      About the App
    </Text>
  );
}

function AnalyticsTitle({ navigation }) {
  return (
    <Text style={{ fontSize: 23, color: "white", fontWeight: 500 }}>
      Team Analytics
    </Text>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <NavigationContainer>
        <Stack.Navigator screenOptions={globalScreenOptions}>
          <Stack.Screen
            name="Home"
            component={Home}
            options={({ navigation }) => {
              return {
                headerTitle: () => <HeaderTitle navigation={navigation} />,
              };
            }}
          />
          <Stack.Screen
            name="Info"
            component={Info}
            options={({ navigation }) => {
              return {
                headerTitle: () => <InfoTitle navigation={navigation} />,
              };
            }}
          />
          <Stack.Screen
            name="Analytics"
            component={Analytics}
            options={({ navigation }) => {
              return {
                headerTitle: () => <AnalyticsTitle navigation={navigation} />,
              };
            }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </ThemeProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
