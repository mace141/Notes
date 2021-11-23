# 1.[TypeScript for JS Programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)

## Types by Inference

TypeScript will infer a variable's type by looking at the variable's value.

``` typescript
let helloWorld = "Hello World";
let helloWorld: string;
// both are defining the string type to helloWorld
```

## Defining Types

There are two syntaxes for building types: `interface` and `type`

You should prefer `interface` over `type` except for specific features

You can explicitly define an object's type using an `interface` declaration

``` typescript
interface User {
  name: string;
  id: number;
}
```

You can also use an `interface` declaration with a class 

``` typescript
interface User {
  name: string;
  id: number;
}

class UserAccount {
  name: string;
  id: number;

  constructor(name: string, id: number) {
    this.name = name;
    this.id = id;
  }
}

const user: User = new UserAccount('Daniel', 141);
```

`Interfaces` can also be used to type parameters and return values to functions

``` typescript
function getAdmin(): User {
  // ...
}

function deleteUser(user: User) {
  // ...
}
```

`declare` is used to tell TypeScript that this object exists already and the
statement doesn't need to be compiled into JavaScript

``` typescript 
declare const user: User;
```

### Types

JavaScript has a small set of primitive types: 
* `boolean`
* `bigint`
* `number`
* `string`
* `null`
* `symbol`
* `undefined`

TypeScript adds a few more types to this list:
* `any` - allow anything
* `never` - specified type is not possible
* `unknown` - ensure someone using this type declares what the type is
* `void` - a function that returns `undefined`

## Complex Types

You can declare complex types by combining simple ones using unions or generics

### Unions

Unions allow you to declare multiple types or values

``` typescript
type myBool = true | false;
type WindowStates = "open" | "closed" | "minimized";
type LockStates = "locked" | "unlocked";
type PositiveOddNumbersUnderTen = 1 | 3 | 5 | 7 | 9;
```

### Generics

Generics provide variables to types. They are commonly used with arrays to declare 
the array's contents

``` typescript
type StringArray = Array<string>;
type NumberArray = Array<number>;
type ObjectWithNameArray = Array<{ name: string }>;
```

## Structural Type System

TypeScript checks values to see if it matches the expected shape of the value. 

``` typescript 
interface Point {
  x: number;
  y: number;
}

function logPoint(p: Point) {
  console.log(`${p.x}, ${p.y}`);
}

const point = { x: 0, y: 2 };
logPoint(point);
```

The `point` variable was not declared to be a `Point` type but `logPoint` checked
the argument's shape and validated its type

Shape matching only requires a subset of properties to match

``` typescript 
const point3 = { x: 12, y: 26, z: 89 };
logPoint(point3); // logs "12, 26"
 
const rect = { x: 33, y: 3, width: 30, height: 80 };
logPoint(rect); // logs "33, 3"
 
const color = { hex: "#187ABF" };
logPoint(color);
// Argument of type '{ hex: string; }' is not assignable to parameter of type 'Point'.
//   Type '{ hex: string; }' is missing the following properties from type 'Point': x, y
```

Objects and classes in TypeScript follow the same structural typing rules. If an
object and class have the required properties, TypeScript will say the types match

``` typescript
class VirtualPoint {
  x: number;
  y: number;
 
  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}
 
const newVPoint = new VirtualPoint(13, 56);
logPoint(newVPoint); // logs "13, 56"
```

# 2. [The Basics](https://www.typescriptlang.org/docs/handbook/2/basic-types.html)

## `tsc`, the TypeScript Compiler

After installing TypeScript, you can check a TypeScript file's types and compile
it into a JavaScript file. To do so, you run `tsc filename.ts` in your terminal.
If there are no errors, it will create a JavaScript file. If there are errors, 
they will be visible in the terminal. 

## Erased Types & Downleveling

The compiled JavaScript will not have type annotations and will be in ES3 by 
default. You can specify the version by running the compiler with `--target es2015`. 
For example, `tsc --target es2015 hello.ts`.

## Strictness

TypeScript allows you to vary the level of strictness by turning on flags. 
Turning on the strict flag in the CLI or `"strict": true` in tsconfig.json will
toggle them all on. The two most important ones are `noImplicitAny` and 
`strictNullChecks`

noImplicitAny - variables whose type is inferred as `any` will be issued an error

strictNullChecks - makes handling `null` and `undefined` more explicit

### Non-null Assertion Operator (`!`)

Adding a `!` after any expression will assert that the value is not `null` or
`undefined`.

``` typescript
function runtimeRoulette(x?: number | null) {
  // No error while compiling
  console.log(x!.toFixed());
}
```

# 3. [Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

## Primitive Types

