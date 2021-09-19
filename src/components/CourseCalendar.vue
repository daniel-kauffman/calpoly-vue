<template>
  <div class="container-fluid">
    <h1 class="text-center">Course Calendar</h1>
    <hr/>

    <p>This calendar is tentative and <strong>subject to change</strong>. It is intended to provide students approximate dates for course events but should not be used for planning purposes. Any changes made to this calendar within one week of the due date will be announced to the class.</p>

    <div class="d-flex justify-content-center">
      <button class="btn text-white mx-1 mb-3"
              :class="{ activeSchedule: !showTopics }"
              @click="toggleSchedule()">
        Important Dates
      </button>
      <button class="btn text-white mx-1 mb-3"
              :class="{ activeSchedule: showTopics }"
              @click="toggleSchedule()">
        Activity Guide
      </button>
    </div>

    <table class="table table-striped table-bordered text-monospace">
      <thead class="thead-light text-center">
        <tr>
          <th></th>
          <th v-for="day in days" :key="day">{{ day }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="i in Math.floor(dateStrs.length / days.length)" :key="i">
          <td class="align-middle text-center text-monospace">{{ weeks[i - 1] }}</td>
          <td class="p-0"
              v-for="j in days.length" :key="j">
            <CourseCalendarDay :dateStr="getDateStr(i, j)"
                               :items="getItems(i, j)[showTopics ? 'topics' : 'events']"
                               :recess="getItems(i, j).recess ? getItems(i, j).recess[0] : null"/>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import CourseCalendarDay from "./CourseCalendarDay.vue"


export default {
  components: {
    CourseCalendarDay
  },
  props: {
    course: Number
  },
  data:
    function () {
      return {
        showTopics: false,
        days: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        weeks: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "F"],
        start: new Date("2021/06/21")
      };
    },
  computed: {
    dateStrs:
      function () {
        var dateObjects = [];
        for (let i = this.start.getDay(); i >= 0; --i) {
          dateObjects.push(this.offsetDate(this.start, -i));
        }
        {
          let nextDate = this.start;
          for (let day = 0; day < this.weeks.length * 7; ++day) {
            nextDate = this.offsetDate(nextDate, 1);
            dateObjects.push(nextDate);
          }
        }
        return dateObjects.map(this.toModifiedISOString);
      },
    items:
      function () {
        return this.$parent.calendars[this.course];
      }
  },
  methods: {
    offsetDate:
      function (thisDate, offset) {
        let msPerDay = 1000 * 60 * 60 * 24;
        return new Date(thisDate.valueOf() + (msPerDay * offset));
      },
    toModifiedISOString:
      function (dateObject) {
        let pattern = /[0-9]{4}-[0-9]{2}-[0-9]{2}/;
        return dateObject.toISOString().match(pattern)[0].split("-").join("/");
      },
    getDateStr:
      function (row, col) {
        return this.dateStrs[(row - 1) * this.days.length + (col - 1)];
      },
    getItems:
      function (row, col) {
        let items = this.items[this.getDateStr(row, col)];
        return items ? items : {};
      },
    toggleSchedule:
      function () {
        this.showTopics = !this.showTopics;
      }
  }
}
</script>


<style scoped>
button.btn {
  background-color: var(--calpoly-green);
  width: 10em;
}
button.activeSchedule {
  background-color: var(--calpoly-gold);
}
table {
  table-layout: fixed;
}
th:not(:first-child) {
  box-shadow: 1px 1px, -1px -1px;
  position: sticky;
  top: 0;
}
th:first-child {
  width: 3em;
}
td:first-child {
  background-color: var(--calpoly-green);
  color: white;
}
</style>
