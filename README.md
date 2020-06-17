# Front End python application

## Contributors

**Data Science**
|||||
|:--:|:--:|:--:|:--:|
|Chris|Brandon|Monica|Jack|

## What is it?

The main purpose of this application is the compliment the electron client for Tagger-Mail. This python application is standalone, which serves to the client using `zerorpc` and `zeromq`. The main class - `TaggerMail` - has several methods which serve as the handlers for incoming requests.

## Methods

```
say_hello (func)

    Args:
        None

    Yields:
        "Hello, World!"
```

## Tech Stack

* python
    * zerorpc

## Usage

To test this locally, make sure you have python version >= 3.7.
From the command line, run

`$ zerorpc tcp://localhost:4242 say_hello`

Output:

`"Hello, World!"`
