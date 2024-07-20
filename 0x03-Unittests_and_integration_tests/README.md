# alx-backend-python

This repository contains the code for the ALX Backend Python project. The project focuses on unit testing and integration testing in Python.


## Resources

## Resources

- [unittest](https://docs.python.org/3/library/unittest.html) — Unit testing framework
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — mock object library
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/8658043/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/) — Parameterized testing for Python unit testing
- Memoization


## Unit Testing
Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. It aims to test the logic defined inside the tested function and should only test the function's behavior, mocking any external dependencies.

### TestAccessNestedMap
In the `test_utils.py` file, you will find the `TestAccessNestedMap` class that contains unit tests for the `access_nested_map` function. The tests use the `@parameterized.expand` decorator to test the function with different inputs and assert that the function returns the expected result.

### TestGetJson
The `TestGetJson` class in `test_utils.py` contains unit tests for the `get_json` function. The tests use `unittest.mock.patch` to mock the `requests.get` function and ensure that it returns the expected result. The tests also assert that the mocked `get` method is called with the correct arguments.

### TestMemoize
The `TestMemoize` class in `test_utils.py` demonstrates how to test memoized functions. It uses `unittest.mock.patch` to mock a method and asserts that the memoized property is called only once.

### TestGithubOrgClient
The `TestGithubOrgClient` class in `test_client.py` contains unit tests for the `GithubOrgClient` class. It uses `@patch` as a decorator to mock the `get_json` function and ensure that it is called with the expected arguments. The tests also use `@parameterized.expand` to parametrize the test with different organization examples.

## Integration Testing
Integration testing aims to test the code path end-to-end, including interactions between different parts of the code. It focuses on low-level functions that make external calls, such as HTTP requests, file I/O, and database I/O.

### TestIntegrationGithubOrgClient
The `TestIntegrationGithubOrgClient` class in `test_client.py` contains integration tests for the `GithubOrgClient` class. It uses fixtures from `fixtures.py` to mock external requests and ensure that the `public_repos` method returns the expected results.




## Tasks

1. Parameterize a unit test
    - Implement the `TestAccessNestedMap.test_access_nested_map` method in `test_utils.py` to test the `access_nested_map` function. Use the `@parameterized.expand` decorator to test the function with different inputs and assert that it returns the expected result.

2. Parameterize a unit test (continued)
    - Implement the `TestAccessNestedMap.test_access_nested_map_exception` method in `test_utils.py` to test that a `KeyError` is raised for specific inputs. Use the `@parameterized.expand` decorator to parametrize the test and assert that the exception message is as expected.

3. Mock HTTP calls
    - Implement the `TestGetJson.test_get_json` method in `test_utils.py` to test the `get_json` function. Use `unittest.mock.patch` to mock the `requests.get` function and ensure that it returns the expected result. Assert that the mocked `get` method is called with the correct arguments.

4. Parameterize and patch
    - Implement the `TestMemoize.test_memoize` method in `test_utils.py` to test the memoization functionality of the `memoize` decorator. Use `unittest.mock.patch` to mock a method and assert that when calling a memoized property twice, the correct result is returned and the method is only called once.

5. Parameterize and patch as decorators
    - Implement the `TestGithubOrgClient.test_org` method in `test_client.py` to test the `GithubOrgClient.org` method. Use `@patch` as a decorator to mock the `get_json` function and ensure that it is called with the expected argument. Parametrize the test with different organization examples.

6. Mocking a property
    - Implement the `TestGithubOrgClient.test_public_repos_url` method in `test_client.py` to test the `GithubOrgClient._public_repos_url` property. Use `patch` as a context manager to mock the `GithubOrgClient.org` method and make it return a known payload. Test that the result of `_public_repos_url` is the expected one based on the mocked payload.

7. More patching
    - Implement the `TestGithubOrgClient.test_public_repos` method in `test_client.py` to test the `GithubOrgClient.public_repos` method. Use `@patch` as a decorator to mock the `get_json` function and make it return a payload of your choice. Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value of your choice. Test that the list of repos is what you expect from the chosen payload and that the mocked property and `get_json` were called once.

8. Parameterize
    - Implement the `TestGithubOrgClient.test_has_license` method in `test_client.py` to test the `GithubOrgClient.has_license` method. Parametrize the test with different inputs and assert that the expected returned value matches.

9. Integration test: fixtures
    - Implement the `TestIntegrationGithubOrgClient` class in `test_client.py` to perform integration tests for the `GithubOrgClient` class. Use `@parameterized_class` to parameterize the class with fixtures from `fixtures.py`. Mock the `requests.get` function to return example payloads and assert that the `public_repos` method returns the expected results.

10. Integration tests (advanced)
     - Implement the `TestIntegrationGithubOrgClient.test_public_repos` method in `test_client.py` to test the `GithubOrgClient.public_repos` method. Use the fixtures to define the expected results and assert that the method returns the expected values.

11. Integration tests (advanced)
     - Implement the `TestIntegrationGithubOrgClient.test_public_repos_with_license` method in `test_client.py` to test the `GithubOrgClient.public_repos` method with the `license` argument. Use the fixtures to define the expected results and assert that the method returns the expected values.


## HappyCoding!
