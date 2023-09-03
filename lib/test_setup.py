import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest,
    select_oldest_bear_and_returns_name_and_age,
    select_youngest_bear_and_returns_name_and_age,
)

def test_select_all_female_bears_return_name_and_age():
    # Write test logic here to verify the correctness of the query
    pass

def test_select_all_bears_names_and_orders_in_alphabetical_order():
    # Write test logic here to verify the correctness of the query
    pass

def test_select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest():
    # Write test logic here to verify the correctness of the query
    pass

def test_select_oldest_bear_and_returns_name_and_age():
    # Write test logic here to verify the correctness of the query
    pass

def test_select_youngest_bear_and_returns_name_and_age():
    # Write test logic here to verify the correctness of the query
    pass

# Run the tests
if __name__ == "__main__":
    import pytest
    pytest.main() 