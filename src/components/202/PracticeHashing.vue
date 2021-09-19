<template>
  <Assignment :name="name" :title="title" :files="files">
    <template v-slot:description>
    <p>Hashing is the process of storing values in a <em>hash table</em>, usually represented as a list or array. Similar to indexing on a list, reading or updating values from a hash table may be performed in <code>O(1)</code> ("constant") time, meaning that the access time is independent of the size of the table. Table positions (also called "slots" or "buckets") are generated using a <em>hash function</em>, which is usually composed of simple arithmetic operations to keep table access fast.</p>
    <p>In order to allow for duplicate values in the table, each value must have a unique key associated with it; it is these keys, rather than their values, that are passed to the hash function to determine where the value should be stored in the table. However, even with unique keys, hash collisions - in which the hash function outputs the same position for different keys - are possible, and any hash table must employ some kind of collision resolution method.</p>
    <p>Two of the most common collision resolution methods are as follows.</p>
    <ul>
      <li><strong>Separate Chaining:</strong> Keep a list (chain) at each slot, and just add to or search through the list as necessary. Degrades to <code>O(N)</code> access time if some chains become very long.</li>
      <li><strong>Open Addressing:</strong> If a slot is occupied, choose the next one in a sequence. For Linear Probing, this means the very next empty slot; for other types of probing (e.g. Quadratic Probing), it means skipping ahead some number of positions to avoid value clustering in some parts of the table. Degrades to <code>O(N)</code> access time if clustering becomes frequent.</li>
    </ul>
    <p>In addition to the above, another method is to modify Separate Chaining to use a Binary Search Tree (BST) instead of a linear list. This approach allows even highly-occupied slots to have <code>O(log n)</code> (instead of linear) access time. However, in order to maintain this faster access time, the BST must be self-balancing.</p>
    </template>

    <template v-slot:implementation>
      <p>You are provided with an <code>Entry</code> class to instantiate key-value entries for the hash table. Some functions begin with the name <code>chain</code> or <code>probe</code>, referring to the use of separate chaining or linear probing, respectively. Only function calls using separate chaining should modify the <code>ref</code> attribute to link entires together; for function calls using linear probing, this attribute should always remain <code>None</code>.</p>
      <p>The provided <code>hash_key</code> definition is a simple hash function to be used in this assignment. It accepts two integers - a key to hash and a table size - and returns an index for the table.</p>
      <p>The <code>balance_tree</code> function is only intended to provide exposure to creating a self-balancing tree, and will not be used in any of the hash tables for this assignment.</p>

      <FunctionSignature name="get_load_factor" :params="[['table', 'List[Optional[Entry]]']]" type="float"/>
      <p>Return the load factor of the given table, which includes empty slots.</p>
      <pre>
table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
get_load_factor(table) -&gt; 0.5

table = [Entry(0, "A", None), Entry(5, "B", None), None, None, None]
get_load_factor(table) -&gt; 0.4</pre>

      <FunctionSignature name="resize" :params="[['table', 'List[Optional[Entry]]'], ['mode', 'str']]" type="List[Optional[Entry]]"/>
      <p>Resize and return the given table to be one more than twice the original length and rehash all integer keys from the original table into the resized table using the given collision resolution mode, which will be either <code>"chain"</code> or <code>"probe"</code>. Rehash lower-indexed keys first; for separate chaining only, rehash keys at the head of the chain first.</p>
      <pre>
table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))), Entry(7, "D", Entry(1, "E", None)), None]
resize(table, "chain") -&gt; [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None), None, Entry(3, "B", None), None, None, Entry(6, "C", None)]

table = [Entry(0, "A", None), Entry(3, "B", None), Entry(8, "C", None)]
resize(table, "probe") -&gt; [Entry(0, "A", None), Entry(8, "C", None), None, Entry(3, "B", None), None, None, None]</pre>

      <FunctionSignature name="chain_get" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int']]" type="str"/>
      <p>Return the value corresponding to the given key in the table, following separate chaining collision resolution. If the key does not exist in the table, raise a <code>KeyError</code>.</p>
      <pre>
