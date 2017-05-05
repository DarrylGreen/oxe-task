# oxe-task

This has been tested using py.test on a Debian system. Install py.test by running

    pip install pytest

The unit tests in convertor_tests.py assume that the RomanConvertor program is in the same directory as convertor_tests.py. To run the unit tests, cd to the directory containing convertor_tests.py and run

    py.test convertor_tests.py

To use the TextChecker, do the following:

    from text_checker import TextChecker
    text_checker = TextChecker(online_text_url, path_to_RomanConvertor)
    roman_numeral_locations = text_checker.get_locations_of_roman_numerals()

The output of TextChecker.get_locations_of_roman_numerals() is a dictionary with the numbers that were found in the text as the keys, with the values being a list containing the line and word locations that number was found at.