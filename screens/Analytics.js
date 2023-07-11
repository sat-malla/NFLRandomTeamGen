import { StyleSheet, Text, View, ScrollView, FlatList } from "react-native";
import React, { useState, useEffect } from "react";
import { useTheme } from "../DarkTheme/ThemeProvider.js";

const Analytics = () => {
  const { colors } = useTheme();
  const [record, setRecord] = useState([]);

  const getAnalytics = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/");
      const json = await response.json();
      setRecord(json.record);
    } catch (error) {
      Alert.alert(error);
    }
  };

  useEffect(() => {
    getAnalytics();
  }, []);

  const titles = [
    {
      id: "1",
      title: "Team Rating",
      text: Store.Rating(),
    },
    {
      id: "2",
      title: "Playoff Chances",
    },
  ];

  const titles1 = [
    {
      id: "1",
      title: "Team Record",
      component: (
        <FlatList
          data={record}
          scrollEnabled={false}
          contentContainerStyle={{ justifyContent: "center" }}
          keyExtractor={(item) => item.id}
          ItemSeparatorComponent={() => <View style={{ height: 2 }} />}
          renderItem={({ item }) => (
            <Text style={{ fontSize: 13, color: colors.text }}>
              {item.item}
            </Text>
          )}
        />
      ),
    },
    {
      id: "2",
      title: "Team Accolades",
    },
  ];

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
          fontSize: 30,
          fontWeight: "bold",
          marginTop: 40,
          color: colors.text,
        }}
      >
        Team Analytics
      </Text>
      <View style={{ flex: 1, flexDirection: "row", marginTop: 20 }}>
        <FlatList
          data={titles}
          scrollEnabled={false}
          contentContainerStyle={{ justifyContent: "center" }}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <View
              style={{
                backgroundColor: "white",
                borderColor: "blue",
                borderTopWidth: 30,
                borderWidth: 2,
                height: 110,
                width: 150,
                padding: 15,
                alignItems: "center",
                marginLeft: 40,
                marginTop: 20,
                borderRadius: 16,
              }}
            >
              <Text
                style={{
                  marginTop: -38,
                  color: "white",
                  fontWeight: "bold",
                }}
              >
                {item.title}
              </Text>
              <Text
                style={{
                  marginTop: 19,
                  marginRight: 3,
                  fontSize: 30,
                  fontWeight: "400",
                  color: colors.text,
                }}
              >
                {item.text}
              </Text>
            </View>
          )}
        />
        <FlatList
          data={titles1}
          scrollEnabled={false}
          contentContainerStyle={{ justifyContent: "center" }}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <View
              style={{
                backgroundColor: "white",
                borderColor: "blue",
                borderTopWidth: 30,
                borderWidth: 2,
                height: 110,
                width: 150,
                padding: 15,
                alignItems: "center",
                marginLeft: 10,
                marginTop: 20,
                borderRadius: 16,
              }}
            >
              <Text
                style={{
                  marginTop: -38,
                  marginBottom: 10,
                  color: "white",
                  fontWeight: "bold",
                }}
              >
                {item.title}
              </Text>
              {item.component}
            </View>
          )}
        />
      </View>
    </ScrollView>
  );
};

export default Analytics;

const styles = StyleSheet.create({});
