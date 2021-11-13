# React

React is a JavaScript library for building user interfaces. It is component-based
and uses a diffing algorithm to compare the Virtual DOM with the Real DOM in order
to decide which components to update. 

React is commonly used with JSX to allow for better visualization of the HTML 
elements. `React.createElement(component, props, ...children)` is used to create 
React elements without JSX. 

## Rendering Components

In a class component, the `render()` function will return the React element. 

``` javascript
class DateTime extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <p>
        {new Date().toLocaleString()}
      </p>
    )
  }
}
```

In a functional component, the function itself is equivalent to `render()`.

``` javascript
const DateTime = (props) => (
  <p>
    {new Date().toLocaleString()}
  </p>
)
```

## Components and Props

React components can accept props (i.e properties from parent components). Props 
must not be changed by the component itself; in this sense, React components are 
pure functions. 

Components will re-render when props or state changes. 

``` javascript
const Welcome = (props) => (
  <p>Welcome {props.name}!</p>
);
```

## State and Lifecycle

### State 

State is mutable data that belongs to the component and upon change will trigger
a re-render. The component below will re-render every time the user clicks the 
button because the click event handler will increment the `count` state. 

``` javascript
class ClickCounter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    const { count } = this.state;

    return (
      <div>
        <p>
          {user.name} clicked {count} times!
        </p>
        <button onClick={() => { this.setState(count + 1) }}>Click</button>
      </div>
    );
  }
}
```

State cannot be modified directly; it must be modified with `setState()`.

React may group multiple `setState()` calls into a single update for performance.
Because `props` and `state` can be updated asynchronously, you cannot depend on 
them for setting the next state. 

``` javascript
// This is wrong
this.setState({ count: this.state.count + this.props.increment });

// This is right. The function receives the previous state and the current props
this.setState((state, props) => ({
  count: state.count + props.increment
}));
```

State updates are merged together; the new state passed to `setState()` will 
overwrite only the given keys.

``` javascript
// example
this.state = { count: 3, resets: 5 };
this.setState({ count: 0 });

this.state = { count: 0, resets: 5 };
```

### Lifecycle Methods

Lifecycle methods are special methods that trigger at certain moments of a 
component's lifecycle. Some commonly used ones are `componentDidMount()`, 
`componentDidUpdate()`, and `componentWillUmount()`.

`componentDidMount()` is useful for initializing any state variables perhaps from 
an API response. 

`componentWillUnmount()` is useful for performing any necessary cleanup. 

For more on class components and lifecycle methods, click 
[here](https://reactjs.org/docs/react-component.html).

``` javascript
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = { date: new Date() };
  }

  componentDidMount() {
    this.timerID = setInterval(() => {
      this.setState({ date: new Date() });
    }, 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  render() {
    return (
      <h1>It is now {this.state.date.toLocaleTimeString()}</h1>
    );
  }
}
```

## Handling Events

In React, event handlers are defined on the element itself by passing in a 
function and are named using camel case. 

Click [here](https://reactjs.org/docs/events.html) for more events.

``` javascript
<button onClick={clickedFunction}>Click me!</button>
```

## Hooks

Hooks make React simpler by removing the need to bind context to class functions
and making state variables share the same scope as the returned React element. 

**Hooks must be at the top level and cannot be nested in if statements, loops, or nested functions**

For more hooks, click [here](https://reactjs.org/docs/hooks-reference.html).

### `useState()`

`useState()` is a hook that sets the state to the argument and returns a state 
variable and a function that updates that specific state variable. 

``` javascript
import React, { useState } from 'react';

const Counter = (props) => {
  const [count, setCount] = useState(0);

  return (
    <>
      <p>This is the count: {count}</p>
      <button onClick={() => setCount(count + 1) }>Click me!</button>
    </>
  );
};
```

### `useEffect()`

`useEffect()` is a hook that is used to create side effects. The side effects can 
occur depending on certain data if the hook is passed a second argument. 
Otherwise, `useEffect()` will be called after every render as if using 
`componentDidMount()` and `componentDidUpdate()`.

``` javascript
import React, { useState, useEffect } from 'react';

const Counter = (props) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  }, [count]);

  return <button onClick={() => setCount(count + 1)}>Click</button>;
}
```

#### Cleanup

To use effects with cleanup, you return a cleanup function inside the hook. 

``` javascript
import React, { useState, useEffect } from 'react';

const Clock = (props) => {
  const [date, setDate] = useState(new Date());
  const [timerID, setTimerID] = useState(null);

  useEffect(() => {
    setTimerID(setInterval(() => {
      setDate(new Date());
    }, 1000));

    return function cleanup() {
      clearInterval(timerID);
    }
  }, []);

  return <h1>It is now {date.toLocaleTimeString()}</h1>;
};
```

Passing an empty array as the second argument to `useEffect()` is equivalent to 
`componentDidMount()`. 