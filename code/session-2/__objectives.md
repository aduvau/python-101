# Session #2 Objectives

1. Setup development environment

We should all be able to start a Python project on our machines, safely (closed environment):

- use of terminal
- `python` command working and firing Python v3
- `pip` installation working
- ability to launch the project in a text editor
- ability to execute the code in the terminal (based on `setup.py` in this folder)

2. Make an object with the relevant data only:

- Id of the launch
- Date of the launch
- Location of the launch (<- launchpad)
- Rocket name of the launch (<- rocket)
- Cost of the launch (<- ? (at least I want to know the rocket cost))

```python
next_launch = {
  "id": "",
  "date": 2025-03-20blabla,
  "location": {
    "city": "",
    "facility": "",
    "state": "",
    "lat": 0,
    "long": 0,
  },
  "rocket": {
    "name": "",
    "cost": 0,
  },
}
```

3. (Optional) Github sync setup

If we have time, we should try doing the Github setup all together. This would help us make sure we are all on the same page (+ it'd be recorded for others).
If we cannot, we'll have to do this async because we'll need it later.
