# Session 1: let's discover SpaceX API!

## 1. Recording

[Python 101 - Session 1](https://raileuropegroupe-my.sharepoint.com/:v:/g/personal/aduvauchelle_raileurope_com/ETb6-h9396xOkSGgxdpAJLYBm3c-dGViR48cHsVBLuIiEQ)

## 2. How to use an external library?

You will have several kinds of modules, including:

1. Those included in the standard library of Python (like `print`): **You can just call them**
2. Those that are included with your Python standard environment, even if not in Python itself (like `json`): **You need to import them**
3. Those that are not included by default (like `requests`): **You need to install them** with `pip install <library_name>`

## 2. Fetching an API

### API URL and endpoints

1. We need the API "base url": this is the **URL part shared by all our requests**. For instance: `https://api.spacexdata.com/v4`. It is composed of `https://api.spacexdata.com`, which is the general URL, and `/v4`, the version of the API we are fetching.
   The version is not always here, depending on APIs. If it is, **you must target the same version** for all the requests of your app. Changes of versions often lead to breaking changes in the API implementation. So you might not get the same endpoints, or an endpoint might not provide the same data structure, breaking our code.
   To correctly select a version, try to find the last stable version. Sometimes it's explicit. Sometimes, like for the SpaceX API, you have to guess: one endpoint only was on v5, everything else is on v4... We have to use v4.
2. We have to fetch from endpoints. One endpoint in our case is the one to get the next launch: `/launches/next`. It is kind of a special one, because the id of the next launch cannot be known in advance. But remember that for REST APIs, you usually have endpoints to fetch all launches (`/launches`) or one launch, providing an id in the request (`/launches/410320-230230-2309448`).
3. So our full URL will be: `https://api.spacexdata.com/v4/launches/410320-230230-2309448`.
4. Because we want a single source of truth for the base url and the version, we will store it at one single place, and then interpolate it in all of our requests. Remember:

```python
import requests

base_url = "https://api.spacexdata.com/v4"

next_launch = requests.get(f"{base_url}/launches/next")

# OR

all_rockets = requests.get(f"{base_url}/rockets")
```

### Fetching

As seen in the session and in the code above, we need a special external libraries to make our requests: `requests`. You can find other, more advanced, more modern, but `requests` is very simple to use for us.

- To install: `pip install requests` in your terminal.
- Then you can import it in your file: `import requests`, at the top of the file.
- Then you can use it: `requests.get("api_url")`

Right now, we have only seen one **request method**: `get`. Just remember it is used to fetch data that we will manipulate and display in our client (terminal, server, browser, etc), but that cannot be used to write data on the database, or modify the data. We would need different methods for that, like `post`. But that would need some security, like authentication, etc.

### HTTP Statuses

We have only encountered two statuses for now:

- `200` means "Everything went fine"
- `404` means "The resource was not found on the API"

Remember that you can access this status after doing you request:

```python
result = requests.get("api_url")

status = result.status_code
```

### Result data and manipulation

Once we have our data, it can be access through two main methods:

```python
result = requests.get("api_url")

content = result.text

# OR

content_as_json = result.json()
```

Text is a long string that has the advantage of giving you the data, but is not very usable.
With `json()`, the result is transformed into a JSON object that you will be able to manipulate. Note that the `.json()` method is possible because the return of our `requests.get()` is of type `Response` object. What can we do with it:

- Access any data in it: `content_as_json["id"]`
- Write to a JSON file to store your data

To write your data, don't overthink it. It's a combination of `open` and `json`, both included in your env by default (but you need to `import json`). Just keep this somewhere:

```python
with open(f"output/filename.json", "w") as file:
        json.dump(json_data, file, indent=2)
```

## 3. Refactoring

That was the very last part of the session, and remember that **we only scratched the surface of it**.

Two rules, that I use but that you will adapt, ditch or embrace as your grow as a programmer:

- Never do **premature refactoring**: if you can't spot the same patterns repeated 3, 4 or more times, it is probably not the right time to refacto. If you do, you might overcomplicate it, or introduce some code design that might not scale in the future because you did not have all the information at the time you decided to refacto.
- [Keep it simple, stupid!](https://en.wikipedia.org/wiki/KISS_principle): think about your teammates, or yourself in 6 months. They probably won't mind that you found the smartest refactoring ever with tons of abstraction if they can't understand what your code is doing. Keeping our code simple, aka calling `get_json()` and `write_json()` three times, even with some code duplication, and adding a comment to explain what each step is supposed to do, was definitely a better choice than trying to make a clever loop over abstract data to reduce the number of lines of code.

As we have said, refactoring at a higher level of complexity is hard, and will probably require more safeguards (like tests) to make sure we don't break anything in our app.

Keep in mind that refactoring is useful, though. For instance, we have introduced:

```python
def get_json(url: str) -> json:
    result = requests.get(url)
    return result.json()
```

It fetches and returns the result as JSON. We were using it three times, probably a lot more when it grows... It might not be perfect based on our future usecases, but it is still easy enough to understand, so we won't have much trouble doing something else with it.

## 5. Dynamic types and typing hints

We have talked about it: Python is a dynamic typer. Some coders like it, some hate it. It is what it is, and it is perfectly fine in Python to do:

```python

a = 42

print(type(a)) # Output 'int'

a = "Hello"

print(type(a)) # Output 'str'
```

But sometimes, we want to have more guidance. If we cannot force the developer to use the intended types, at least we can give them hints about what we wanted to achieve. Let's look at this code:

```python
def write_json(data: json, data_type: str) -> None:
    with open(f"output/data_{data_type}.json", "w") as file:
        json.dump(data, file, indent=2)
```

So, `write_json` is a function (`def` is the clue) that takes two arguments (`data` and `data_type`) and returns nothing.

Again, if you call `write_json(42, {"a": "Cheese"})`, nothing is going to break... Well, it is going to break because you won't be able to write your json file ^^ but at least it will let you call the function anyway. So it is what is is: a hint to guide the developer. And it's perfectly optional.

## 6. Blank page syndrom

Don't get stuck.
Don't jump into code straight away.
You are not here to code, you are here to solve a problem, so:

- Make sure you understand your problem
- Make sure you understand the steps you need to go through to solve your problem
- Do not hesitate to use pseudo-code: write the steps in plain English, in comments, so your problem is divided in smaller, easier steps

For example, in this session:

**Problem to solve**: I want to store data regarding next launch, like `date`, `location` and `rocket`.
**Steps to reproduce (global view)**:

- I need to get the data for next launch
- I need to transform the data into a writable format
- I need to store that transformed data somewhere
  **Steps to reproduce (more precise)**:
- I need to get the data for next launch
  - I need an URL
  - I need an endpoint
  - I need a library to fetch
  - I need to do fetch
- I need to transform the data into a writable format
  - I need to transform the result in JSON
  - I need to store this JSON in a variable
- I need to store that transformed data somewhere - I need to use a library to write in a json file - I need to give it my JSON variable value - I need to give it a filename - I need to give it options (here, `indent=2`)
  etc.

## 5. Next time

If you want, you can start thinking about what comes next.

As we said, we now have 3 unrelated JSON files:

- `data_launch.json` has the `date` we need and knows the ids of `launchpad` and `rocket`
- `data_launchpad.json` has the location of the launch
- `data_rocket.json` has the `name` of the rocket and the `price` of a launch with it

We probably want an object looking like:

```python

    # next_launch = {
    #   "id": "",
    #   "date": 2025-03-20blabla,
    #   "location": {
    #       "city": "",
    #       "facility": "",
    #       "state": "",
    #       "lat": 0,
    #       "long": 0,
    #   },
    #   "rocket": {
    #       "name": "",
    #       "cost": 0,
    #   },
    # }
```

- Can you think of a way to build this object?
- Can you think of usecases where we would like to use this object (should we store, print, should we make something that can be interrogated by the user through the terminal)?
- Can you think of other relevant data we could get for our next launch, based on the data we already store or other endpoints from the API?
- Can you think of ways to implement of of these?
