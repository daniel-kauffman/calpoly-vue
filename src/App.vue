<template>
  <div class="flex-container"
       style="min-height: 100%;"
       @keydown.shift="setShowAll">
    <NavigationColumn :activeCourse="activeCourse"
                      @set-active-course="setActiveCourse"
                      @set-active-component="setActiveComponent"/>
    <div id="main-pane">
      <keep-alive>
        <component :is="activeComponent"
                   :course="activeCourse"/>
      </keep-alive>
    </div>
  </div>
</template>


<script>
import Instructor from "@/components/Instructor.vue"
import NavigationColumn from "@/components/NavColumn.vue"


export default {
  components: {
    Instructor,
    NavigationColumn
  },
  data:
    function () {
      return {
        activeCourse: null,
        activeComponent: Instructor,
        showAll: false,
        courses: [101, 202, 480],
        calendars: {"101": require("@/assets/101/calendar.json"),
                    "202": require("@/assets/202/calendar.json"),
                    "480": require("@/assets/480/calendar.json")}
      }
    },
  methods: {
    setActiveCourse:
      function (course) {
        this.activeCourse = course;
      },
    setActiveComponent:
      function (component) {
        this.activeComponent = component;
      },
    setShowAll:
      function (event) {
        if (event.code === "Digit8") {
            this.showAll = true;
        }
      }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
:root {
  --calpoly-green: #154734;
  --calpoly-gold: #BD8B13;
}
#main-pane {
  padding: 0.5em 2em 0.5em 2em;
  width: 100%;
}
button:focus {
  outline: none;
}
code {
  background-color: whitesmoke;
  border: 1px solid lightgray;
  border-radius: 0.2em;
  color: black;
  font-family: monospace;
  margin: 0em 0.2em 0em 0.2em;
  padding: 0em 0.2em 0em 0.2em;
}
div.flex-container {
  display: flex;
}
figcaption {
  text-align: center;
}
h1 {
  text-align: center;
}
p, li {
  text-align: justify;
}
pre {
  margin-left: 2em;
}
th, td {
  padding: 0.8em;
}
tbody > tr:nth-child(odd) {
  background-color: whitesmoke;
}
thead {
  text-align: center;
}
tr {
  border-top: 1px solid lightgray;
  border-bottom: 1px solid lightgray;
}
</style>
