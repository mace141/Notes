# $$$$$$$$$$$$$$$$$$$$$$$$$ W6D3 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ What is an API? ]]]]]]]]]]]]]]]]]]]]]]]]]

# Application Programming Interface
    # i.e API of a Ruby object are the public methods

# API of a website are the HTTP routes

# Website includes assets to be rendered by the browser
# Webservice (API) - just data
    # i.e, mobile app, server2server, client side rendering of data(Single Page Application SPA)

# [[[[[[[[[[[[[[[[[[[[[[[[[ HTTP Request/Response ]]]]]]]]]]]]]]]]]]]]]]]]]

# HTTP Request goes from CLIENT to SERVER
    # method (GET, PUT, PATCH, POST, DELETE)
    # path (/users/path/)
    # query (?loc=NY&name=daniel)
    # body - additional data which can come from smth like a form. cannot be part of a GET request

# HTTP Response goes from SERVER to CLIENT
    # status - represented by numeric codes (200 OK, 404 NOT FOUND)
    # body - main response

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rails Routing ]]]]]]]]]]]]]]]]]]]]]]]]]

#https://open.appacademy.io/learn/swe-in-person/rails/routing-i--basics

# ROUTERs define your applications API - valid paths and methods

# When an HTTP request is sent to a Rails SERVER, it first makes contact with the ROUTER
    # which sends the request to the appropriate CONTROLLERS based on PATH & METHOD. The ROUTER
    # also tells the CONTROLLER how to do its job. 

# When the router matches the PATH & METHOD: 
    # check routes.rb
    # initialize the corresponding controller
    # call the appropriate actions on the controller

# The controller creates the RESPONSE and sends it back to the CLIENT

# ========================= Routes =========================
=begin
# Route syntax are typically like this: HTTP method, route, CONTROLLER method
    # i.e, get 'superheroes', to: 'superheroes#index'
    
# ------------------------- Resource Routes -------------------------
    
# REST: Representational State Transfer
    # convention for routes syntax

   HTTP Verb   |        Path       |   action   | used for
---------------|-------------------|------------|----------------------------------------------
GET	           | /photos	       |   index	| display a list of all photos
GET	           | /photos/new	   |   new	    | return an HTML form for creating a new photo
POST	       | /photos	       |   create	| upload and create a new photo
GET	           | /photos/:id	   |   show	    | display a specific photo
GET	           | /photos/:id/edit  |   edit	    | return an HTML form for editing a photo
PATCH or PUT   | /photos/:id	   |   update	| update a specific photo
DELETE	       | /photos/:id	   |   destroy  | delete a specific photo

# Rails allows us to create all these routes using this method
    # resources :superheroes, only: [:index, :show, :create, :update, :destroy]
=end

Rails.application.routes.draw do
  # Collection Route
  resources :superheroes do
      resources :abilities, only: [:index]
  end
  # Member Route
  resources :abilities, only: [:show, :update, :create, :destroy]
  # This allows the GET / , root URL, request to invoke superheroes#index 
  root to: 'superheroes#index'
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Controllers ]]]]]]]]]]]]]]]]]]]]]]]]]

# Postman is a tool used to test our API 

## rails s
# starts the rails server

# Controller file names must be camel_case: superheroes_controller.rb
# Controllers are always plurally named 
# get 'superheroes', to: 'superheroes#fun'
class SuperheroesController < ApplicationController
  # def fun
  #     render text: 'Hello'
  # end

  def fun         # params is a hash of key:value pairs
      render json: params
  end
end

# Parameters can come from THREE places:
  #1 Query string
      # github.com/mace141/repos?name=W6D3
          # params = {action: show, controller: mace141, name: W6D3}
  #2 Request body
  #3 URL params/Route params (wildcards)
      # github.com/mace141/141
          # params = {action: show, controller: mace141, id: 141}

## bundle exec rake routes
# shows the routes that can be taken

# ========================= Strong Parameters =========================
=begin 
# There are three kinds of parameters possible in a web application: 
  query string, request body, & route fragment

# Rails will mix the three into a single #params method

# We may have used mass assignment previously but we can't do that here because we want to 
  restrict which parameters a user assign

# params has some built in methods to passlist (list of allowed elements) certain attributes
  for mass assignment. both methods take in attribute names as symbols
  # require()
  # permit()

params.require(:superhero).permit(:power, :secret_identity)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Delegation ]]]]]]]]]]]]]]]]]]]]]]]]]

<%= @patient.doctor.name %>
<%= @patient.doctor.specialty %>
<%= @patient.doctor.office.number %>
<%= @patient.doctor.office.address %>

# This violates the Law of Demeter! We can prevent this by using DELEGATION to assign methods

def doctor_name 
  doctor.name
end

<%= @patient.doctor_name %>

# Writing getters is fine, but we can do better by using the delegate method
=end
class Office < ApplicationRecord
  belongs_to :doctor
end

class Doctor < ApplicationRecord
  has_one :office
  has_many :patients
  delegate :number,
      :address,
      to: :office,
      prefix: true
end

class Patient < ApplicationRecord
  belongs_to :doctor
  delegate :name,
      :specialty,
      :office_number,
      :office_address,
      to: :doctor,
      prefix: true
end

# <%= @patient.doctor_name %>
# <%= @patient.doctor_specialty %>
# <%= @patient.doctor_office_number %>
# <%= @patient.doctor_office_address %>

=begin
# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ HTTP ]]]]]]]]]]]]]]]]]]]]]]]]]

# HTTP:
  protocol for communication over the internet
  clients and servers communicate via messages (requests & responses)
  HTTP requests are just strings
  HTTP defines how requests & responses are formatted and transmitted

# HTTP Request has four components:
  # Mandatory components
      # Method (verbs)
      # Path
  # Optional components
      # Query string
      # Body

# ========================= Anatomy of a URL =========================

protocol, domain,       path,      query string

http://   google.com/   search?    query=dogs

