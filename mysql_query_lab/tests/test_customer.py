import pandas as pd
import pytest


def test_output(output, df=None):
    """
    Test the output of a query on a DataFrame.

    Parameters:
        output (DataFrame): The output DataFrame from the query.
        df (DataFrame, optional): The DataFrame to perform the query on.
            Default is None.

    Raises:
        AssertionError: If the query output does not meet the expected criteria.
        KeyError: If an invalid key is used in the query.

    Prints:
        A message indicating whether the test passed or not.

    """

    # Test that the query returns the correct number of rows
    assert len(output) == 4, "The query did not return the correct number of rows."

    # Test that the query returns the correct column names
    assert output.columns == ['name'], \
        "The query did not return the correct column names."

    # Test that the query returns the correct values
    assert output.values.flatten().tolist() == ['Will', 'Jane', 'Bill', 'Zack'], \
        "The query did not return the correct values."

    # Test that the query raises an error when an invalid key is used in the query
    with pytest.raises(KeyError):
        try:
            # this will additionally trigger pd.core.computation.ops.UndefinedVariableError
            df.query("invalid_column != 2")[['name']]
        except:
            raise KeyError

    print(f"Test passed: Output matches the expected result.")

if __name__ == '__main__':
    test_output(*args)