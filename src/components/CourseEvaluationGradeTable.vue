<template>
  <table class="table table-striped w-auto text-center">
    <thead>
      <tr>
        <th class="px-4">Grade</th>
        <th class="px-4">Min</th>
        <th class="px-4">Max</th>
      </tr>
    </thead>
    <tbody class="text-monospace">
      <tr v-for="(min, i) in gradeMinimums" :key="i">
        <td class="text-monospace" v-if="passingGrades[i].length === 1">{{ passingGrades[i] }}&nbsp;</td>
        <td class="text-monospace" v-else>{{ passingGrades[i] }}</td>

        <td class="text-monospace">{{ min }}</td>
        <td class="text-monospace" v-if="i > 0">{{ gradeMinimums[i - 1] - 1}}</td>
        <td v-else></td>
      </tr>
      <tr>
        <td class="text-monospace">F&nbsp;</td>
        <td></td>
        <td class="text-monospace">{{ gradeMinimums[gradeMinimums.length - 1] - 1 }}</td>
      </tr>
    </tbody>
  </table>
</template>


<script>
export default {
  data:
    function () {
      return {
        passingGrades: [      "A", "A-",
                        "B+", "B", "B-",
                        "C+", "C", "C-",
                        "D+", "D", "D-"],
//        gradeMinimums: [93, 90, 87, 83, 80, 77, 73, 70]
        gradeMinimums: [92, 88, 84, 80, 76, 72, 68, 64, 63, 61, 60]
      };
    }
}
</script>
