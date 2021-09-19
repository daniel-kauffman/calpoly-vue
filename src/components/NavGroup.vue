<template>
  <div v-if="isNotEmpty">
    <button class="menu-item"
            :class="!collapsible || display ? 'expanded' : 'collapsed'"
            @click="display = !display">
      <span v-if="collapsible">{{ display ? "-" : "+" }}</span>
      <slot></slot>
    </button>
    <transition name="slide">
      <div :style="{'--item-count': Object.keys(this.group).length}"
           v-show="!collapsible || collapsible && display">
        <NavigationButton class="group-item"
                          v-for="(name, component, index) in group"
                          :key="index"
                          :name="name"
                          :component="component"
                          @set-active-component="propagateEvent">
          {{ (collapsible ? (index + 1) + ". " : "") + name.replace("*", "") }}
        </NavigationButton>
      </div>
    </transition>
  </div>
</template>


<script>
import NavigationButton from "./NavButton.vue"


export default {
  components: {
    NavigationButton
  },
  props: {
    collapsible: Boolean,
    group: Object
  },
  data:
    function () {
      return {
        display: !this.collapsible
      };
    },
  computed: {
    isNotEmpty:
      function () {
        return Object.keys(this.group).length > 0
               && Object.values(this.group).filter(x => x[0] != "*").length > 0;
      }
  },
  methods: {
    propagateEvent:
      function (event) {
        this.$emit("set-active-component", event);
        this.display = false;
      }
  }
}
</script>


<style scoped>
.group-item {
  border-left-style: double;
  border-width: 1px 0px 1px 6px;
}
.slide-enter-active, .slide-leave-active {
  transition: max-height 0.5s;
}
.slide-enter, .slide-leave-to {
  max-height: 0;
}
.slide-enter-to, .slide-leave {
  max-height: calc(3em * var(--item-count));
}
button.collapsed {
  background-color: var(--calpoly-green);
  border-color: var(--calpoly-gold);
}
button.expanded {
  background-color: var(--calpoly-gold);
  border-color: var(--calpoly-green);
}
button.collapsed:hover, button.expanded:hover {
  border-color: white;
}
button.collapsed:hover {
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
  animation-name: expand;
}
@keyframes expand {
  from {background-color: var(--calpoly-green);}
    to {background-color: var(--calpoly-gold);}
}
span {
  border: 1px solid gray;
  font-family: monospace;
  margin-right: 0.5em;
  padding: 0.01em 0.25em 0.01em 0.25em;
}
</style>
