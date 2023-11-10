# Algorithms

This repository have the objective to store diferent types of algorithms your applications.

## Structure

```
├───data_structures
│   ├───algorithm_type_1
│   │   └───classes
│   ├───algorithm_type_2
│   │   └───classes
│   ├───algorithm_type_n
│   │   └───classes
├───docs
├───algorithm_type_1
│   ├───algorithm_1
│   ├───algorithm_n
├───algorithm_type_2
│   ├───algorithm_1
│   ├───algorithm_n
├───algorithm_type_n
│   ├───algorithm_1
│   ├───algorithm_n
├───utils
├───main.py
```

- ./data_strucutre store the classes that will be used in the algorithms
- For each type of algorithm problem, ./data_structure should have (if necessry) a subdirectory with the name of the type of algorithm problem
- Each subdirectory of the project Algorithms, besides data_structures, stores files that implements algorithm to 
resolve problems of that type of algorithm, for example, the type Graphs will have a file implementing algorithms
for the hamiltonian cycle problem and another for the shorthest path problem.
- ./docs will store external documentation, articles, books, links (if copyright don't allow), or whatever explains implementations of the algorithms
- ./utils will store utility files, such as CLI interface implementations, desktop interface implementations, etc.
## Good Practices

This repo should follow the [PEP8](https://peps.python.org/pep-0008/) conventions.

### Modules
```
Modules should have short, all-lowercase names. 
Underscores can be used in the module name if it improves readability. 
Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
```

### Classes
```
Class names should normally use the CapWords convention.
```

### Functions and variables
```
Function names should be lowercase, with words separated by underscores as necessary to improve readability.
```
In addition, functions names must be in the imperative form.

### Documentation on code
Every function or method should have a docstring as described in [PEP257](https://peps.python.org/pep-0257/).
On the docstring, it's convenient to explain the function, the parameters and the return value. 
If it's a main algorithm function, it's convenient to explain the algorithm, computer science interests ~~(for the nerds)~~, and references on the ./docs folder.
If it is based on a pseudocode, you can add the pseudocode on the code using single line comments.