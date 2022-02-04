from code_challenges.array_insert_shift.array_insert_shift import insert_shift_array

def test_setup():
    assert True

def test_module_import():
    arr = [2, 4, 5, -8]
    num = 5
    actual = insert_shift_array(arr, 5)
    assert actual == [2, 4, 5, 5, -8]

