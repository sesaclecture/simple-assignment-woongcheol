import assignment

def test_name_type():
<<<<<<< Updated upstream
    assert isinstance(assignment.name, str)

def test_age_type():
    assert isinstance(assignment.age, int)

def test_numbers_content():
    assert 2 in assignment.numbers
    assert len(assignment.numbers) == 3

def test_is_student():
    assert assignment.is_student is True
=======
    assert isinstance(assignment.name, str), "name should be a string"

def test_age_type():
    assert isinstance(assignment.age, int), "age should be an integer"

def test_numbers_content():
    assert isinstance(assignment.numbers, list), "numbers should be a list"
    assert all(isinstance(num, int) for num in assignment.numbers), "all elements in numbers should be integers"

def test_is_student_type():
    assert isinstance(assignment.is_student, bool), "is_student should be a boolean"
>>>>>>> Stashed changes
