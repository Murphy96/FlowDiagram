<template>
  <div>
    <v-tabs v-model="tab">
      <v-tab> Upload image </v-tab>
      <v-tab> Loading </v-tab>
      <v-tab> Result </v-tab>
      <v-tab-item>
        <v-container>
          <v-row align="center" justify="center">
            <v-col>
              <label for="">Sube la fotografia de tu diagrama de flujo</label>
              <v-file-input
                id="image"
                label="File input"
                filled
                prepend-icon="mdi-camera"
                @change="onFileChange"
              ></v-file-input>
              <v-img max-width="100%" :src="img" />
              <br />
              <v-btn dark class="indigo">
                <v-icon class="mr-2"> mdi-heart </v-icon>
                Process
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
      <v-tab-item>
        <v-row align="center" justify="center" width="100%">
          <v-col>
            <center>
              <v-progress-circular
                size="100"
                width="10"
                indeterminate
                color="indigo"
              ></v-progress-circular>
            </center>
          </v-col>
        </v-row>
      </v-tab-item>
      <v-tab-item>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="6">
            <p class="display-1">Something</p>
          </v-col>
          <v-col cols="12" sm="6">
            <p class="display-1">Code</p>
          </v-col>
        </v-row>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="6">
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero
              ducimus iure doloribus nam iste sed assumenda deserunt dolores in,
              molestiae fuga doloremque! Laboriosam cumque ipsa fuga libero
              ratione, animi incidunt.
            </p>
          </v-col>
          <v-col cols="12" sm="6">
            <div class="text-h5 mb-6">
              <code class="transparent">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus
                facere tempore magnam delectus similique nesciunt quidem sequi,
                expedita, a voluptates vel ipsa ipsam reprehenderit repellat
                odit fugit ab voluptas iure.
              </code>
            </div>
          </v-col>
        </v-row>
      </v-tab-item>
    </v-tabs>
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
    tab: null,
  }),
  methods: {
    onFileChange(e) {
      this.img = URL.createObjectURL(e);
    },
  },
};
</script>
