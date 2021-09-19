<template>
  <div class="flex-container">
    <div>{{ name }}(</div>
    <div v-for="(div, i) in paramTags"
         :key="i"
         v-html="div">
    </div>
    <div>-&gt;&nbsp;{{ verifiedType }}</div>
  </div>
</template>


<script>
export default {
  props: {
    name: String,
    params: Array,
    type: String
  },
  computed: {
    paramTags:
      function () {
        if (!this.params) {
          return ["<div>)&nbsp;</div>"];
        }
        var divs = [];
        for (let i = 0; i < this.params.length; ++i) {
          divs.push("<div>"
                    + this.params[i][0]
                    + (this.params[i][0] != "self" ?
                       ": " + this.params[i][1] : "")
                    + (i < this.params.length - 1 ? "," : ")") + "&nbsp;"
                    + "</div>");
        }
        return divs;
      },
    verifiedType:
      function () {
        if (!this.type) {
          return "None";
        } else if (this.type.endsWith("?")) {
          return "Optional[" + this.type.slice(0, -1) + "]";
        } else {
          return this.type;
        }
      }
  },
}
</script>


<style scoped>
div.flex-container {
  background-color: whitesmoke;
  border: 1px solid lightgray;
  display: flex;
  flex-wrap: wrap;
  font-family: monospace;
  font-size: 1.1em;
  margin-bottom: 0.5em;
  margin-top: 2em;
  padding: 0.5em 0.5em 0.5em 1em;
}
</style>
