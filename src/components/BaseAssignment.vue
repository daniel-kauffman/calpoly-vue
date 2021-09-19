<template>
  <div>
    <h1>{{ title }}</h1>
    <h4 v-if="dueDate"
        style="text-align: center;">
      Due {{ $root.formatDateStr(dueDate, true) }} by {{ time ? time : dueTime }} Pacific Time
    </h4>
    <div v-if="extra">
      <p style="color: blue; text-align: center;">This assignment is extra credit.</p>
    </div>
    <hr/>

    <div v-if="$slots.description">
      <h2>Description</h2>
      <slot name="description"></slot>
    </div>

    <h2>Implementation</h2>
    <div v-if="files.length > 0">
      <p>To begin, use the following file(s):
        <a  v-for="(filename, index) in files"
            :key="index"
            target="_blank"
            :href="directory + filename"
            style="margin-right: 1em;">{{ filename }}</a>
      </p>
    </div>

    <p v-if="files.some(s => s.endsWith('tests.py'))">Define the following functions in <code>{{ files[0] }}</code>, with at least 5 tests for each function (unless otherwise stated) in <code>{{ files[1] }}</code>.</p>
    <slot name="implementation"></slot>

    <div v-if="rubric">
      <h2>Scoring Rubric</h2>
      <p>
        The score you receive on this assignment will be based on which
        achievements the program satisfies. The achievements are listed in the
        order recommended to complete them.
      </p>
      <table id="rubric">
        <thead>
          <tr>
            <th></th>
            <th>Achievement</th>
            <th>Credit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, name, index) in rubric"
              :key="name">
            <td>{{ index + 1 }}</td>
            <td>{{ name }}</td>
            <td>{{ value }}%</td>
          </tr>
          <tr v-if="rubricTotal < 100">
            <td>{{ Object.keys(rubric).length + 1 }}</td>
            <td>Complete Program</td>
            <td>{{ 100 - rubricTotal }}%</td>
          </tr>
        </tbody>
      </table>
      <br/>
    </div>

    <div v-if="name && files">
      <h2>Submission</h2>
      <p>On a CSL server with <span v-html="fileStr"></span> in your current directory:</p>
      <table id="submission">
        <thead>
          <tr>
            <th>Instructor</th>
            <th>Command</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Daniel Kauffman</td>
            <td>/home/dkauffma/casey {{ $parent.$parent.activeCourse }} {{ name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    name: String,
    title: String,
    time: Number,
    files: Array,
    rubric: Object,
    extra: Boolean
  },
  data:
    function () {
      return {
        dueTime: "9PM",
        directory: process.env.BASE_URL
                   + this.$parent.$parent.activeCourse + "/"
      };
    },
  computed: {
    dueDate:
      function () {
        let course = this.$parent.$parent.activeCourse;
        let calendar = this.$parent.$parent.calendars[course];
        for (let dateStr in calendar) {
          if ("events" in calendar[dateStr]) {
            for (let title of calendar[dateStr]["events"]) {
              if (title === this.title.split(":")[0]) {
                return dateStr;
              }
            }
          }
        }
        return null;
      },
    rubricTotal:
      function () {
        return Object.values(this.rubric).reduce((a, b) => a + b);
      },
    fileStr:
      function () {
        var tags = [];
        for (let file of this.files) {
          tags.push("<code>" + file + "</code>");
        }
        return tags.join(" and ");
      }
  }
}
</script>


<style scoped>
table#submission td:first-child {
  text-align: right;
}
table#submission th:first-child, table#submission td:first-child {
  border-right: 1px solid lightgray;
}
table#submission td:last-child {
  font-family: monospace;
  font-size: 1.1em;
}
table#rubric td:nth-child(odd) {
    text-align: center;
}
table#rubric td:nth-child(2) {
    text-align: right;
}
</style>
