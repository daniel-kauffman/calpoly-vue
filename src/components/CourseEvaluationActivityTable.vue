<template>
  <table class="table table-striped w-auto text-center">
    <thead>
      <tr>
        <th>Activity</th>
        <th>Number</th>
        <th>Each %</th>
        <th>Total %</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(activity, i) in activities[$parent.$parent.activeCourse]"
          :key="i">
        <td>{{ activity.name }}</td>

        <td class="text-monospace" v-if="activity.count">{{ activity.count }}</td>
        <td v-else></td>

        <td class="text-monospace" v-if="activity.each">{{ activity.each }}</td>
        <td v-else></td>

        <td class="text-monospace">{{ activity.total }}</td>
      </tr>
    </tbody>
  </table>
</template>


<script>
export default {
  data:
    function () {
      return {
        "activities": {
          101:[
            {name: "Problem Sets", count: 8, total: 20},
            {name: "Projects", count: 3, total: 30},
            {name: "Quizzes", count: 4, total: 30},
            {name: "Final Exam", count: 1, total: 15},
            {name: "Conduct", count: null, total: 5}
          ],
          202:[
            {name: "Problem Sets", count: 8, total: 20},
            {name: "Projects", count: 3, total: 30},
            {name: "Quizzes", count: 4, total: 30},
            {name: "Final Exam", count: 1, total: 15},
            {name: "Conduct", count: null, total: 5}
          ],
          480:[
            {name: "Projects", count: 6, total: 50},
            {name: "Discussions", count: 7, total: 25},
            {name: "Presentation", count: null, total: 20},
            {name: "Conduct", count: null, total: 5}
          ],
        }
      };
    },
  created:
    function () {
      for (var activity of this.activities[this.$parent.$parent.activeCourse]) {
        if (activity.count) {
          activity["each"] = Math.round(activity.total / activity.count * 10) / 10;
        } else {
          activity["each"] = null;
        }
      }
    }
}
</script>
