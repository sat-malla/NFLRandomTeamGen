import { StyleSheet, Text, View } from "react-native";
import React, { useLayoutEffect } from "react";

const Info = ({ navigation }) => {
  useLayoutEffect(() => {
    navigation.setOptions({
      headerBackTitleStyle: { color: "white" }
    });
  }, [navigation]);

  return (
    <View
      style={{
        alignItems: "center",
        height: "100%",
        backgroundColor: "white",
      }}
    >
      <Text style={{ fontSize: 29, fontWeight: "bold", marginTop: 30 }}>
        What is this App?
      </Text>
      <Text style={{ fontSize: 29, fontWeight: "bold", marginTop: 40 }}>
        About the Developer
      </Text>
    </View>
  );
};

export default Info;

const styles = StyleSheet.create({});