# ========================= HTTP Request Methods =========================

# GET
# POST
# PATCH/PUT
# DELETE

# ========================= HTTP Response Components =========================

# Status 
  # numeric indication of type of response (successful/failure)
  # look to wikipedia for standard status codes (200 OK, 404 Not found)
  # Know these for now: 200, 302, 422
# Body
  # data/content responded by the server
  # can be an HTML document, or data formatted as JSON

# [[[[[[[[[[[[[[[[[[[[[[[[[ Router ]]]]]]]]]]]]]]]]]]]]]]]]]

# Rails ROUTER receives an HTTP request and decides which controller to send the request. 
  ROUTER instantiates an instance of the controller and invokes an action based on 
  the request components

REST is a standardized way to interpret an HTTP Request and extrapolate the desired
  response from the server. It maps HTTP verbs to CRUD actions

POST        -> Create
GET         -> Read
PATCH/PUT   -> Update
DELETE      -> Destroy

# RESTful routes:

 HTTP Verb   |        Path       |   action   |         used for
---------------|-------------------|------------|----------------------------------------------
GET	           | /photos	       | index	    | display a list of all photos
GET	           | /photos/new	   | new	    | return an HTML form for creating a new photo
POST	       | /photos	       | create	    | upload and create a new photo
GET	           | /photos/:id	   | show	    | display a specific photo
GET	           | /photos/:id/edit  | edit	    | return an HTML form for editing a photo
PATCH or PUT   | /photos/:id	   | update	    | update a specific photo
DELETE	       | /photos/:id	   | destroy    | delete a specific photo
=end
# ========================= Setting Up Routes =========================

# Generate 8 standard RESTful routes

resources :photos

# You may add ONLY or EXCEPT options to include/exclude certain actions
  # the array must contain ACTION names, not method names

resources :photos, only: [:create, :destroy]

resources :photos, except: [:create, :destroy]

# Create a custom route in routes.rb

get 'photos', to: 'photos#index'

## bundle exec rails server
# open the rails server

## bundle exec rails routes
# displays routes

Rails.application.routes.draw do 
  # for custom/manual routes
  get "/songs", to: "songs#index"

  # easy way for all standard RESTful routes
  resources :songs
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Controller ]]]]]]]]]]]]]]]]]]]]]]]]]

# Takes in HTTP Requests, decides what to do with them & how to respond

# ========================= Params =========================

## params is a method that returns the information from the request

# THREE ways to populate params in an HTTP request
  # Wildcards - inside a route. i.e, /users/:id
  # Query string - /path?param1=value1&param2=value2
  # Request body - usually built using a form
      # avoid this for GET requests

# Controller actions must either RENDER or REDIRECT

class SongsController < ApplicationController
  def index
      songs = Song.all 
      render json: songs 
  end

  def show 
      song = Song.find(params[:id])
      render json: song 
  end

  def create 
      song = Song.new(song_params)
      if song.save 
          render json: song 
      else
          render json: song.errors.full_messages, status: 422
      end
  end

  def update 
      song = Song.find(params[:id])
      if song.update(song_params)
          # redirect_to needs a url helper to redirect the user to another path
          # this will redirect to #show
          redirect_to song_url(song)  # or song_url(song.id)
      else
          render json: song.errors.full_messages, status: :unprocessable_entity # same as 422
      end
  end

  def destroy 
      song = Song.find(params[:id])
      song.destroy 
      # this will redirect to #index 
      redirect_to songs_url
  end

# ------------------------- Strong Params -------------------------
# Strong parameters is when you write a method to dictate access to attributes
  private

  def song_params
      params.require(:song).permit(:body, :author_id)
  end
end

# add this to ApplicationController 
class ApplicationController < ActionController::Base 
  skip_before_action :verify_authenticity_token
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W6D4 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Callbacks ]]]]]]]]]]]]]]]]]]]]]]]]]
=begin
# Callbacks are methods that get called whenever an object is created, saved,
    updated, deleted, validated, or loaded from the database.

# ========================= Relational Callbacks =========================

# Supposed a User has many posts, when the user is deleted, so should the user's posts
    (otherwise, the posts are WIDOWED). We can do this by passing the :dependent option 
    to has_many. 
        # has_many :posts, dependent: :destroy

# dependent: :destroy/:nullify will help prevent widows but they dont prevent 
    invalid foreign key values (i.e, -1). Also if a record is DELETEd thru SQL,
    Rails won't protect against the error

# To ensure Referential Integrity, you have to add constraints at the DB level. 

# Common Callbacks
    # before_validation
    # after_create
    # after_destroy

# You can be even more specific with callbacks by specifying the cue method

before_validation(on: :create) do 
    ... code here
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Domain Name System Overview ]]]]]]]]]]]]]]]]]]]]]]]]]

# Domain Name System (DNS)

# ========================= Domain Names =========================

# Domain labels are heirarchically ordered from right to left
    # www.google.com - google is a subdomain of com

# ========================= Name Servers & Revolvers =========================

# There are name servers for each domain that delegate authority for a subdomain
    to another name server. The opposite of a name server (holds info) is a DNS revolver. 

# DNS revolvers query for IP addresses and cache recent/popular results

# ========================= Querying for a Domain Name =========================

# Recursive case: when the name server doesn't have all the information locally and must
    pass the query onto another name server

# Iterative case: when the name server returns its best guess as to what other name server
    has the appropriate information and returns the IP address to the original resolver
    
# [[[[[[[[[[[[[[[[[[[[[[[[[ JSON API ]]]]]]]]]]]]]]]]]]]]]]]]]

# The key to building a Rails API is to have the controllers convert model objects 
    into JSON and then return the JSON. 

## to_json 
# converts into JSON string. works on both collections and individual objects

## render json:
# will render the object as json by calling to_json under the hood 
=end
# [[[[[[[[[[[[[[[[[[[[[[[[[ Nested Collections ]]]]]]]]]]]]]]]]]]]]]]]]]

