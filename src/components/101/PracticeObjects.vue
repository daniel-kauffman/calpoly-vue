<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
      <p>Thus far, data types discussed include, among others, integers, strings and lists. An instance of each of these types contains one or more values and has a set of operations that may be performed on those values. Integers represent a single number and may use arithmetic and relational operators; strings represent zero or more characters and have several functions (<code>upper</code>, <code>isalpha</code>, <code>split</code>, etc.) that operate on them; lists may contain any number of different types and have functions for modifying their size and contents.</p>
      <p>In object-oriented programming, an object is a user-defined type composed of internal variables called <strong>attributes</strong>. An object is also able to call special functions specific to itself called <strong>methods</strong>. Taken together, attributes (the data) and methods (the operations) allow us to consider an object to be of a distinct data type.</p>
      <p>The attributes and methods accessible to an object are defined inside a class definition. The class sets the structure to which each object created from it will conform. Like a function definiton, a class is only defined once; like function calls, any number of objects may be created (or <strong>instantiated</strong>) from a single class definition.</p>
      <p>Consider the <code>Student</code> class below.</p>
      <pre>
class Student:

    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return str(self.id) + " " + self.name</pre>

      <p>Using this class, any number of <code>Student</code> objects may be instantiated, each with their own <code>id</code> and <code>name</code> attributes.</p>
      <pre>
s1 = Student(1, "Daniel")
s2 = Student(2, "Daniel")

assert s1.id == 1
assert s1.name == "Daniel"
assert s2.id == 2
assert s2.name == "Daniel"

assert s1 == s2                 # s1 == s2 automatically calls s1.__eq__(s2)
assert str(s1) == "101 Daniel"  # str(s1) automatically calls s1.__repr__()</pre>

      <h4>Testing Methods</h4>
      <p>To test <code>__eq__</code> methods, use the <code>==</code> or <code>!=</code> operators.</p>
      <pre>
assert p1 == p2
assert p1 != p3</pre>
      <p>To test <code>__repr__</code> methods, cast an object to a string with <code>str</code>.</p>
      <pre>
assert str(p1) == "(1, 2)"</pre>
      <p>All other methods may be called normally using dot <code>.</code> notation.</p>
      <pre>
assert p1.distance(p2) == 0.0</pre>
      <p><strong>Never call double-underscore methods directly.</strong> In addition, all non-double-underscore methods must have a calling object (to the left of the dot); do not use the name of the class to call an instance method. The following lines demonstrate how <strong>not</strong> to call methods and would be considered incorrect.</p>
      <pre style="color: red;">
