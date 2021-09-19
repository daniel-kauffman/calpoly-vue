<template>
  <nav>
    <div>
      <a target="_blank" href="https://www.calpoly.edu/">
        <img id="logo" src="@/assets/img/calpoly.png"/>
      </a>
    </div>

    <div id="courses">
      <button v-for="course of $parent.courses"
              :key="course"
              :class="course === activeCourse ? 'selected' : 'unselected'"
              @click="setActiveCourse">{{ course }}
      </button>
    </div>

    <template v-if="activeCourse">
      <NavigationButton component="Instructor"
                        @set-active-component="$emit('set-active-component',
                                                     $event)">
        Instructor Info
      </NavigationButton>

      <NavigationGroup v-for="(group, name, index) in groups"
                       :key="index"
                       :group="group"
                       @set-active-component="$emit('set-active-component',
                                                    $event)">
        {{ name }}
      </NavigationGroup>
    </template>
    <div class="menu-item selected" v-else>
      Select a Course
    </div>
  </nav>
</template>


<script>
import Instructor from "@/components/Instructor.vue"
import NavigationButton from "@/components/NavButton.vue"
import NavigationGroup from "@/components/NavGroup.vue"


export default {
  props: {
    activeCourse: Number
  },
  components: {
    NavigationButton,
    NavigationGroup
  },
  computed: {
    groups:
      function () {
        var courseGroups;

        if (this.activeCourse === 101) {
          courseGroups = {
            "Problem Sets": {
              PracticeArithmetic: "Arithmetic",
              PracticeFunctions: "Functions",
              PracticeBranching: "Branching",
              PracticeConditionalIteration: "Conditional Iteration",
              PracticeSequentialIteration: "Sequential Iteration",
              PracticeLists: "Lists",
              PracticeExceptions: "Exceptions",
              PracticeObjects: "Classes & Objects",
              PracticeSortSearch: "Sort & Search",
            },
          };
        } else if (this.activeCourse === 202) {
          courseGroups = {
            "Problem Sets": {
              PracticeLinkedLists: "Linked Lists",
              PracticeStacks: "Stacks",
              PracticeRecursion: "Recursion",
              PracticeBinaryTrees: "BinaryTrees",
              PracticeQueues: "Queues",
              PracticeHashing: "Hashing",
              PracticeGraphs: "Graphs",
              PracticeRegularExpressions: "Regular Expressions",
            },
          };
        } else if (this.activeCourse === 480) {
          courseGroups = {
            "Projects": {
              ProjectTileDriver1: "Tile Driver I",
              ProjectTileDriver2: "Tile Driver II",
              ProjectBiogimmickry: "Biogimmickry",
              ProjectMineShafted: "Mine Shafted",
              ProjectBoardStupid: "Board Stupid",
              ProjectMoonlander: "Moonlander II",
              ProjectKnowOp: "Know Op"
            },
          };
        }

        var generalGroups = {
          "Course Details": {
            CourseDescription: "Description",
            CourseAssessment: "Assessment",
            CourseResources: "Resources",
            CourseCalendar: "Calendar"
          },
          "Policies": {
            PolicyEnrollment: "Enrollment",
            PolicyStyle: "Code Style",
            PolicyConduct: "Student Conduct",
            PolicyAccommodation: "Accommodation"
          },
          "Guides": {
            GuideCasey: "Casey Submission System",
            GuideGettingStarted: "Getting Started",
            GuideSecureShell: "Secure Shell (SSH)",
            GuideVim: "Vim Editor"
          }
        };

        return {...courseGroups, ...generalGroups};
      }
  },
  methods: {
    isCollapsible:
      function (name) {
        return name === "Problem Sets"
               || name === "Projects"
               || name === "Discussions";
      },
    setActiveCourse:
      function (event) {
        this.$emit("set-active-course", parseInt(event.target.innerHTML));
        this.$emit("set-active-component", Instructor);
        this.$root.scrollToTop();
      }
  }
}
</script>


<style scoped>
>>> .menu-item {
  border-style: solid;
  border-width: 1px 0px 1px 0px;
  color: white;
  padding: 0.5em;
  text-align: left;
  text-indent: 1em;
  width: 100%;
}
img#logo {
  padding: 1em;
  width: 100%;
}
#courses {
  display: grid;
  grid-auto-flow: column;
}
#courses button {
  border-style: solid;
  border-width: 0px 1px 0px 1px;
  color: white;
  text-align: center;
}
#courses button:hover {
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
  animation-name: expand;
}
@keyframes expand {
  from {background-color: var(--calpoly-green);}
    to {background-color: var(--calpoly-gold);}
}
.selected {
  background-color: var(--calpoly-gold);
  border-color: var(--calpoly-green);
}
.unselected {
  background-color: var(--calpoly-green);
  border-color: var(--calpoly-gold);
}
nav {
  background-color: var(--calpoly-green);
  width: 18em;
}
nav > :first-child, nav > :last-child {
  border-bottom-color: var(--calpoly-gold);
  border-bottom-style: solid;
  border-bottom-width: 1px;
}
</style>