# app/models/magazine.rb
class Magazine < ApplicationRecord
  has_many :articles
end

# app/models/article.rb
class Article < ApplicationRecord
  belongs_to :magazine
end

# config/routes.rb
NewspapersApp::Application.routes.draw do
  resources :magazines do
      # provides a route to get all the articles for a given magazine.
      resources :articles, only: :index
  end
  # generates a /magazines/:magazine_id/articles route

  # provides all seven typical routes
  resources :articles
end

class ArticlesController
  def index
      if params.has_key?(:magazine_id)
          # index of nested resource
          @articles = Article.where(magazine_id: params[:magazine_id])
      else
          # index of top-level resource
          @articles = Article.all
      end
  
      render json: @articles
  end
end

# Collection Routes:
# index: GET /magazines/:magazine_id/articles
# new: GET /magazines/:magazine_id/articles/new
# create: POST /magazines/:magazine_id/articles

# Member routes
# show: GET /magazines/:magazine_id/articles/:id
# edit: GET /magazines/:magazine_id/articles/:id/edit
# update: PUT /magazines/:magazine_id/articles/:id
# update: PATCH /magazines/:magazine_id/articles/:id
# destroy: DELETE /magazines/:magazine_id/articles/:id

# As a general rule, NEVER generate any of the member routes when nesting. 
  # Member routes should only belong to top level resources. 

# Nested #index routes are good. Nested #create routes are bad. Nested #new route = OK

# [[[[[[[[[[[[[[[[[[[[[[[[[ Non-Default Routes ]]]]]]]]]]]]]]]]]]]]]]]]]

# Adding Member Routes - add a member block into the resource block

resources :photos do
  member do
      get 'preview'
  end
end

# A GET request for /photos/1/preview will be routed to the preview action of 
  # PhotosController. It will also create a preview_photo_url helper.

# Adding Collection Routes 

resources :photos do
  collection do
      get 'search'
  end
end

# This enables rails to recognize paths such as /photos/search with GET, and route
  # to the search action of PhotosController. Also creates search_photos_url helper

# $$$$$$$$$$$$$$$$$$$$$$$$$ W6D5 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rails Views ]]]]]]]]]]]]]]]]]]]]]]]]]

# View files should be named as the controller action - index.html.erb
    # erb stands for embedded Ruby - allows the html to use Ruby code

# Instead of rendering json: code_here, we can now render the View file

def index 
  # use instance variables because the View has access to these variables
  @books = Book.all 
  render :index 
end

# In order to use ruby code in the index.html.erb file we have to use certain brackets

<% ruby code that will not be printed %>
<%= ruby code that we want to render %>

# ------------------------- Index -------------------------

<ul>
  <% @books.each do |book| %>                                                                                         >
      <a href="<%= book_url(book) %>"> <li><%= book.title %></li> </a>               
  <% end %>
</ul>

# You do not need to write the head section in the View files because they inherit
  # from the application.html.erb. This is where you write html that will be inherited

# ========================= Forms =========================

# ------------------------- New -------------------------

# The New action is used to return a form to the user in order to Create something

# We want to store our form in the new.html.erb file

# action: URL for where we are sending data
# method: HTTP method/verb
<form action="/books" method="post">
              # <% books_url %> can replace /books
  <label for="title">Title</label>
  <input id="title" type="text" name="book[title]">     
                              # name's value will be the key in params in controller
  <br>    # breakline for html

  <label for="author">Author</label>
  <input id="author" type="text" name="book[author]">     

  <br>

  <label for="year">Year</label>
  <input id="year" type="text" name="book[year]">     
                  # type="date" will allow the user to select dates from a calendar
  <br>
  # select tag is used for dropdowns
  <label for="category">Category</label>
  <select id="category" name="book[category]">
      # disabled will prevent the user from submitting the option. selected makes it act as default
      <option disabled selected>-- Please select --</option>
      <option value="Fiction">Fiction</option>
      <option value="Non-Fiction">Non-Fiction</option>
      <option value="Memoir">Memoir</option>
  </select>

  <br><br>

  <label for="description">Description</label>
  <textarea name="book[description]"></textarea>

  <input type="submit" value="Add book to library">
      # input type="submit" makes a button
</form>

# ------------------------- Edit -------------------------

def edit 
  @book = Book.find_by(id: params[:id])   # prefer find_by because not found 
  render :edit                            # will return nil rather than raise error
end

def update 
  @book = Book.find_by(id: params[:id])
  
  if @book.update_attributes(book_params) # update_attributes will update, save and return a boolean
      redirect_to book_url(@book)
  else
      render :edit 
  end
end

<form action="<% book_url(@book) %>" method="post"> # cannot put PATCH but we can work around
  <input type="hidden" name="_method" value="PATCH">       # using a hidden input

  <label for="title">Title</label>
  <input id="title" type="text" name="book[title]" value="<%= @book.title %>">     
                                                  # this will render the title in the input box
  <br>    

  <label for="author">Author</label>
  <input id="author" type="text" name="book[author]" value="<%= @book.author %>">     

  <br>

  <label for="year">Year</label>
  <input id="year" type="text" name="book[year]" value="<%= @book.year %>">     

  <br>

  <label for="category">Category</label>
  <select id="category" name="book[category]">
      <option disabled>-- Please select --</option>
                              # use ternary logic to add selected to the option
      <option value="Fiction" <%= @book.category == "Fiction" ? "selected" : "" %> >Fiction</option>
      <option value="Non-Fiction" <%= @book.category == "Non-Fiction" ? "selected" : "" %> >Non-Fiction</option>
      <option value="Memoir" <%= @book.category == "Memoir" ? "selected" : "" %> >Memoir</option>
  </select>

  <br><br>

  <label for="description">Description</label>
  <textarea name="book[description]">
      <%= @book.description %>    
  </textarea> # this will render the book's description

  <input type="submit" value="Update book">
</form>

