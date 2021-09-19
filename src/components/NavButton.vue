<template>
  <button class="menu-item"
          @click="setActiveComponent"
          v-if="isVisible">
    <slot></slot>
  </button>
</template>


<script>
export default {
  props: {
    name: String,
    component: String
  },
  computed: {
    isVisible:
      function () {
        let showAll = this.$parent.$parent.$parent.showAll;
        return showAll || this.name === undefined ? true : this.name[0] != "*";
      }
  },
  methods: {
    setActiveComponent:
      function () {
        this.$emit("set-active-component", this.component);
        this.$root.scrollToTop();
      }
  }
}
</script>


<style scoped>
button {
  background-color: var(--calpoly-green);
  border-color: var(--calpoly-gold);
}
button:hover {
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
  animation-name: expand;
  border-color: white;
}
@keyframes expand {
  from {background-color: var(--calpoly-green);}
    to {background-color: var(--calpoly-gold);}
}
</style>
