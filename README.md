# Nirvana project

## Project description

Project instructions
Suppose you have 3 different APIs you can call with member_id as a parameter.

 

so example API calls would be:

 

https://api1.com?member_id=1

https://api2.com?member_id=1

https://api3.com?member_id=1

 

and you'll get responses from these apis with similar responses:

 

API1: {deductible: 1000, stop_loss: 10000, oop_max: 5000}

API2: {deductible: 1200, stop_loss: 13000, oop_max: 6000}

API3: {deductible: 1000, stop_loss: 10000, oop_max: 6000}

 

As you can see above the API's don't always agree. The task is to build an API that calls these APIs and coalesces the responses with a strategy. 



An example strategy could be the average of the response fields. With the average strategy, your coalesce API would respond with:

{deductible: 1066, stop_loss: 11000, oop_max: 5666}

 

Your API should:

Take in the member_id as a parameter
Make the calls to the different APIs
Coalesce the data returned by the APIs
As a bonus challenge: allow for the coalescing strategy to be configurable
 

What we are looking for:

Testing,

Design Patterns,

Efficiency,

and last but not least creativity!

 

Note: We recommend using a lightweight framework like Flask or FastAPI for this project (we use FastAPI at Nirvana), but feel free to use whatever framework you are most familiar with!

 

How to submit
Upload your completed project to your GitHub, and then paste a link to the repository below in the form along with any comments you have about your solution.


## Setup

Using Python 3.7 proceed to install requirements in /requirements

```
pip install -r requirements/prod.txt
```

## Testing

```
pip install -r requirements/test.txt
```

```
 pytest --cov=api --cov=api_internal tests/
```