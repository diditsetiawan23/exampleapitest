## API Automation Framework
This simple framework will generate a JSON file as the test report, you can find it on reports/json_reports/{file_here}.
4 Things that tested by this framework :
- Status Code
- Response Format
- JSON Schema
- Response Times

#### Setup
Clone the repository

```sh
# via HTTPS
$ git clone https://github.com/diditsetiawan23/exampleapitest.git

# via ssh
$ git clone git@github.com:diditsetiawan23/exampleapitest.git
```

Install all the related requirements / dependencies by run the following command

```sh
$ pip3 install -r requirements.txt
```

To run all of the test cases, you can prompt with the command of

```sh
$ python test_runner.py
```

To run your own test case instead running all of the tests, by run this command

```sh
$ python -m unittest discover . <name_your_test_file>
```