<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
    </template>

    <template v-slot:implementation>
      <p>The functions below must <strong>not</strong> mutate the input lists. Do not use <code>min</code>, <code>max</code>, or other built-in functions that trivialize the problems, such as <code>sorted</code>.</p>

      <FunctionSignature name="sort_ints" :params="[['ints', 'List[int]'], ['mode', 'str']]" type="List[int]"/>
      <p>Sort the given list of integers by calling one of the <code>*_pass</code> helper functions. <code>mode</code> will be one of <code>"bubble"</code>, <code>"selection"</code>, or <code>"insertion"</code> and specifies which <code>*_pass</code> function to call. If the given mode is not one of these values, raise a <code>ValueError</code>.</p>

      <FunctionSignature name="bubble_pass" :params="[['ints', 'List[int]']]" type="List[int]"/>
      <p>Perform one pass of Bubble Sort, defined as going through each pair of adjacent numbers once and swapping two when they are not in the correct order.</p>

      <FunctionSignature name="selection_pass" :params="[['ints', 'List[int]'], ['start', 'int']]" type="List[int]"/>
      <p>Perform one pass of Selection Sort, defined as finding the next lowest integer and swapping it with its correct position. The <code>start</code> parameter indicates the position of the first unsorted integer, which will be zero the first time this function is called.</p>

      <FunctionSignature name="insertion_pass" :params="[['ints', 'List[int]'], ['start', 'int']]" type="List[int]"/>
      <p>Perform one pass of Insertion Sort, defined as inserting the next unsorted integer into its correct position. The <code>start</code> parameter indicates the position of the first unsorted integer, which will be zero the first time this function is called.</p>

      <FunctionSignature name="binary_search" :params="[['ints', 'List[int]'], ['n', 'int']]" type="int"/>
      <p>Find integer <code>n</code> using binary search. If it exists, return its index; otherwise, return <code>-1</code>. Assume the list is already sorted.</p>
    </template>
  </Assignment>
</template>


<script>
import Assignment from "@/components/BaseAssignment.vue"
import FunctionSignature from "@/components/AssignmentFunctionSignature.vue"


export default {
  components: {
    Assignment,
    FunctionSignature
  },
  data:
    function () {
      return {
        name: "pset9",
        title: "Problem Set IX: Sort & Search",
        files: ["pset9.py", "p9tests.py"]
      };
    }
}
</script>