# ========================= Partials =========================

# https://open.appacademy.io/learn/swe-in-person/rails/partials

# Copying the code from new.html.erb to edit.html.erb is not very DRY. What we 
  # should do is use PARTIALS which essentially allows views to inherit a template

# Partial file names are denoted with an underscore before the name
  # i.e, _form.html.erb

def new 
  @book = Book.new    # you don't want to pass in any parameters so this @book instance is a dummy
  render :new             # that is used for the partials
end

# Add this to the view files you want to inherit the template
<%= render 'form', book: @book, action: :edit % >                                                                        

# Add this to the partial
<% if action == :edit % >                                                                                                
  <% action_url = book_url(book) % >
<% else % >
  <% action_url = books_url % >
<% end % >                                                                                                               

<form action="<% action_url %>" method="post"> # cannot put PATCH but we can work around
  # if action == :edit, then insert that html         # using a hidden input
  <% if action == :edit % >                                                                                            
      <input type="hidden" name="_method" value="PATCH">       
  <% end % >                                                                                                           
  <label for="title">Title</label>
  <input id="title" type="text" name="book[title]" value="<%= book.title %>">     
                                                  # this will render the title in the input box
  <br>    

  <label for="author">Author</label>
  <input id="author" type="text" name="book[author]" value="<%= book.author %>">     

  <br>

  <label for="year">Year</label>
  <input id="year" type="text" name="book[year]" value="<%= book.year %>">     

  <br>

  <label for="category">Category</label>
  <select id="category" name="book[category]">
                          # use ternary logic to check if action is new or edit
      <option disabled <%= book.category ? "" : "selected" %> >-- Please select --</option>
                              # use ternary logic to add selected to the option
      <option value="Fiction" <%= book.category == "Fiction" ? "selected" : "" %> >Fiction</option>
      <option value="Non-Fiction" <%= book.category == "Non-Fiction" ? "selected" : "" %> >Non-Fiction</option>
      <option value="Memoir" <%= book.category == "Memoir" ? "selected" : "" %> >Memoir</option>
  </select>

  <br><br>

  <label for="description">Description</label>
  <textarea name="book[description]">
      <%= book.description %>    
  </textarea> # this will render the book's description
                              # use ternary for button text
  <input type="submit" value="<%= action == :edit ? 'Update book' : 'Add book' %>">
</form>

# ------------------------- Index -------------------------

# _book.html.erb
<li>
  <%= book.title %> by <%= book.author %>
</li>

# index.html.erb
<ul>
  <%= render @books % >                                                                                                
</ul>
# that will iterate through books and call render 'book', book: book

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rails Parameters ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/rails/rails-parameter-conventions

# If you want Rails to build an array, you can do this

<input name="person[phone_numbers][]" type="text" value="555-123-4567">
<input name="person[phone_numbers][]" type="text" value="555-765-4321">
<input name="person[phone_numbers][]" type="text" value="555-135-2468">

{ 'person' => {
  'phone_numbers' => [
      '555-123-4567',
      '555-765-4321',
      '555-135-2468'
    ]
  }
}

# You cannot create an array of hashes, but you can do this

<input name="persons[0][phone_number]" type="text" value="555-123-4567">
<input name="persons[1][phone_number]" type="text" value="555-765-4321">
<input name="persons[2][phone_number]" type="text" value="555-135-2468">

{ 'persons' => {
    '0' => { 'phone_number' => '555-123-4567' },
    '1' => { 'phone_number' => '555-765-4321' },
    '2' => { 'phone_number' => '555-135-2468' }
  }
}

# $$$$$$$$$$$$$$$$$$$$$$$$$ W7D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Authorization ]]]]]]]]]]]]]]]]]]]]]]]]]

# Cookies <= 4 kb data. Cookies are stored on the client side as a hash of data.
# Cookies are sent in the HEADER of the HTTP request

# Session token: proof of login at the current time

# A session token is given each time you log in and removed from your data once
    # you log out

# ASCII is a common character encoding, which includes english letters, numbers,
    # and punctuation symbols 

# Encoding is used to maintain data usability between applications
# Encryption is used for data confidentiality by using a key and an encryption algo

# Hashing for authentication means keeping the result of the password hash on the 
    # database and comparing hash function outputs rather than the password directly

# Cryptographic hashing functions are preferred for security - low chance of collision

# Salting is the adding of a random string to a password, which will then be hashed

# [[[[[[[[[[[[[[[[[[[[[[[[[ BCrypt ]]]]]]]]]]]]]]]]]]]]]]]]]

# require 'bcrypt'

# BCrypt stores the salt and the hash together in one string

# ========================= Class Methods =========================

# BCrypt::Password.create("password")

## BCrypt::Password.new("bcrypted_password_as_string")
# will convert the string back into an instance of BCrypt::Passsword

# ========================= Instance Methods =========================

## version
# version of bcrypt used

## cost
# number of hash iterations

## salt
# return salt portion of the BCrypt::Password

## checksum
# returns the password digest without the salt

## is_password?("password")
# checks if password matches the encryption

# [[[[[[[[[[[[[[[[[[[[[[[[[ Session & Flash ]]]]]]]]]]]]]]]]]]]]]]]]]

# Session is a hash of your cookies used in Rails. The keys and values should be
    # short because they are stored on the server

# Flash is a Rails type of cookie that is stored until the next request
    # It is frequently used for error messages
    # Flash.now isn't a cookie, but is a hash of this request's data

# [[[[[[[[[[[[[[[[[[[[[[[[[ Authentication Pattern ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= User Model =========================

