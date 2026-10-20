from application import calculate_grade

def test_system():
    # Structural assertion tests
    assert calculate_grade(95) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(40) == "Fail"
    print("✅ All automated test metrics passed successfully!")

if __name__ == "__main__":
    test_system()
