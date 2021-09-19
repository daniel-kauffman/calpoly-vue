<template>
  <div>
    <h1>Course Updates</h1>
    <hr/>

    <div v-for="(entry, date, index) in updates"
         :key="index">
      <div class="header">
        <strong>[{{ date }}]</strong> {{ entry[0] }}
      </div>
      <div v-if="entry[1]"
           class="notes">
        {{ entry[1] }}
      </div>
    </div>

  </div>
</template>


<script>
export default {
  props: {
    course: Number
  },
  data:
    function () {
      return {
        updates: require("@/assets/" + this.course + "/updates.json")
      };
    },
}
</script>


<style scoped>
div.header {
  background-color: whitesmoke;
  border: 1px solid lightgray;
  font-family: monospace;
  font-size: 1.1em;
  margin-top: 2em;
  padding: 0.5em 0.5em 0.5em 1em;
}
div.notes {
  padding: 0.5em 0.5em 0.5em 1em;
}
</style>
