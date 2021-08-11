# TOC

    -Preface
    -Operator and Collections
    -String Comparisons
    -Sequences of if Statements
    -Boolean Expressions
    -Switch Statements vs. if Statements
    -Initial Size of Collections
    -Functions
    -Objects vs. Values
    -The const Keyword
    -Common Subexpressions
    -Datatype Size
    -Prefer Local Variables Over Fields
    -Do Not Keep Unused Objects
    -Inlining

# Preface

The most important things to get right are algorithms and data structures. This guide will not help you with that. Instead, it contains a list of things you need to keep in mind to write efficient code at a lower level.

# Operator and Collections

If you need to perform repeated contains tests on a collection, it is better to use a set than a sequence unless the sequence is always very short. This is because contains tests on sequences that have linear time complexity.

# String Comparisons

Strings are compared by looking at all characters until a match can be either verified or refuted. Naturally, this is much slower than comparing two pointers or enums (which are just integers). Therefore, avoid string comparisons in performance-sensitive code. Symbols, on the other hand, are immutable and can be compared efficiently just by looking at the pointers (the syntax for Symbols is #"contents", rather than "contents".)

# Sequences of if Statements

If the conditions used in a sequence of if statements are mutually exclusive, it is important to use the else keyword to link the statements together. Otherwise, as many tests will be tried as there are if statements.

When a sequence of if statements have been linked together using the else keyword, the conditions that are most frequently true should come first since that skips the largest number of tests on average.

It can also be a good idea to order tests by efficiency so that expensive tests come at the end (if the tests are not equally costly to execute). The same goes for the order of conditions inside complex boolean expressions.
Example of Bad Code

Here only one test can be true if key is a local variable, so the if statements should be linked with the else keyword.

```java
if (key == 1) doSomething1();
if (key == 2) doSomething2();
if (key == 3) doSomething3();
```

# Boolean Expressions

The order in which conditions are specified affects performance. Place the conditions that are most likely to short-circuit the computation first.
Example:

```java
if (oftenFalse and oftenTrue) ..
if (oftenTrue or oftenFalse) ..
```

# Switch Statements vs. if Statements

Prefer switch statements for large sets of mutually exclusive tests, unless you know that some tests are much more likely to be true than others. In that case, perform those tests first in a chain of if statements.

Switch statements can be compiled into many different forms. The encoding that best suits the specific set of cases will be chosen. For integral types, the compiler can currently choose between using a jump table, binary search, and linear search. Switch statements on strings are encoded as state machines.

# Initial Size of Collections

Specify a good initial size (first parameter of the constructor) if you know the typical number of elements a sequence (or map, or set) will contain. Sequences are implemented as arrays, and when their capacity is exceeded the contents will be copied into a new sequence of greater size. By allocating enough space upfront you may avoid the work implied by incremental adjustment.

Maps and sets are implemented as hash tables, or in other words, arrays of buckets. The above reasoning applies to them too.

# Functions

Member functions declared as final are faster to call than methods, and are easier to inline. The penalty of a non-final method call can be significant if the call is repeated many times.

# Objects vs. Values

Choosing to represent something with a value instead of a class can improve performance since values are allocated at the variable declaration site (the stack for a local variable, or the surrounding object in case of a field) and thus do not increase the load on the garbage collector. Cache performance can also be improved.

# The const Keyword

Using the const keyword can enable the compiler to precompute expressions involving the identifier.

# Common Subexpressions

Eliminate common subexpressions by storing the result in a local variable.
Example

Instead of

```java
if (foo.bar.whee and key == 1) {
    x = foo.bar.whee;
}
```

Write

```java
int whee = foo.bar.whee;
if (whee and key == 1) {
    x = whee;
}
```

# Datatype Size

Use the smallest data type that will do the job if there will be many instances of it. For instance, there are variations of the int datatype with smaller sizes (int8 and int16). This advice does not apply to local variables or function parameters, since all values get at least 32 bits anyway there.

# Prefer Local Variables Over Fields

This will be more important in the future when the compiler does more advanced optimizations. Right now the advantages are that stack variables are more likely to be cached and accessing them involves fewer instructions. Also, object references on the stack are more likely to be overwritten early, enabling the memory of the objects to be reclaimed faster.

# Do Not Keep Unused Objects

The garbage collector works best with short-lived objects. Make the lifetime of your objects as short as possible. The lifetime of references on the stack is limited by the lifetime of the function call, but global variables can live forever. Be careful not to extend the lifetime of global references more than necessary. Collections (sequences, maps..) of references are especially important.

# Inlining

To make a function call, the compiler must pass all arguments from the caller to the callee and transfer control to the latter. For small functions, this overhead can harm performance. Consider using the inline property on functions that are called frequently from performance-critical parts of the code. However, be aware that using inlining frivolously can have the opposite effect and degrade performance since the size of the code can increase. Measure the effect and consult with other people to decide when inlining should be used.
