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
`boolean`
`bigint`
`number`
`string`
`null`
`symbol`
`undefined`

TypeScript adds a few more types to this list:
`any` - allow anything
`never` - specified type is not possible
`unknown` - ensure someone using this type declares what the type is
`void` - a function that returns `undefined`

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
