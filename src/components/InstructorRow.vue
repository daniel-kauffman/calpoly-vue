<template>
  <div class="flex-container">
    <div id="title">{{ title }}</div>
    <div id="content">
      <slot></slot>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    title: String
  }
}
</script>


<style scoped>
div#title {
  font-weight: bold;
  text-align: right;
  padding-top: 1em;
  width: 12em;
}
div#content {
  font-family: monospace;
  font-size: 1.3em;
}
div.flex-container {
  display: flex;
  flex-direction: row;
}
a, div {
  display: inline;
  padding: 0.5em;
}
</style>
