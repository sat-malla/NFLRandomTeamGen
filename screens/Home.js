import {
  StyleSheet,
  View,
  TouchableOpacity,
  Image,
  Alert,
  FlatList,
  Button,
  ScrollView,
} from "react-native";
import SwitchWithIcons from "react-native-switch-with-icons";
import { Text } from "@rneui/base";
import React, { useLayoutEffect, useState, useEffect, useRef } from "react";
import { useTheme } from "../DarkTheme/ThemeProvider.js";
import { AntDesign, Ionicons, Entypo } from "@expo/vector-icons";

const Home = ({ navigation }) => {
  const { dark, colors, setScheme } = useTheme();
  const [data, setData] = useState([]);
  const [schedule, setSchedule] = useState([]);
  const [buttonPressed, isButtonPressed] = useState(false);

  const toggleTheme = () => {
    dark ? setScheme("light") : setScheme("dark");
  };

  const getMessage = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/");
      const json = await response.json();
      setData(json.teamItems);
      setSchedule(json.schedule);
      isButtonPressed(true);
    } catch (error) {
      Alert.alert(error);
    }
  };

  useEffect(() => {
    getMessage();
  }, []);

  navigation.setOptions({
    headerLeft: () => (
      <View
        style={{
          flexDirection: "row",
          justifyContent: "flex-end",
          marginRight: 22,
          marginLeft: -8,
          marginBottom: 2,
        }}
      >
        <TouchableOpacity
          onPress={toggleTheme}
          style={{
            borderWidth: 2,
            borderColor: "white",
            borderRadius: 8,
            padding: 5,
            paddingHorizontal: 6,
          }}
        >
          {dark ? (
            <Entypo name="light-up" size={20} color={"white"} />
          ) : (
            <Ionicons name="moon" size={20} color={"white"} />
          )}
        </TouchableOpacity>
      </View>
    ),
    headerRight: () => (
      <View
        style={{
          flexDirection: "row",
          justifyContent: "flex-end",
          width: 80,
          marginRight: 5,
        }}
      >
        <TouchableOpacity
          onPress={() => navigation.navigate("Info")}
          activeOpacity={0.5}
        >
          <AntDesign name="infocirlceo" size={25} color="white" />
        </TouchableOpacity>
      </View>
    ),
  });

  return (
    <ScrollView
      style={{
        height: "100%",
        backgroundColor: colors.primary,
      }}
      contentContainerStyle={{
        alignItems: "center",
      }}
      scrollIndicatorInsets={{ right: 1 }}
    >
      <Text
        style={{
          fontSize: 29,
          fontWeight: "bold",
          marginTop: 40,
          color: colors.text,
        }}
      >
        Welcome to the Best
      </Text>
      <Text
        style={{
          fontSize: 30,
          fontWeight: "bold",
          marginTop: 10,
          color: colors.text,
        }}
      >
        NFL Random Team Generator
      </Text>
      <Text
        style={{
          fontSize: 20,
          fontWeight: "400",
          marginTop: 50,
          color: colors.text,
        }}
      >
        Click the 'Generate' button to get started!
      </Text>
      <TouchableOpacity
        style={{
          backgroundColor: "#1c5cff",
          padding: 10,
          marginTop: 40,
          marginBottom: 10,
          width: "50%",
          height: 50, //buttonPressed ? "4%" : "14%",
          borderRadius: 10,
          alignItems: "center",
          justifyContent: "center",
        }}
        onPress={getMessage}
      >
        <Text style={{ color: "white", fontSize: 20, fontWeight: "bold" }}>
          Generate
        </Text>
      </TouchableOpacity>
      <Button
        disabled={!buttonPressed}
        title="Clear"
        accessibilityLabel="Clear Generated Team"
        color="red"
        onPress={() => isButtonPressed(false)}
      />
      {buttonPressed ? (
        <View style={{ marginTop: 10, padding: 15 }} >
          <FlatList
            data={data}
            keyExtractor={({ id }) => id}
            scrollEnabled={false}
            contentContainerStyle={{ alignItems: "center" }}
            ItemSeparatorComponent={() => <View style={{ height: 5 }} />}
            renderItem={({ item }) => (
              <Text style={{ fontSize: 15, color: colors.text }}>
                {item.item}
              </Text>
            )}
          />
          <FlatList
            data={schedule}
            keyExtractor={({ id }) => id}
            scrollEnabled={false}
            style={{ marginTop: 10 }}
            contentContainerStyle={{ alignItems: "center" }}
            ItemSeparatorComponent={() => <View style={{ height: 5 }} />}
            renderItem={({ item }) => (
              <Text style={{ fontSize: 10, color: colors.text }}>
                {item.item}
              </Text>
            )}
          />
        </View>
      ) : (
        <Text> </Text>
      )}
      <View style={{ height: 90 }} />
    </ScrollView>
  );
};

export default Home;

const styles = StyleSheet.create({});
