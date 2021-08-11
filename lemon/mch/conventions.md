# Naming Conventions

Naming conventions in CM programming language use the camel case style for naming variables, enums, methods, and classes. Enums, methods, and variables should be in lower-case for their first letter whereas class names should be in upper-case.

```java
/**
 * Enumeration (lower case first letter).
 */
public enum myEnum : field access {
    entry0;
    entry1;
}


/**
 * Value (lower case first letter).
 */
public value myValue {
    public int field0;
    public int field1;
}


/**
 * Class (upper case first letter).
 */
public class MyClass {
    public int field0;
    public int field1;
}


/**
 * Function (lower case first letter).
 */
public int myFunction() {
    return 1;
}


/**
 * Alias, use the style of the original definition.
 */
public alias KRack = LongKitchenRackClass;
public alias kStyle = longKitchenStyleValue;
```

# White Space

All arithmetic operators except subtraction (-) and addition (+) should not have spaces from their operands. Spaces should also not separate unary operators such as decrement (++) and increment (--).

```java
int a = 1*2;
int b = 2/4;
int c = 1 + 2;
int d = 2 - 1;
int e = 2*100 + 4*(1 - 10/3);
```

Use spaces around equal sign (=) when it is used to assign.

```java
int f = a;
int g=a; // <- not like this.
```

# Blank Line

Two blank lines should be used between globals, functions, methods, classes, enums, and similar whereas one blank line should be used between class fields.

Braces

Do not mix braces and non-braces.

```java
// Do not mix braces and non-braces.
if (a) {
    b++;
    c++;
 } else {
    c--;
 }

// And not like this.
if (a) {
    b++;
    c++;
 } else
  c--;

// But this is okay.
if (a) for (v in a.members) {
      v++;
  }
```

Using "one-liners" can be effective, as long the length does not exceed 100 characters;

```java
// One-liners are okay, but do not exceed 100 chars per row.
if (snapper) for (z in snapper.neighbors) if (z as Rack) pln(z.rackW);
```

# Comments

Avoid using comments inside the scope of your code. If your function body starts to become longer and require many comments to explain your code, it is advisable to split it up into several smaller functions with descriptive names.

Header comments indicate a new section of code. Header comments are preceded by two blank lines and succeeded by one blank line. Header comments are not punctuated unless it consists of a sentence.

```java
/**********************************************************************

* Header comment describing section 1
 **********************************************************************/

//Section 1 code.

/**********************************************************************

* Header comment describing section 2
 **********************************************************************/

//Section 2 code.
```

Scope comments are used to comment about methods, variables, functions, and classes. Capitalization and punctuation should be used. A variable should have one blank line preceding the comment. Classes, methods, and functions should have two blank lines preceding the comment.

```java
/**

* Describe the class.
 */
public class SomeClass {

    /**
  * Describe the field.
     */
    public int i;
```

# Other Considerations

    Use a lot of white space to create sparse or airiness to the code.
    Keep function bodies reasonably short.
    Use relevant function and variable naming.
    Always comment on all definitions (even though it seems pointless)
    Always comment function return values.
