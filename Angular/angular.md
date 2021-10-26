# Angular

Angular is a component based frontend framework. 

## Components

`@Component` is a decorator that specifies the Angular metadata for the component 
 * `selector` - the component's CSS element selector
 * `templateUrl` - the location of the component's template file
 * `styleUrls` - the location of the component's private CSS styles

## Lifecycle Hooks

`ngOnInit()` is useful for initialization logic

## Formatting

`uppercase` can be used to format a string to uppercase
 * `<h2>{{hero.name | uppercase}} Details</h2>`

## Directives

`ngModel` binds HTML and class properties two ways so that data transfers between 
both
`<div>
  <label for="name">Hero name: </label>
  <input id="name" [(ngModel)]="hero.name" placeholder="name">
</div>`

You must opt-in to the `FormsModule` in the `@NgModule` decorator to use the 
`ngModel` directive

``` typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HeroesComponent } from './heroes/heroes.component';

@NgModule({
  declarations: [
    AppComponent,
    HeroesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

`*ngFor` is Angular's repeater directive. It repeats the element for each one in
a list

`<li *ngFor="let hero of heroes">`