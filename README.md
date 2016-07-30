#dlup
A simple and tiny bot to increase download counts of things on the Internet. Will work for what you want it to as long as it meets the
following conditions: 1) Counts downloads by HTTP `GET` requests, and 2) Allows external downloads without authentication. 
Made with the intention of education. :sunglasses:

###Usage
```sh
$ git clone https://github.com/ifvictr/dlup
$ cd dlup
$ python dlup.py
```
Remember to modify the variables `MAX_THREADS`, `LOOPS_PER_THREAD`, and `TARGETS` to suit your needs.