class User < ApplicationRecord 
  validates :username, :session_token, presence: true, uniqueness: true 
  validates :password_digest, presence: {message: "Password can't be blank"}
  validates :password, length: { minimum: 6, allow_nil: true }
  # This will make sure users enter a password of at least 6 characters and allow
      # password to be nil when pulled out of a database
  before_validation :ensure_session_token # when you run #save. (after_initialization => after #new)

  attr_reader :password

  def self.find_by_credentials(username, password)
      user = User.find_by(username: username)
      return user if user && BCrypt::Password.new(user.password_digest).is_password?(password)
      nil 
  end

  def self.generate_session_token 
      SecureRandom::urlsafe_base64
  end

  def reset_session_token!
      self.session_token = User.generate_session_token
      self.save!
      self.session_token
  end

  def ensure_session_token 
      self.session_token ||= User.generate_session_token
  end

  def password=(password)
      @password = password
      self.password_digest = BCrypt::Password.create(password)
  end
  # We have to overwrite the password= method because we don't want to store 
      # the actual password, but instead we want to store the encrypted password
end

# We'll also need behavior for generating, ensuring, and resetting session tokens.

# ========================= Controllers =========================

# UsersController
  # new => register/signup
  # create => create user and login

# SessionsController
  # new => log-in form
  # create => logs in
  # destroy => logs out

# ApplicationController
  # current_user => use session token to determine who current user is
      # use ||= to store the current user to avoid repetitive lookups 
  # login!(user) => plants session token into the session
  # logged_in? => checks if user is logged in

# [[[[[[[[[[[[[[[[[[[[[[[[[ CSRF & Forms ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/rails/csrf-and-forms

# Cross-Site Request Forgery: issuing of an unintended request to another website

# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

# Rainbow table attack: table of different passwords and their hash result

# 3 Key Authorization Functionalities
  # Sign up
  # Log in
  # Log out

# Sign up
  # new & create are required controller actions/routes

# Relevant Routes for Login
resource :session, only: [:new, :create]    # resource singular!

class SessionsController < ApplicationController
  before_action :require_logged_out, only: [:new, :create]
  # we dont want users who are logged in to try to login again
  before_action :require_logged_in, only: [:destroy]
  # we only want logged in users to logout

  def new 
      @user = User.new 
      render :new 
  end

  def create 
      @user = User.find_by_credentials(params[:user][:username], params[:user][:password])
      if @user
          login!(@user)
          redirect_to user_url
      else
          render :new
      end
  end

  def destroy 
      logout!
      redirect_to new_session_url
  end

  def logout! 
      current_user.reset_session_token! if logged_in?     # reset token on database
      session[:session_token] = nil       # reset session_token on client side
      @current_user = nil 
  end
end

class User < ApplicationRecord 
  validates :username, :session_token, presence: true, uniqueness: true 
  validates :password_digest, presence: {message: "Password can't be blank"}
  validates :password, length: { minimum: 6, allow_nil: true }
  # This will make sure users enter a password of at least 6 characters and allow
      # password to be nil when pulled out of a database
  before_validation :ensure_session_token # when you run #save. (after_initialize => after #new)

  before_action :require_logged_out, only: [:new, :create]
  # we dont want users who are logged in to try to sign up again
  before_action :require_logged_in, only: [:index, :show]
  # we only want users who are logged in to access the main part of our app

  attr_reader :password

  def self.find_by_credentials(username, password)
      user = User.find_by(username: username)
      if user && user.is_password?(password)
          user 
      else
          nil 
      end
  end

  def self.generate_session_token 
      SecureRandom::urlsafe_base64
  end

  def password=(password)
      @password = password
      self.password_digest = BCrypt::Password.create(password)
  end
  # We have to overwrite the password= method because we don't want to store 
      # the actual password, but instead we want to store the encrypted password

  def reset_session_token!
      self.session_token = User.generate_session_token
      self.save!
      self.session_token
  end

  def ensure_session_token 
      self.session_token ||= User.generate_session_token
  end

  def is_password?(password)
      password_object = BCrypt::Password.new(self.password_digest)
      password_object.is_password?(password)
  end
end

class ApplicationController < ActionController::Base 
  skip_before_action :verify_authenticity_token   # built-in to skip before action
  helper_method :current_user, :logged_in?        # allows views to use these methods

  def login!(user)
      session[:session_token] = user.reset_session_token
  end

  def current_user
      @current_user ||= User.find_by(session_token: session[:session_token])
  end

  def logged_in?
      !!current_user  # !! converts object to strict boolean data type
  end

  def require_logged_in
      redirect_to new_session_url unless logged_in?
      # send user to the login form if they are trying to perform 
          # an action that requires them to be logged in
  end

  def require_logged_out
      redirect_to users_url if logged_in?
      # send user to the users index (home page) if they are trying to perform
          # an action that requires them to be logged out
  end
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W7D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ CSRF ]]]]]]]]]]]]]]]]]]]]]]]]]

# Cross Site Request Forgery: issuing of an unintended request to another website

<input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>">
# add this to your form tag

protect_from_forgery with: :exception
# add this to the application controller

# [[[[[[[[[[[[[[[[[[[[[[[[[ Radio Button ]]]]]]]]]]]]]]]]]]]]]]]]]

<% Cat::COAT_COLORS.each do |coat_color| %>
    <label>
        <input type="radio" 
               name="cat[coat_color]" 
               value="<%= coat_color %>"
               <%= "checked" if cat.color == coat_color %>>
               # will select the radio button if chosen previously
        <%= coat_color.upcase %>
    </label>
<% end % >

# [[[[[[[[[[[[[[[[[[[[[[[[[ Text Area ]]]]]]]]]]]]]]]]]]]]]]]]]

<label for="cat_description">Description</label>
<textarea name="cat[description]" id="cat_description"><%= cat.description % ></textarea>

# [[[[[[[[[[[[[[[[[[[[[[[[[ Helper Functions ]]]]]]]]]]]]]]]]]]]]]]]]]

# Let's say we wanted to display a truncated description next to the cat's name
    # We can then do this:
<%= cat.name % > (<%= cat.description.slice(0, 20) % ><%= "..." if cat.description.length < 20 % >)
# However, it's better to use a helper method because the code can get very long

<%= cat_link(cat) % >

