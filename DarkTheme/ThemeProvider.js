import React, { createContext, useState, useEffect, useContext } from "react";
import { lightTheme, darkTheme } from "/Users/sathvikm/Documents/nflRandomTeamGen/DarkTheme/colors.js";
import { useColorScheme } from "react-native";

export const ThemeContext = createContext({
  dark: false,
  colors: lightTheme,
  setScheme: () => {},
});

export const ThemeProvider = (props) => {
  const colorScheme = useColorScheme();
  const [isDark, setIsDark] = useState(colorScheme == "dark");
  useEffect(() => {
    setIsDark(colorScheme == "dark");
  }, [colorScheme]);
  const defaultTheme = {
    dark: isDark,
    colors: isDark ? darkTheme : lightTheme,
    setScheme: (scheme) => setIsDark(scheme == "dark"),
  };

  return (
    <ThemeContext.Provider value={defaultTheme}>
      {props.children}
    </ThemeContext.Provider>
  );
};

//creating custom hook
export const useTheme = () => useContext(ThemeContext);
