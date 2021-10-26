# Angular - Tour of Heroes

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

`*ngIf` is used to conditionally render HTML

`<div *ngIf="selectedHero"></div>`

## Event Handlers

### Click Event

Angular's syntax for binding a click event is like this:
`<li *ngFor="let hero of heroes" (click)="onSelect(hero)">`

This will call the component's `onSelect(hero)` function when clicked. 

## Attribute, Class, Style Binding

### Syntax

`<p> [attr.attribute-you-are-targeting]="expression"></p>`

### Class 

This will set the list item's class to `selected` if `hero === selectedHero`

`<li [class.selected]="hero === selectedHero"></li>`

## Sharing data between components

`@Input()` lets a parent component pass data to a child component

`@Output()` lets a child component pass data to a parent component

Example: 
``` html
<!-- Heroes component passes selectedHero to HeroDetail component as a hero property -->
<app-hero-detail [hero]="selectedHero"></app-hero-detail>
```
``` typescript
import { Component, OnInit, Input } from '@angular/core';
import { Hero } from '../hero';

@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.css']
})
export class HeroDetailComponent implements OnInit {
  @Input() hero?: Hero;
  
  constructor() { }

  ngOnInit(): void {
  }

}
```

## Services

Services are essentially reusable APIs that fetch data for a component.

`@Injectable()` services participate in the dependency injection system, meaning
the system will set the service as a singleton instance. 

``` typescript
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Hero } from './hero';
import { HEROES } from './mock-heroes';

@Injectable({
  providedIn: 'root'
})
export class HeroService {

  constructor() { }

  getHeroes(): Observable<Hero[]> {
    const heroes = of(HEROES);
    return heroes;
  }
}
```
``` typescript
import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {
  heroes: Hero[] = [];
  selectedHero?: Hero;

  constructor(private heroService: HeroService) { }

  ngOnInit(): void {
    this.getHeroes();
  }

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  }

  getHeroes(): void {
    this.heroService.getHeroes()
        .subscribe(heroes => this.heroes = heroes);
  }
}
```

## Routing

`ng generate module app-routing --flat --module=app` 

This command will create a module. `--flat` flag puts the file in `src/app`. 
`--module=app` tells the CLI to import it into `AppModule`

### RouterModule

src/app/app-routing.module.ts
``` typescript 
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HeroesComponent } from './heroes/heroes.component';

const routes: Routes = [
  { path: 'heroes', component: HeroesComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

`RouterModule` and `Routes` lets the application have routing functionality. 
`RouterModule.forRoot(routes)` will configure the router at the application's root level.
The module must import the `RouterModule.forRoot(routes)` and export the 
`RouterModule` to make routes accessible throughout the application. 

### RouterOutlet

`<router-outlet></router-outlet>` can be added to the `AppComponent` template to 
display components that correspond to the routes

### routerLink

To add links and navigate through the application, you can add a `routerLink` 
property to an `a` tag. `<a routerLink="/heroes">Heroes</a>`