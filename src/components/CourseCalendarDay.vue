<template>
  <div class="container">
    <div class="row bg-light border-bottom px-2 py-1" style="font-size: 0.8em">
      {{ formattedDateStr }}
    </div>
    <div class="row flex-column p-1" style="height: 6em;">
      <span v-if="recess"
            style="background-color: black;">
        {{ recess }}
      </span>
      <span v-for="(item, i) in items"
            :key="i"
            :style="{ backgroundColor: getColor(item) }">
        {{ item }}
      </span>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    dateStr: String,
    items: Array,
    recess: String
  },
  computed: {
    formattedDateStr:
      function () {
        return this.$root.formatDateStr(this.dateStr);
      }
  },
  methods: {
    getColor:
      function (item) {
        if (item.startsWith("Quiz")) {
          return "crimson";
        } else if (item.startsWith("Project")) {
          return "royalblue";
        } else if (item.startsWith("Problem Set")
                   || item.startsWith("Discussion")) {
          return "green";
        } else {
          return "gray";
        }
      },
  }
}
</script>


<style scoped>
span {
  border-radius: 0.3em;
  color: white;
  font-size: 0.7em;
  font-weight: bold;
  margin: 0.1em;
  padding: 0.1em;
  text-align: center;
}
</style>
