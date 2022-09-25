#!/bin/bash
<<<<<<< HEAD
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}

=======
# This program takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
>>>>>>> 66776013a7346e445b9783fbf2c53239a097b9d6
