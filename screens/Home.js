import { StyleSheet, View, TouchableOpacity, Image } from "react-native";
import SwitchWithIcons from "react-native-switch-with-icons";
import { Text } from "@rneui/base";
import React, { useLayoutEffect, useState } from "react";
import { useTheme } from "../DarkTheme/ThemeProvider.js";
import { AntDesign, Ionicons, Entypo } from "@expo/vector-icons";

const Home = ({ navigation }) => {
  const { dark, colors, setScheme } = useTheme();

  const toggleTheme = () => {
    dark ? setScheme("light") : setScheme("dark");
  };

  const lightModeIcon = (
    <Image
      source={{ uri: "Images/light-mode.png" }}
      style={{ width: 20, height: 100 }}
    />
  );
  const darkModeIcon = (
    <Image
      source={{ uri: "Images/night-mode.png" }}
      style={{ width: 100, height: 100 }}
    />
  );

  navigation.setOptions({
    headerLeft: () => (
      <View
        style={{
          flexDirection: "row",
          justifyContent: "flex-end",
          marginRight: 22,
          marginLeft: -8,
        }}
      >
        <TouchableOpacity
          onPress={toggleTheme}
          style={{
            borderWidth: 2,
            borderColor: "white",
            borderRadius: 8,
            padding: 5,
            paddingHorizontal: 6
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
    <View
      style={{
        alignItems: "center",
        height: "100%",
        backgroundColor: colors.primary,
      }}
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
          marginTop: 70,
          width: "50%",
          height: "5.5%",
          borderRadius: 10,
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Text style={{ color: "white", fontSize: 20, fontWeight: "bold" }}>
          Generate
        </Text>
      </TouchableOpacity>
    </View>
  );
};

export default Home;

const styles = StyleSheet.create({});
