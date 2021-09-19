import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false


const requireComponent = require.context("@/components/", true);
requireComponent.keys().forEach(fileName => {
  const componentName = fileName.split("/")
                                .pop()
                                .replace(/Base/, "")
                                .replace(/\.\w+$/, "");
  const componentConfig = requireComponent(fileName);
  Vue.component(componentName, componentConfig.default || componentConfig);
});


new Vue({
  el: "#app",
  methods: {
    scrollToTop:
      function () {
        window.scrollTo(0, 0);
      },
    formatDateStr:
      function (dateStr, includeDay = false) {
        var formatted = "";
        let dateArray = new Date(dateStr).toDateString().split(" ");
        if (includeDay) {
          formatted += dateArray[0] + ", ";
        }
        return formatted + dateArray[1] + " " + parseInt(dateArray[2], 10);
      }
  },
  render: h => h(App),
})//.$mount('#app')
