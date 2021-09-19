<template>
  <table>
    <thead v-if="assistantHours">
      <tr>
        <th style="background-color: whitesmoke;"></th>
        <th>Daniel</th>
        <th>TA (CSL)</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(hour, day) in hours" :key="day">
        <td style="background-color: var(--calpoly-gold);"
            v-if="day === getDayOfWeek()">{{ day }}</td>
        <td style="background-color: var(--calpoly-green);"
            v-else>{{ day }}</td>

        <td v-if="hour">
          <div>{{ hour[0] }}</div> - <div>{{ hour[1] }}</div>
        </td>
        <td class="no-hours" v-else>
          <em>No Hours Scheduled</em>
        </td>

        <template v-if="assistantHours">
          <td v-if="assistantHours[day]">
            {{ toHourStr(assistantHours[day]) }}
          </td>
          <td class="no-hours" v-else>
            <em>No Hours Scheduled</em>
          </td>
        </template>

      </tr>
    </tbody>
    <caption style="font-size: 0.58em; text-align: justify;">
      Hours are subject to change or cancelation. Changes will be announced to
      the class. Cancelations will be posted on this page.
    </caption>
  </table>

</template>


<script>
export default {
  data:
    function () {
      return {
        hours: {
          "Mon": null,
          "Tue": null,
          "Wed": null,
          "Thu": null,
          "Fri": null
        },
        assistantHours: null
      };
    },
  methods: {
    getDayOfWeek:
      function () {
        var day = new Date().getDay();
        switch (day) {
          case 1: return "Mon";
          case 2: return "Tue";
          case 3: return "Wed";
          case 4: return "Thu";
          case 5: return "Fri";
        }
      }
  }
}
</script>


<style scoped>
div {
  display: inline-block;
  width: 3em;
}
th, td {
  background-color: white;
  border: 1px solid lightgray;
  padding: 0.2em 0.8em 0.2em 0.8em;
}
th {
  text-align: center;
}
td:first-child {
  color: white;
}
td.no-hours {
  background-color: whitesmoke;
  color: gray;
}
</style>