# app/helpers/application_helper.rb
module ApplicationHelper
    def cat_link(cat)
        short_description = cat.description.slice(0, 20)
        short_description += "..." if cat.description.length > 20

        html = "<a href=\"#{cat_url(cat)}\">"
        html += "#{h(cat.name)} (#{h(short_description)})"
        html += "</a>"

        html.html_safe 
        # html_safe protects the page from being injected with scripts
            # without this, it will print  
        # h() escapes the input 
    end
end

# Link tag shortcut

<%= link_to "New Cat!", new_cat_url % >

# Button tag shortcut

<%= button_to "Destroy Cat!", cat_url(cat), method: :delete % >

# Capture blocks of code (html/ruby)

capture(&block)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Layouts ]]]]]]]]]]]]]]]]]]]]]]]]]

# Here's how to use content_for

# application.html.erb

<footer>
    <p>This site is property of 99 Cats.</p>
    <%= yield :footer % >
</footer>

# show.html.erb

<% content_for :footer do % >
    This is a cat show page. 
<% end % >

# [[[[[[[[[[[[[[[[[[[[[[[[[ ActionMailer ]]]]]]]]]]]]]]]]]]]]]]]]]

# ActionMailer allows us to send mails from our application. It works like our
    # controllers, where there's a class extending from ActionMailer::Base found
    # in app/mailers, and there are views in app/views/mailer_name

## rails g mailer UserMailer
# generates the mailer, views, and tests

# ========================= Mailer =========================

class UserMailer < ApplicationMailer
    default from: 'notifications@example.com'
  
    def self.welcome_email(user)
        @user = user
        @url = 'http://example.com/login'
        mail(to: user.email, subject: 'Welcome to My Awesome Site')
    end
end

# This is how you can send a welcome_email. You can also set cc and bcc attributes
    # To send multiple emails use an array of email strings

# mail() return an email object (Mail::Message), but doesn't send it

# ========================= User Controller =========================

# app/controllers/users_controller.rb
def create
    u = User.create(user_params)

    msg = UserMailer.welcome_email(u)
    msg.deliver_now
    # deliver_now is the method that send the email

    render :root
end

# ========================= Views =========================

# app/views/user_mailer/welcome_email.html.erb

<html>
    <head>
        <meta content='text/html; charset=UTF-8' http-equiv='Content-Type' />
    </head>
    <body>
        <h1>Welcome to example.com, <%= @user.name %></h1>
        <p>
            You have successfully signed up to example.com,
            your username is: <%= @user.login %>.<br />
        </p>
        <p>
            To login to the site, just follow this link: <%= @url %>.
        </p>
        <p>Thanks for joining and have a great day!</p>
    </body>
</html>

# You must also create a text email for people who don't like HTML emails and to 
    # prevent being categorized as spam

# app/views/user_mailer/welcome_email.text.erb

Welcome to example.com, <%= @user.name % >
===============================================

You have successfully signed up to example.com,
your username is: <%= @user.login % >.

To login to the site, just follow this link: <%= @url % >.

Thanks for joining and have a great day!

# The mail method, after detecting two templates, will now generate an alternative email

# ========================= Attachments =========================

# Add a file path to the attachments variable in the mailer file

def welcome_email
    attachments['filename.jpg'] = File.read('/path/to/filename.jpg')
    # ...
end

# ========================= Generate URLs =========================

# app/config/environments/development.rb
config.action_mailer.default_url_options = { host: 'localhost:3000' }

# app/config/environments/production.rb
config.action_mailer.default_url_options = { host: 'www.production-domain.com' }

# ========================= Letter Opener =========================

# Gemfile
gem 'letter_opener', group: :development

# config/environments/development.rb
config.action_mailer.delivery_method = :letter_opener

# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Flash & Flash.now ]]]]]]]]]]]]]]]]]]]]]]]]]

# Flash is similar to session. It is a hash-like object that has key-value pairs
    # of temporary cookies. It's used to display any type of one-time msg (i.e, errors)

# Flash last through the NEXT request/response cycle (use with redirect_to)
# Flash.now last through the CURRENT request/response cycle (use with render)

# Flash includes everything in BOTH flash and flash.now

## rails s -p 9000
# -p flag lets you specify which port to run the server

# $$$$$$$$$$$$$$$$$$$$$$$$$ W7D3 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rails Testing ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Setup =========================

# Necessary Gems:
# rspec-rails: rspec for rails
    # factory_bot_rails: automatically create instances of our models
    # faker: gives us ability to generate random data
    # capybara: allows us to test our views
    # shoulda-matchers: allows us to test our validations. better error msgs
    # launchy: launch external apps from our rails app
    
## rails g rpsec:install
# creates rspec directory and files

# --color
# --format documentation
# add these to .rspec file

# config/application.rb
# change :controller_specs value to true 

## rails g model TestModel
# creates a TestModel in the spec directory
    
# ========================= Models =========================

# Use the rspecs to test for validations, associations, class methods, error messages

it "should validate presence of name" do 
  capy = Capy.new(color: 'blue')
  expect(capy.valid?).to be false
end

# This can be shortened using shoulda-matchers

it { should validate_presence_of(:name) }
it { should validate_uniqueness_of(:name) }
it { should have_many(:parties) }
it { should have_many(:parties_to_attend).through(:attendances) }

# custom validation
it "should validate color is not green" do 
  green_capy = Capy.new(name: "deb", color: "green")
  green_capy.valid?
  expect(green_capy.errors[:color]).to eq(["cannot be green!!"])
end

# class method 
it "should return all capys of color rainbow" do 
  rainbow = Capy.create(name: "rainbow", color: "rainbow")
  not_rainbow = Capy.create(name: "not rainbow", color: "blue")
  expect(Capy.capys_of_the_rainbow).to include(rainbow)
  expect(Capy.capys_of_the_rainbow).not_to include(not_rainbow)
