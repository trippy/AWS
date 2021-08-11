

# Index

 1.  Embedded files
 2. `.rs` Files
    - Loading `.rs` Files 
    - Load order
  3. `string` / `str` handling
     - Concatenation
     - Helper functions


# 1. Embedded Files
In order to pack files (be it a `PNG`, `CM3D`, `.RS`, etc) inside your extension all you need to do is to return it inside the `package ExtensionInfo getExtensionInfo() : referred {` method.  

Here's and example:
```java
/**
* Actual extension info, don't change function name
*/
package ExtensionInfo getExtensionInfo() : referred {
    ExtensionInfo info = loadExtensionInfoFromXml(#:package);
    Url[] files();
    files << cmNative("custom/myextension/resources/*.rs");
    files << cmNative("custom/myextension/images/*.png");
    files << cmNative("custom/myextension/randomStuff/*.*");
    info.filesToInclude = files;
    return info;
}
```

# 2. `.rs` Files

Resource files are super useful but it's not always fun to go through the process of making sure they are properly set up for you extension/package.

## Loading `.rs` files

Your files need to be properly registered and the right place to do so is inside the method `public  void  initialize(ExtensionEnv env)` in your `ToolboxCatalogExtension` class (e.g.: `UltraLazyExtension`).

The way to do so is by calling `safeLoadRs` along with `cmFindUrl` .

Here's an example if we want to embed `cm/core/core.rs` into our extension:  `safeLoadRs(cmFindUrl("cm/core/core.rs"));`

## Load order
By calling the method `putNextRsPkg` you get to build a priority lookup graph that CET will use in order to fetch the correct description for your `$label`. 

The first parameter is the `parent` package that will be searched for and, the second parameter is the fallback option (in case a given resource is not found in `parent`).

Calls to the `putNextRsPkg` are also usually set up inside the Extension's `public  void  initialize(ExtensionEnv env)`    method.

Here's an example that first searches for resource inside the package `custom.mypackage` and, if nothing is found, falls back to `cm.abstract.office`: `putNextRsPkg("custom.mypackage", "cm.abstract.office")`;

# 3. `string` / `str` handling

## Concatenation
There are tree main ways that you can approach `str` concatenation in CET.

 | Method  | Description | Example | 
 |--|--|--|
| `#` | Easiest way to concatenate strings but not a great option performance wise. | `str w = "Hello" # " World";`| 
| `spnn` | Easily builds up a new `str` by adding values together. | `str w = spnn("Hello", " World");`| 
| `StrBuf` | The best way (performance wise) to build up a new `str` (specially long ones). | ```StrBuf buf(); buff << "Hello" << " World"; pln(buf.toS());```| 


## Helper functions

 | Method  | Description | Example | 
 |--|--|--|
 | `cm.core.settings.coreDistanceToS` | Formats a given `distance` value into a `str` using the user's preferred distance unity | `double v = 1; pln(v.distance().coreDistanceToS();`|
