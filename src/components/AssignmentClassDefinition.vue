<template>
  <div>
    <h6>class {{ name }}</h6>
    <slot></slot>
  </div>
</template>


<script>
export default {
  props: {
    name: String
  }
}
</script>


<style scoped>
div {
  border: 1px solid lightgray;
  padding: 1em;
  margin: 1em 0em 1em 0em;
}
h6 {
  font-family: monospace;
  font-size: 1.2em;
}
</style>