table = [Entry(3, "B", Entry(0, "A", None)), None, None]
get(table, 0) -&gt; "A"</pre>

      <FunctionSignature name="chain_insert" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int'], ['val', 'str']]" type="List[Optional[Entry]]"/>
      <p>Add the given key-value pair (as a Entry object) to the table and return this updated table, following separate chaining collision resolution. If performing this update results in the load factor reaching 1.5, resize the table and rehash the entire table before returning it.</p>
      <pre>
table = [Entry(3, "C", Entry(0, "A", None)), Entry(4, "D", Entry(1, "B", None)), None]
insert(table, 8, "E") -&gt; [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)), None, Entry(3, "C", None), Entry(4, "D", None), None, None]</pre>

      <FunctionSignature name="chain_remove" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int']]" type="List[Optional[Entry]]"/>
      <p>Remove the Entry object containing the given key and return this updated table. If such an entry does not exist, raise a <code>KeyError</code>.</p>
      <pre>
table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
remove(table, 3) -&gt; [Entry(6, "C", Entry(0, "A", None)), None, None]</pre>

      <FunctionSignature name="probe_get" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int']]" type="str"/>
      <p>Return the value corresponding to the given key in the table, following linear probing collision resolution and terminating early if an empty slot (but not a nullified entry) is encountered. If the key does not exist in the table, raise a <code>KeyError</code>.</p>
      <pre>
table = [Entry(0, "A", None), Entry(3, "B", None), None]
get(table, 3) -&gt; "B"</pre>

      <FunctionSignature name="probe_insert" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int'], ['val', 'str']]" type="List[Optional[Entry]]"/>
      <p>Add the given key-value pair (as a Entry object) to the table and return this updated table, following linear probing collision resolution by replacing either an empty slot or a nullified entry with the new entry. If performing this update results in the load factor reaching 0.75, resize the table and rehash the entire table before returning it.</p>
      <pre>
table = [Entry(0, "A", None), Entry(1, "B", None), None]
insert(table, 2, "C") -&gt; [Entry(0, "A", None), Entry(1, "B", None), Entry(2, "C", None), None, None, None, None]</pre>

      <FunctionSignature name="probe_remove" :params="[['table', 'List[Optional[Entry]]'], ['key', 'int']]" type="List[Optional[Entry]]"/>
      <p>Call the <code>nullify</code> method on the Entry object containing the given key and return this updated table. If such an entry does not exist, raise a <code>KeyError</code>.</p>
      <pre>
table = [Entry(0, "A", None), Entry(1, "B", None), None]
remove(table, 0) -&gt; [Entry(None, None, None), Entry(1, "B", None), None]</pre>

      <FunctionSignature name="get_height" :params="[['root', 'Optional[TreeNode]']]" type="int"/>
      <p>Return the height (length of the longest path from the root) of the given binary tree. Let a single-node tree have a height of <code>0</code> and an empty tree a height of <code>-1</code>.</p>
      <pre>
root = TreeNode(3, TreeNode(2, TreeNode(1, None, None), None),
                   TreeNode(4, None, None))
get_height(root) -&gt; 2</pre>

      <FunctionSignature name="balance_tree" :params="[['root', 'Optional[TreeNode]']]" type="Optional[TreeNode]"/>
      <p>Given a BST, return its AVL-balanced form in which, for every node, the difference between the heights of its children is never greater than one. Rotations must occur during the traversal back up the tree, instead of while traversing down it.</p>
      <pre>
root = TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), None)
balance_tree(root) -&gt; TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))</pre>
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
        name: "pset6",
        title: "Problem Set VI: Hashing",
        files: ["pset6.py", "p6tests.py"]
      };
    }
}
</script>