`string` - string values like `"Hello, world"`

`number` - numbers like `141`. There is no `int` or `float`, everything is a `number`

`boolean` - for `true` and `false`

## Arrays

To specify an array like `[1, 2, 3]`, you can use the syntax `number[]` or 
`Array<number>`

## `any`

TypeScript's `any` is used when you don't want a value to cause typechecking errors.
When a value's type is `any` you can do anything JavaScript can do with it. 

## Type Annotations on Variables

Type annotations are always on the right of what is being typed. However, in most
cases this isn't needed because TypeScript will infer the type based on the value.

``` typescript
let myName: string = 'Daniel';

// myName is inferred as type 'string'
let myName = 'Daniel';
```

## Functions

Both the input and the output of functions can be typed. 

``` typescript
function greet(name: string): string {
  return `Hello ${name}`;
}
```

### Anonymous Functions

TypeScript uses contextual typing to determine the type of a variable in 
anonymous functions

``` typescript
const names = ['Daniel', 'Lily', 'ChocoPie'];

// Contextual typing
names.forEach((s) => {
  console.log(s);
});
```

## Object Types

Object types are defined by listing the properties and their types. 

``` typescript
// Properties can be separated with either `,` or `;`
function logCoordinates(pt: { x: number; y: number }) {
  console.log(`X: ${pt.x}, Y: ${pt.y}`);
}
```

### Optional Properties

Some properties may be optional and can be declared as such by adding a `?` after
the property name.

``` typescript
function logFullName(person: { first: string, middle?: string, last: string }) {
  // ...
}
```

Because a property may not exist on the object, you have to check for `undefined`
before using it. 

``` typescript
let person: { first: string, middle?: string, last: string } = { first: 'Daniel', last: 'Wu' };

// Okay
if (person.middle !== undefined) {
  console.log(person.middle.toUpperCase());
}

// Modern
console.log(person.middle?.toUpperCase());
```

Adding a `?` to the right of a property in a method chain is called **optional 
chaining**. It prevents runtime errors from occuring and will return `undefined` 
if the property does not exist. 

## Union Types

Types can be combined using the `|` operator to form more complex types called a
union. A union is formed from two or more *members* (types in the union). 

Some methods are not available to every member which require us to *narrow* the 
code. The code below is narrowed by the conditional statements. 

``` typescript
function printId(id: number | string) {
  if (typeof id === 'number') {
    console.log(id);
  } else {
    console.log(id.toUpperCase());
  }
}
```

## Type Aliases

Type aliases are great for creating a type object that can be used multiple times.
They can be used to define object types and union types. 

``` typescript
type Point = {
  x: number,
  y: number
};

type ID = number | string;
```

## Interfaces

An interface declaration is another way to define an object type. 

``` typescript
interface Point {
  x: number,
  y: number
}
```

### Type Aliases vs Interfaces

Type aliases and interfaces are very similar and are often times used interchangeably,
but type aliases cannot be mutated. 

Extending an interface
``` typescript
interface Animal {
  name: string  
}

interface Bear extends Animal {
  honey: boolean
}
```

Extending a type via intersections
``` typescript
type Animal = {
  name: string
}

type Bear = Animal & {
  honey: boolean
}
```

## Type Assertions

When you know the type better than TypeScript, you can assert a type to specify 
the type. 

For example, when you query for an HTMLElement using `document.getElementById`
TypeScript knows that it will return some type of  `HTMLElement` but not which one. 
However, you can assert which type it will be which will allow you to use methods
defined on the specified type. 

``` typescript
const myInput = document.getElementById('my-input') as HTMLInputElement;
// No problems doing this due to the type assertion
console.log(myInput.value);
```

>Be careful using type assertions because they are removed at compile-time which
>means there won't be runtime checking or an exception if the assertion is wrong.

Type assertions can only be made to a *more specific* or *less specific* type. 

## Literal Types

On top of specifying a type, TypeScript allows you to specify a literal type. 
Literal types are not very useful by themselves, but are much more useful when
combining literals into unions. You can also combine non-literals with literals. 

``` typescript
let greeting: 'hello' = 'hello';

// This will cause an error because `greeting` has a literal type of 'hello' 
greeting = 'hi';

const greetings: string | 'hello' | 'hi' | 'how are you' = 'hello';
```

### [Literal Inference](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-inference)

When you initialize a variable with an object, TypeScript will infer the types and
assume the values may change later. If you want to assign a literal type to the 
object, then you can use type assertion. The suffix `as const` will convert the 
entire object to literal types. 

``` typescript
const req = { url: 'https://example/com', method: 'GET' } as const;
handleRequest(req.url, req.method);
```