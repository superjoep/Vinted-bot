<template>
  <div>
    <button @click="this.fetchScrapedData()">refresh</button>
    <h1 v-for="data in scrapedData">
      <img :src="data.imageSRC" /><br />
      <div style="font-size: medium">{{ data.imageTitle }}</div>
      <a :href="data.imageLink">View product</a>
    </h1>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      scrapedData: {
        title: "",
        content: "",
      },
    };
  },
  methods: {
    async fetchScrapedData() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/scrape"); // URL of your Flask backend
        this.scrapedData = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
      console.log(response);
    },
  },
  mounted() {
    this.fetchScrapedData(); // Fetch data when component is mounted
  },
};
</script>