end
# this can be shortened to 
expect(Capy.capys_of_the_rainbow.where_values_hash).to eq("color" => "rainbow")

# ========================= Factory Bot & Faker =========================

FactoryBot.define do 
  factory :capy do 
    name { Faker::Name.name }
    color { Faker::Color.hex_color }
  end
end

# now we can make a capy using FactoryBot

subject(:capy) { FactoryBot.build(:capy) }

FactoryBot.build(:capy, color: "green")     # will build a green capy

# you can also nest this inside the :capy factory method to build a green capy
factory :green_capy do 
  color "green"
end

# ========================= Controllers =========================

# We want to test for status codes and responses

# RSpec Rails API
    # Navigation
        # get
        # post
        # patch
        # delete
    # Assertions
        # render_template
        # redirect_to
        # have_http_status, be_success

# index
it "renders the capy's index" do 
  get :index 
  expect(response).to be_success
  expect(response).to render_template(:index)
end

# show
it "renders the show template" do 
  Capy.create!(name: "deb", color: "blue")
  get :show, id: 1
  expect(response).to render_template(:show)
end
it "is not a success" do 
  begin
    get :show, id: -1
  rescue => exception
    ActiveRecord::RecordNotFound
  end
  expect(response).not_to render_template(:show)
end

# create
it "with invalid params, renders the new template" do 
  post :create, capy: { name: "kath" }
  expect(response).to render_template(:new)
end
it "with valid params, redirects to capys page" do 
  post :create, capy: { name: "kath", color: "maroon" }
  expect(response).to redirect_to(capy_url(Capy.find_by(name: "kath")))
end

# ========================= Capybara =========================

# Capybara API
    # Navigation
        # visit
        # click_on
    # Forms
        # fill_in "field", with: "value"
        # choose, check, uncheck
        # select "option", from: "select box"
    # Assertions
        # have_content
        # current_path
        # page
    # Debugging
        # save_and_open_page

# spec/features/capy_feature.rb

feature "capybara features", type :feature do 
  feature "making a new capybara" do 
    before(:each) do 
      visit "/capys/new"
    end

    scenario "with invalid params" do
      fill_in "name", with: "pam"
      click_on "Create Capy"
      expect(current_path).to eq("/capys")
      expect(page).to have_content("Color can't be blank")
    end

    scenario "with valid params" do
      fill_in "name", with: "pam"
      fill_in "color", with: "pink"
      click_on "Create Capy"
      expect(page).to have_content("pam")
      expect(current_path).to eq("/capys/#{Capy.find_by(name: "pam").id}")
    end
  end
end

# spec/spec_helper.rb

def create_capy(name, color)
  visit "/capys/new"
  fill_in "name", with: name
  fill_in "color", with: color
  click_on "Create Capy"
end

# [[[[[[[[[[[[[[[[[[[[[[[[[  ]]]]]]]]]]]]]]]]]]]]]]]]]
# =========================  =========================
# -------------------------  -------------------------

# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

# ========================= Models =========================

# spec/models/user_spec.rb
require 'rails_helper'

RSpec.describe User, type: :model do 
  # insert tests here
end

# ========================= Controllers =========================

# spec/controllers/songs_controller_spec.rb
require 'rails_helper'

RSpec.describe SongsController, type: :controller do 
  # insert tests here
  describe 'get #new' do 
    it 'brings up the form to make a song' do 
      # subject is instance of SongsController created for request
      # get passed the 'require_logged_in' before_action hook
      # dont use real logged_in? (unit testing); just make it return true
      # to simulate being logged in
      allow(subject).to receive(:logged_in?).and_return(true)
      get :new 

      expect(response).to render_template(:new)
    end
  end

  describe 'delete #destroy' do 
    let(:test_song) { create(:song) }

    it 'destroys the song' do 
      delete :destroy, params: { id: test_song.id }

      expect(Song.exists?(test_song.id)).to be false
    end
  end

  describe 'post #create' do 
    # needs user to be logged in
    before(:each) do 
      create(:user)
      # treat the user we created above as the current user - last in DB
      allow(subject).to receive(:current_user).and_return(User.last)
    end

    context 'with valid params' do 
      before(:each) do 
        post :create, params: { song: { body: 'valid song' } }
      end

      it 'creates the song' do 
        expect(Song.last.body).to eq('valid song')
      end

      it 'redirects to song show page' do  
        expect(response).to redirect_to(song_url(Song.last))
      end
    end

    context 'with invalid params' do 
      before(:each) do 
        post :create, params: { song: { not_valid: '' } }
      end

      it 'renders the new template' do 
        expect(response).to redirect_to(new_song_url)
        expect(response).to have_http_status(422)
      end

      it 'adds errors to flash' do 
        expect(flash[:errors]).to be_present
      end
    end
  end
end

# ------------------------- Factory Bot -------------------------

FactoryBot.define do 
  factory :song do 
    body { 'happy birthday to you!' }

    # song association with user 
    association :author, factory: :user
  end
end

# ========================= Capybara (Views) =========================

# spec/features/songs_spec.rb
require 'rails_helper'

feature 'creating a song', type: :feature do 
  before(:each) do 
    create(:user)
    visit(new_song_url)
  end

  scenario 'takes in a body' do 
    expect(page).to have_content('Body')
    expect(page).to have_content('Create a Song')
  end

  scenario 'takes us back to song show on successful submit' do 
    log_in_user(User.last)
    make_song('over the rainbow!')

    expect(page).to have_content('Song Show Page')
    # song_path is like song_url, except it excludes the domain (localhost:3000)
    expect(current_path).to eq(song_path(Song.last))
    expect(page).to have_content('over the rainbow!')
  end
end

feature 'deleting a song', type: :feature do 
  before(:each) do 
    create(:user)
    log_in_user(User.last)
    make_song('to be deleted')
    click_button('Delete the Song')
  end

  scenario 'deletes the song' do 
    expect(page).to have_content('All the Songs')
    expect(page).to_not have_content('to be deleted')
  end
