# Introduction

Configura Magic (CM) is an object-oriented language with extensible syntax and support for incremental development. It is strongly typed, and with few exceptions statically typed. Memory for objects and other values is allocated and reclaimed automatically by a garbage collector.

The original motivation for CM came from dissatisfaction with C++ and the long work cycle caused by the need for restarting and recompiling the program after any changes to the source code.

# Compilation Process

CM source files are compiled to machine code before they are executed, but full compilation does not take place immediately. Instead, the source code is translated into different intermediate formats on-demand, and only translated into machine code when the compiler could not delay it any further [JIT Compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation). The compilation process is thus interleaved with the execution of the program. Different source files undergo different degrees of compilation depending on the behavior of the running program.

However, while virtual machines for languages such as Java typically use a mix of interpretation and compilation, the CM compiler never interprets the source code. CM source files are always translated into machine code before they are executed.

# Incremental Development

Files can be recompiled at runtime, enabling an incremental development style. For instance, functions can be rewritten and class fields added and removed at will, without having to restart the entire application for the changes to take effect. The development cycle is thus radically shortened, without sacrificing performance. This enables developers to get rapid feedback from the code they are working on.

# Source Code Organization

All CM source files should belong to a package and be encoded with the [UTF16](http://en.wikipedia.org/wiki/UTF16) character encoding. The source files are usually organized into directories named after the package the files belong to. Source files should have names that end in a dot followed by "cm".

For every developer, there should be a subpackage of cm.profile with the same name as the developer. For instance, if there is a developer with username steot, there should also be a package named cm.profile.steot. When in developer mode, the first source file that is run after a clean start is the file 'boot.cm' in the developer's profile.

# Helpful commands

Here's a list of the most used and common commands you might need to use while writing/troubleshooting CM code:

|Command | Description  |Example| 
|--|--|--| 
| `pln` | CM's very own `Console.WriteLine`, `alert` or `cout` | `pln("Hello World!");`| 
| `inspect` | Opens up the inspect tool with the object you provide as its parameter. It's a great way to look into what a given `Object` holds in its properties without having to rely in a series of `pln`s | `inspect(myObject);`| 
| `stackTrace` | Outputs the stack up to the point where this instruction was placed. Very useful to pinpoint the path your code took to arrive on a certain spot | `stackTrace();`| 
| `ptrace`| During (or specially after) a debug session, have you ever wondered where that one left over message *"HERE!!"* is? Fear no more, `ptrace` is basically a `pln` prefixed with the path to where that message is so you know exactly what file you need to undo/recompile to get rid of that leftover message. | `ptrace("Oh no!");`| 
| `developMode` | CET's built in flag to allow you to check whether or not you're currently running on a DEV's machine. As a matter of fact, if you haven't already, you should go check out this file: `.\base\cm\basic\release.cm`. It holds some interesting/useful flags for these sort of things. | `if (developMode) { pln("It works here!"); }` | 
| `cfd` | Useful if you need a simple print statement to see if a method/location is being hit. It will print the method its in along with the parameters to the method.. | `cfd();` | 

More useful commands can be found [here](https://support.configura.com/hc/en-us/articles/360060039274-Tracing).
****
