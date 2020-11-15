<template>
  <v-app>
    <v-app-bar app color="indigo" dark>
      <v-toolbar-title class="display-1">Flow Diagram</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn to="/" text> Home </v-btn>
      <v-btn to="/about" text>
        About
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
