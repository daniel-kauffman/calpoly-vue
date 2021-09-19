<template>
  <div>
    <h1>{{ title }}</h1>
    <h4 style="text-align: center;">Due {{ $root.formatDateStr(dueDate, true) }} by {{ time ? time : dueTime }} Pacific Time</h4>
    <hr/>

    <h2>Background</h2>
    <slot name="background"></slot>

    <h2>Discussion</h2>
    <slot name="discussion"></slot>

    <h2>Groups</h2>
    <div v-if="groups && groups.length > 0">
      <label>Cal Poly Username:</label>
      <input v-model="username" maxlength=8 />

      <ul>
        <li v-for="name of getGroup(username)"
            :key="name">
          {{ name }}@calpoly.edu
        </li>
      </ul>
    </div>
    <p v-else><em>Groups not yet assigned.</em></p>

  </div>
</template>


<script>
import dates from "@/assets/480/calendar.json"

export default {
  props: {
    groups: Array,
    time: Number,
    title: String
  },
  data:
    function () {
      return {
        dueTime: "9PM",
        username: ""
      };
    },
  computed: {
    dueDate:
      function () {
        for (let dateStr in dates) {
          if ("events" in dates[dateStr]) {
            for (let title of dates[dateStr]["events"]) {
              if (title === this.title.split(":")[0]) {
                return dateStr;
              }
            }
          }
        }
        return null;
      },
  },
  methods: {
    getGroup:
      function (username) {
        for (let group of this.groups) {
            if (group.includes(username)) {
                return group.filter(name => name !== username);
            }
        }
        return [];
      }
  }
}
</script>


<style scoped>
input {
  height: 2em;
  margin-left: 1em;
  width: 6em;
}
</style>
