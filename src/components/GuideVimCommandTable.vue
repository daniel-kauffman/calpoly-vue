<template>
  <table class="table w-auto mx-2">
    <caption class="text-center"><slot></slot></caption>
    <thead class="text-center">
      <tr>
        <th>Command</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(description, command) in commands"
          :key="command">
        <td class="text-center text-monospace">
          <span class="badge badge-light border border-secondary p-2 mx-1"
                v-for="(key, i) in formatCommand(command)"
                :key="i">
            {{ key }}
          </span>
        </td>
        <td>{{ description }}</td>
      </tr>
    </tbody>
  </table>
</template>


<script>
export default {
  props: {
    commands: Object
  },
  methods: {
    formatCommand:
      function (command) {
        return command.split("+");
      }
  }
}
</script>


<style scoped>
span.badge {
  box-shadow: -1px 1px;
  color: black;
  font-size: 1.0em;
}
</style>
