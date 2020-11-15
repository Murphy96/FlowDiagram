<template>
  <div>
    <v-tabs v-model="tab">
      <v-tab href="#tab-1"> Upload image </v-tab>
      <v-tab href="#tab-2" :disabled="!data"> Result </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item value="tab-1">
        <v-container>
          <v-row align="center" justify="center">
            <v-col>
              <center>
                <label for="image"
                  >Sube la fotografia de tu diagrama de flujo</label
                >
                <v-file-input
                  id="image"
                  label="File input"
                  prepend-icon="mdi-camera"
                  @change="onFileChange"
                ></v-file-input>
                <v-img max-width="50vw" :src="img" />
                <br />
                <v-btn
                  class="white--text indigo"
                  @click="getData()"
                  :disabled="!img"
                >
                  <v-icon class="mr-2"> mdi-heart </v-icon>
                  Process
                </v-btn>
              </center>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
      <v-tab-item value="tab-2">
        <v-row align="center" justify="center">
          <v-col cols="12" sm="6">
            <center>
              <p class="display-1">Something</p>
            </center>
          </v-col>
          <v-col cols="12" sm="6">
            <center>
              <p class="display-1">Code</p>
            </center>
          </v-col>
        </v-row>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="6">
            <template v-if="!waitData">
              <p>
                {{ data }}
              </p>
            </template>
            <template v-else>
              <center>
                <v-progress-circular
                  size="100"
                  width="10"
                  indeterminate
                  color="indigo"
                ></v-progress-circular>
              </center>
            </template>
          </v-col>
          <v-col cols="12" sm="6">
            <template v-if="!waitData">
              <div class="text-h5 mb-6">
                <code class="transparent">
                  {{ data }}
                </code>
              </div>
            </template>
            <template v-else>
              <center>
                <v-progress-circular
                  size="100"
                  width="8"
                  indeterminate
                  color="indigo"
                ></v-progress-circular>
              </center>
            </template>
          </v-col>
        </v-row>
      </v-tab-item>
    </v-tabs-items>
    <br />
    <br />
    <br />
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
  data: () => ({
    img: "",
    tab: "tab-1",
    waitData: false,
    data: "",
  }),
  methods: {
    async getData() {
      this.tab = "tab-2";
      this.waitData = true;
      await setTimeout(this.changeData, 1500);
    },
    changeData() {
      this.data = `Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus
            facere tempore magnam delectus similique nesciunt quidem
            sequi, expedita, a voluptates vel ipsa ipsam reprehenderit
            repellat odit fugit ab voluptas iure.`;
      this.waitData = false;
    },
    onFileChange(e) {
      this.img = URL.createObjectURL(e);
    },
  },
};
</script>