end

# spec/spec_helper.rb
def log_in_user(user)
  visit new_session_url 
  fill_in('Username:', with: "#{user.username}")
  fill_in('Password:', with: "password")
  click_button('Login')
end

def make_song(body)
  visit new_song_url 
  fill_in('Body', with: "#{body}")
  click_button("Sing a Song")
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W8D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Tag Id Setter ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/rails/-cc--16-tag-ids-setter

has_many :tags, through: :taggings
# This association creates 3 methods
# Cat#tags
# Cat#tag_ids
# Cat#tag_ids=
    # Creates/Destroys records in a join table
    # new_tags = [1, 2, 3]
    # markov.tag_ids=(new_tags)
    # Queries markov.tag_ids to get markov's current tags and then it creates new
        # Tagging objects for any new tag_ids with cat_id: markov.id, tag_id: new_tag_id
        # AND destroys any Tagging objects not in new_tags

# [[[[[[[[[[[[[[[[[[[[[[[[[ Checkboxes ]]]]]]]]]]]]]]]]]]]]]]]]]

<% Tag.all.each do |tag| % >
  <label>  
    <input type="checkbox" name="cat[tag_id][]" value="<%= tag.id %>"
    # allows for an array of multiple tags/checkboxes
      <%= "checked" if @cat.tag_ids.include?(tag.id) % > >
      # will pre-check the box if cat has this tag
  </label>
<% end % >

def cat_params
  params.require(:cat).permit(:name, :color, :description, tag_ids: [])
  # allows for an array of multiple tags
end

validates :cat, :tag, presence: true 
# you have to validate the association instead of the foreign key 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Concerns ]]]]]]]]]]]]]]]]]]]]]]]]]

# A concern is a module that allows us to add class methods, instance methods, and 
    # run code at class definition time all from within one convenient file. Previously
    # with modules we have included them to add instance methods or extended them to
    # add class methods, but a concern can add both instance methods and class methods
    # at the same time! On top of that, concerns can actually execute code at the time
    # they are included, unlike vanilla modules. This means that an association like
    # has_many will immediately be created when we include the concern.

# app/models/concerns/taggable.rb
# file name must be the same as our module's name
module Taggable
  # this module becomes a concern thanks to this line
  extend ActiveSupport::Concern

  # code in this block will be run in class scope when the concern is included
  included do
    # validations and associations usually go here
    has_many :taggings, as: :taggable
    has_many :tags, through: :taggings
    validates #...
    # etc
  end

  # tags_string will become an instance method
  def tags_string
    tags.map(&:name).join(', ')
  end

  # methods defined in here become class methods
  module ClassMethods

    # this will become a class method
    # it should return all the elements that are tagged 'tag_name'
    def by_tag_name(tag_name)
      self.joins(:tags).where('tags.name' => tag_name)
    end
  end
end

# app/models/question.rb
class Question < ApplicationRecord
  include Taggable
  # ...
end

# app/models/answer.rb
class Answer < ApplicationRecord
  include Taggable
  # ...
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W8D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ HTTP ]]]]]]]]]]]]]]]]]]]]]]]]]

# HTTP is a set of rules for the transfer of data between sites

# HTTP Request Example
GET /cats HTTP/1.1
Host: mycats.com

# HTTP Response Example
HTTP/1.1 200 OK
Content-Length: 32
Content-Type: text/html

<html>

</html>

# netcat can be used to examine the HTTP Request/Response cycle. 
# 80 is a standard port 
## nc example.com 80

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rails ]]]]]]]]]]]]]]]]]]]]]]]]]

# Rails takes HTTP Requests and gives HTTP Responses
# The request is received by the default webserver, WEBrick

# [[[[[[[[[[[[[[[[[[[[[[[[[ Rack ]]]]]]]]]]]]]]]]]]]]]]]]]

# Rack is a form of middleware which is used to act as the liason between the 
# server (WEBrick for Rails) and the web application

# WEBrick, Unicorn, Thin, Puma, etc. are kinds of webservers

# Rails, Sinatra, Padrino, Camping, etc. are frameworks

# Middlewares allow for different web servers to communicate with diff frameworks

# ========================= Demo =========================

require 'rack'
require 'json'

class SimpleApp
  def self.call(env)
    req = Rack::Request.new(env)
    res = Rack::Response.new 

    name = req.params['name']

    res.write("Hello #{name}")
    res.finish
  end
end

class CookieApp
  def self.call(env)
    req = Rack::Request.new(env)
    res = Rack::Response.new 

    food = req.params['food']

    if food 
      res.set_cookie(
        '_my_cookie_app',
        {
          path: '/',
          value: {food: food}.to_json
        }
      )
    else
      cookie = req.cookies['_my_cookie_app']
      cookie_val = JSON.parse(cookie)
      food = cookie_val['food']
      res.write("Your favorite food is #{food}")
    end

    res.finish 
  end
end

app = Proc.new do |env|
  req = Rack::Request.new(env)
  res = Rack::Response.new 

  if req.path.start_with?("/cage")
    res.status = 302
    res['location'] = 'http://cage.com'
  else
    res.write("Nothing to see here")
  end

  res.finish 
end

Rack::Server.start({
  app: SimpleApp,
  Port: 3000
})

# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[  ]]]]]]]]]]]]]]]]]]]]]]]]]

# DNS receives domain name, builds HTTP GET request to the domain

# What is a server?
    # HTTP Request hits server before hitting Rails

# Internet Protocol and Transmission Control Protocol
    # IP is the principal

# TCP Handshake

# HTTP
    # Rules for how content of a request/response should be formatted

# HTTP Headers
    # Set of key-value pairs of various properties of a request/response
    # Request
        # Only one header required (in HTTP/1.1): Host
        # Common headers: Accept, Content-Type
    # Response 
        # No headers required

## Rack::Request.new(env).methods-Object.methods
# will return methods that can be called on a request object