# Vue SSR in Python


This is a simple proof of concept used to illustrate how we can use the Python and the V8 engine via [PyMiniRacer](https://github.com/sqreen/PyMiniRacer) to perform server side rendering of [Vue](https://vuejs.org/) applications from a Python process. This POC was inspired by the [non-Node](https://ssr.vuejs.org/en/non-node.html) documentation you can find for Vue ssr.

Moving forward I plan to build a proper library for rendering apps within a web framework such as [Flask](https://github.com/pallets/flask) or [APIstar](https://github.com/encode/apistar)

## Instructions

Download the git:

```
$git clone https://github.com/androiddrew/py_vue_ssr_poc.git
$ cd ./py_vue_ssr_poc
```

Setup a virtual environment and activate it:

```
$ python3 -m venv env
$ source env/bin/activate
```

install your requirements:

```
$(env) pip install -r requirements`
$(env) npm install
```

Execute the script:

`$(env) python py_vue_ssr.py`

You will see that our component defined in `ssr_example.js` has been rendered to an HTML string and printed to the console:

`$(env)<div data-server-rendered="true">Vue SSR in Python</div>`
