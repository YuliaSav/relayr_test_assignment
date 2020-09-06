Test assignment for relayr.io (version for MacOS).
### Test Assignment
How would you approach test automation of an HTTP API of some service? 
Choose a service from this list https://github.com/toddmotto/public-apis or any other of your choice.
It is better to pick one without authorization as it is easier to test.

Document several test cases. 
Implement one or two automated tests based on the test cases. 
Write the tests as if they were a part of a real project.

### Implementation details
_Disclaimer.
Before running the script, please, make sure that you have `python3` and `virtualenv` installed on your machine.
If you don't, then please install then with the following commands:_
```
brew install python3
```
```
pip3 install virtualenv
```

Use bash script 'run.sh' to prepare environment and run the test: 
```
./run.sh
```

For testing I've chosen unofficial BrewDog's public API - https://api.punkapi.com/v2/.
Because their Punk IPA beer is one of my favourite beers. Also this API is
quite simple and straightforward.

All tests are stored inside `brewdog` folder. There are a couple of simple test cases for the API.
Tests are running under `python3` and `pytest`.