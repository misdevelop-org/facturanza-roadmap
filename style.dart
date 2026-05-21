/*
import 'package:flutter/material.dart';

// Brand colors
Color primaryColor = const Color(0xFF5EB0C7);
Color lightBlue = const Color(0xFFC5D0F9);
Color blue = const Color(0xFF005973);
Color green = const Color(0xFF00A791);
Color lightGreen = const Color(0xFF63D389);
Color orange = const Color(0xFFD3853C);
Color brown = const Color(0xFFB05704);

// State colors

Color successColor = const Color(0xFF63D389);
Color disableColor = const Color(0xFFD0D0D0);
Color errorColor = const Color(0xFFB7260C);

// Dark colors

Color darkBackground = const Color(0xFF414141);
Color darkText = const Color(0xFFE8E8E8);
Color darkSection = const Color(0xFF6F6F6F);

// Light colors

Color lightBackground = const Color(0xFFF5F5F5);
Color lightText = const Color(0xFF6F6F6F);
Color lightSection = const Color(0xFFFFFFFF);

MaterialColor primarySwatch = const MaterialColor(0xFF5EB0C7, <int, Color>{
  50: Color(0xFFF8F0FA),
  100: Color(0xFFC3E1EA),
  200: Color(0xFFA4D2DF),
  300: Color(0xFF86C4D5),
  400: Color(0xFF63B9CF),
  500: Color(0xFF4AA6BF),
  600: Color(0xFF3A8FA6),
  700: Color(0xFF307588),
  800: Color(0xFF255B6A),
  900: Color(0xFF1B414B),
});

BoxDecoration enterpriseDecoration(Color color) => BoxDecoration(
  gradient: LinearGradient(
    colors: [color.withValues(alpha: 0.3), color.withValues(alpha: 0.3), Colors.transparent],
    begin: Alignment.bottomCenter,
    end: Alignment.topCenter,
  ),
);

// Light Theme Data

ThemeData lightTheme = ThemeData(
  dropdownMenuTheme: DropdownMenuThemeData(
    inputDecorationTheme: InputDecorationTheme(
      iconColor: disableColor,
      suffixIconColor: disableColor,
      border: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: Colors.white, width: 1),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: Colors.white, width: 1),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: Colors.white, width: 1),
      ),
      filled: true,
      fillColor: Colors.white,
    ),
    menuStyle: MenuStyle(
      backgroundColor: WidgetStatePropertyAll(Colors.white),
      maximumSize: WidgetStatePropertyAll(Size(double.infinity, 300)),
    ),
    textStyle: TextStyle(color: lightText),
  ),
  colorScheme: ColorScheme.light(primary: primarySwatch.shade800, secondary: primarySwatch.shade600),
  appBarTheme: AppBarTheme(
    backgroundColor: lightBackground,
    surfaceTintColor: lightBackground,
    centerTitle: true,
    iconTheme: IconThemeData(color: lightText),
    titleTextStyle: TextStyle(color: lightText, fontSize: 20),
  ),
  drawerTheme: DrawerThemeData(elevation: 0, backgroundColor: lightBackground),
  fontFamily: 'Inter',
  textTheme: TextTheme(
    bodyLarge: TextStyle(color: lightText),
    bodyMedium: TextStyle(color: lightText),
    bodySmall: TextStyle(color: lightText),
    headlineLarge: TextStyle(color: lightText),
    headlineMedium: TextStyle(color: lightText),
    headlineSmall: TextStyle(color: lightText),
    labelLarge: TextStyle(color: lightText),
    labelMedium: TextStyle(color: lightText),
    labelSmall: TextStyle(color: lightText),
    displayLarge: TextStyle(color: blue),
    displayMedium: TextStyle(color: blue),
    displaySmall: TextStyle(color: blue),
  ),
  iconTheme: IconThemeData(color: lightText),
  popupMenuTheme: PopupMenuThemeData(
    color: lightSection,
    textStyle: TextStyle(color: lightText),
  ),
  cardColor: lightSection,
  buttonTheme: ButtonThemeData(
    colorScheme: ColorScheme(
      primary: lightGreen,
      secondary: primarySwatch.shade200,
      surface: lightSection,
      error: errorColor,
      onPrimary: lightText,
      onSecondary: lightText,
      onSurface: lightText,
      onError: lightText,
      brightness: Brightness.light,
    ),
  ),
  scaffoldBackgroundColor: lightBackground,
  primarySwatch: primarySwatch,
  brightness: Brightness.light,
  visualDensity: VisualDensity.standard,
  useMaterial3: true,
  canvasColor: primarySwatch.shade700,
  elevatedButtonTheme: ElevatedButtonThemeData(style: buttonTheme),
  filledButtonTheme: FilledButtonThemeData(
    style: buttonTheme.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  textButtonTheme: TextButtonThemeData(
    style: buttonTheme.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  outlinedButtonTheme: OutlinedButtonThemeData(
    style: buttonTheme.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  inputDecorationTheme: InputDecorationTheme(
    filled: true,
    fillColor: Colors.white,
    focusColor: Colors.white,
    hoverColor: Colors.white,
    prefixIconColor: lightBlue,
    labelStyle: TextStyle(color: lightText),
    hintStyle: TextStyle(color: lightText),
    floatingLabelStyle: TextStyle(color: blue),
    helperStyle: TextStyle(color: lightBlue, fontSize: 14, fontWeight: FontWeight.bold),
    outlineBorder: BorderSide(color: Colors.white, width: 1),
    enabledBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: Colors.white, width: 1),
    ),
    disabledBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: Colors.white, width: 1),
    ),
    focusedBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: Colors.white, width: 1),
    ),
    errorBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: errorColor, width: 1),
    ),
    focusedErrorBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: errorColor, width: 1),
    ),
  ),
  progressIndicatorTheme: ProgressIndicatorThemeData(color: primarySwatch.shade900),
  dialogTheme: DialogThemeData(
    backgroundColor: lightBackground,
    titleTextStyle: TextStyle(color: blue, fontSize: 20, fontWeight: FontWeight.bold),
    contentTextStyle: TextStyle(color: lightText, fontWeight: FontWeight.w400),
  ),
);

ButtonStyle get buttonTheme {
  return ButtonStyle(
    iconColor: WidgetStateProperty.all(primarySwatch.shade800),
    textStyle: WidgetStateProperty.all(TextStyle(color: primarySwatch.shade800)),
    backgroundColor: WidgetStateProperty.all(primarySwatch.shade200),
    shape: WidgetStateProperty.all(RoundedRectangleBorder(borderRadius: BorderRadius.circular(15))),
  );
}

// Dark Theme Data

ThemeData darkTheme = ThemeData(
  colorScheme: ColorScheme.dark(primary: primarySwatch.shade50, secondary: primarySwatch.shade200),
  dropdownMenuTheme: DropdownMenuThemeData(
    inputDecorationTheme: InputDecorationTheme(
      iconColor: darkText,
      suffixIconColor: darkText,
      border: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: darkSection, width: 1),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: darkSection, width: 1),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: const BorderRadius.all(Radius.circular(20)),
        borderSide: BorderSide(color: darkSection, width: 1),
      ),
      filled: true,
      fillColor: darkSection,
    ),
    menuStyle: MenuStyle(
      backgroundColor: WidgetStatePropertyAll(darkSection),
      maximumSize: WidgetStatePropertyAll(Size(double.infinity, 300)),
    ),
    textStyle: TextStyle(color: darkText),
  ),
  appBarTheme: AppBarTheme(
    backgroundColor: darkBackground,
    surfaceTintColor: darkBackground,
    centerTitle: true,
    iconTheme: IconThemeData(color: darkText),
    titleTextStyle: TextStyle(color: darkText, fontSize: 20),
  ),
  drawerTheme: DrawerThemeData(elevation: 0, backgroundColor: darkBackground),
  fontFamily: 'Inter',
  textTheme: TextTheme(
    bodyLarge: TextStyle(color: darkText),
    bodyMedium: TextStyle(color: darkText),
    bodySmall: TextStyle(color: darkText),
    headlineLarge: TextStyle(color: darkText),
    headlineMedium: TextStyle(color: darkText),
    headlineSmall: TextStyle(color: darkText),
    labelLarge: TextStyle(color: darkText),
    labelMedium: TextStyle(color: darkText),
    labelSmall: TextStyle(color: darkText),
    displayLarge: TextStyle(color: darkText),
    displayMedium: TextStyle(color: darkText),
    displaySmall: TextStyle(color: darkText),
  ),
  iconTheme: IconThemeData(color: darkText),
  cardColor: darkSection,
  buttonTheme: ButtonThemeData(
    colorScheme: ColorScheme(
      primary: primarySwatch.shade800,
      secondary: primarySwatch.shade600,
      surface: darkSection,
      error: errorColor,
      onPrimary: darkText,
      onSecondary: darkText,
      onSurface: darkText,
      onError: darkText,
      brightness: Brightness.dark,
    ),
    textTheme: ButtonTextTheme.primary,
  ),
  popupMenuTheme: PopupMenuThemeData(
    color: darkSection,
    textStyle: TextStyle(color: darkText),
  ),
  scaffoldBackgroundColor: darkBackground,
  primarySwatch: primarySwatch,
  canvasColor: primarySwatch.shade900,
  brightness: Brightness.dark,
  visualDensity: VisualDensity.standard,
  useMaterial3: true,
  elevatedButtonTheme: ElevatedButtonThemeData(style: buttonThemeDark),
  filledButtonTheme: FilledButtonThemeData(
    style: buttonThemeDark.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  textButtonTheme: TextButtonThemeData(
    style: buttonThemeDark.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  outlinedButtonTheme: OutlinedButtonThemeData(
    style: buttonThemeDark.copyWith(backgroundColor: WidgetStatePropertyAll(Colors.transparent)),
  ),
  inputDecorationTheme: InputDecorationTheme(
    filled: true,
    fillColor: darkSection,
    focusColor: darkSection,
    hoverColor: darkSection,
    prefixIconColor: lightBlue,
    labelStyle: TextStyle(color: darkText),
    hintStyle: TextStyle(color: darkText),
    floatingLabelStyle: TextStyle(color: lightBlue),
    helperStyle: TextStyle(color: lightBlue, fontSize: 14, fontWeight: FontWeight.bold),
    outlineBorder: BorderSide(color: darkSection, width: 1),
    enabledBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: darkSection, width: 1),
    ),
    disabledBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: darkSection, width: 1),
    ),
    focusedBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: darkSection, width: 1),
    ),
    errorBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: errorColor, width: 1),
    ),
    focusedErrorBorder: OutlineInputBorder(
      borderRadius: const BorderRadius.all(Radius.circular(20)),
      borderSide: BorderSide(color: errorColor, width: 1),
    ),
  ),
  progressIndicatorTheme: ProgressIndicatorThemeData(color: primarySwatch.shade900),
  dialogTheme: DialogThemeData(
    backgroundColor: darkBackground,
    titleTextStyle: TextStyle(color: darkText, fontSize: 20, fontWeight: FontWeight.bold),
    contentTextStyle: TextStyle(color: darkText, fontWeight: FontWeight.w400),
  ),
);

ButtonStyle get buttonThemeDark {
  return ButtonStyle(
    iconColor: WidgetStateProperty.all(darkText),
    backgroundColor: WidgetStateProperty.all(primarySwatch.shade600),
    shape: WidgetStateProperty.all(RoundedRectangleBorder(borderRadius: BorderRadius.circular(15))),
  );
}
*/