Point.__init__(1, 2)
Point.__eq__(Point(1, 2), Point(1, 2))
Point.__repr__(Point(1, 2))
p1.__eq__(p2)
p1.__repr__()
Point.distance(Point(1, 2), Point(3, 4))</pre>
    </template>

    <template v-slot:implementation>
      <p>In addition to module-level functions, you must write <code>assert</code> statements for every method (except the constructor) of each class.</p>

      <h4>Class Definitions</h4>
      <p>Write definitions for each of the classes below, including all methods.</p>

      <ClassDefinition name="Point">
        <FunctionSignature name="__init__" :params="[['self'], ['x', 'int'], ['y', 'int']]"/>
        <p>Representation of a point on a Cartesian plane with two attributes, x and y.</p>

        <FunctionSignature name="__eq__" :params="[['self'], ['other', '\'Point\'']]" type="bool"/>
        <p>Return True when both x and y attributes are equal and False otherwise.</p>

        <FunctionSignature name="__repr__" :params="[['self']]" type="str"/>
        <p>Return a string representing the point in the format <code>"(x, y)"</code>.</p>

        <FunctionSignature name="distance" :params="[['self'], ['to', '\'Point\'']]" type="float"/>
        <p>Return the Euclidean distance between the calling Point and the argument Point.</p>

        <FunctionSignature name="get_slope_intercept" :params="[['self'], ['other', '\'Point\'']]" type="Tuple[float, float]"/>
        <p>Return a tuple containing the <a target="_blank" href="https://en.wikipedia.org/wiki/Slope">slope</a> and <a target="_blank" href="https://en.wikipedia.org/wiki/Y-intercept">y-intercept</a> (in that order) of the line made from the given two points. Assume the line is not vertical.</p>
      </ClassDefinition>

      <ClassDefinition name="Line">
        <FunctionSignature name="__init__" :params="[['self'], ['p1', 'Point'], ['p2', 'Point']]"/>
        <p>Representation of a line made by two points. Line objects have exactly two attributes, <code>m</code> and <code>b</code>, that respectively store the slope and y-intercept of the line. Assume the line is not vertical.</p>

        <FunctionSignature name="__eq__" :params="[['self'], ['other', '\'Line\'']]" type="bool"/>
        <p>Return True when both slope and y-intercept attributes are equal and False otherwise.</p>

        <FunctionSignature name="__repr__" :params="[['self']]" type="str"/>
        <p>Return a string representing the line in slope-intercept format <code>"y = mx + b"</code>, substituting <code>m</code> and <code>b</code> with real numbers to one decimal place. If <code>b</code> is negative, replace the <code>+</code> operator with a <code>-</code> operator, as in <code>"y = 2.0x - 5.0"</code>.</p>

        <FunctionSignature name="to_parallel" :params="[['self'], ['point', 'Point']]" type="'Line'"/>
        <p>Return a Line object that is parallel to the calling Line object and passes through the given Point object (which is not on the original line).</p>

        <FunctionSignature name="to_perpendicular" :params="[['self']]" type="'Line'"/>
        <p>Return a Line object that is perpendicular to the calling Line object and shares the same y-intercept. Assume the original line is not horizontal.</p>
      </ClassDefinition>

      <ClassDefinition name="Circle">
        <FunctionSignature name="__init__" :params="[['self'], ['center', 'Point'], ['radius', 'int']]"/>
        <p>Representation of a circle using a Point as its center and an integer radius.</p>

        <FunctionSignature name="__eq__" :params="[['self'], ['other', '\'Circle\'']]" type="bool"/>
        <p>Return True when both center and radius attributes are equal and False otherwise.</p>

        <FunctionSignature name="__repr__" :params="[['self']]" type="str"/>
        <p>Return a string representing the circle in the format <code>"~r @ (x, y)"</code> where <code>~</code> is the radius, as in <code>"3r @ (1, 2)"</code>.</p>

        <FunctionSignature name="overlaps" :params="[['self'], ['other', '\'Circle\'']]" type="bool"/>
        <p>Return True when the calling Circle overlaps with the argument Circle and False otherwise. Two circles overlap when the distance between their center points is less than the sum of their radii (consider circles touching at the edge as non-overlapping). This function must not use branching.</p>

        <FunctionSignature name="bisects" :params="[['self'], ['line', 'Line']]" type="bool"/>
        <p>Return True if the line bisects the circle (passes through its center) and False otherwise.</p>
      </ClassDefinition>

      <h4>List Comprehensions on Objects</h4>
      <p>The following functions must be defined <strong>outside any class</strong> (not as methods) using a single <code>return</code> statement that uses a list comprehension (in other words, do not assign the list to a variable and then return the variable). The list comprehension can span multiple lines, if needed.</p>

      <FunctionSignature name="get_point_distances" :params="[['points', 'List[Point]']]" type="List[float]"/>
      <p>Return a list containing the distance from the origin (0, 0) to the corresponding point in the input list. This function must call the previously defined <code>distance</code> method of the Point class.</p>

      <FunctionSignature name="get_circle_distances" :params="[['circles', 'List[Circle]']]" type="List[float]"/>
      <p>Return a list containing the distance from the origin (0, 0) to the corresponding circle in the input list. This function must call the previously defined <code>distance</code> method of the Point class.</p>

      <FunctionSignature name="are_in_first_quadrant" :params="[['points', 'List[Point]']]" type="List[Point]"/>
      <p>Return all points in the given list that are in the first quadrant (both x and y components are positive) of the Cartesian plane.</p>

      <FunctionSignature name="overlaps_unit_circle" :params="[['circles', 'List[Circle]']]" type="List[Circle]"/>
      <p>Return a list of the Circle objects in the given list that overlap with the unit circle, centered at (0, 0) with radius 1. This function must call the previously defined <code>overlaps</code> method of the Circle class.</p>
    </template>
  </Assignment>
</template>


<script>
import Assignment from "@/components/BaseAssignment.vue"
import ClassDefinition from "@/components/AssignmentClassDefinition.vue"
import FunctionSignature from "@/components/AssignmentFunctionSignature.vue"


export default {
  components: {
    Assignment,
    ClassDefinition,
    FunctionSignature
  },
  data:
    function () {
      return {
        name: "pset8",
        title: "Problem Set VIII: Objects & Classes",
        files: ["pset8.py", "p8tests.py"]
      };
    }
}
</script>
