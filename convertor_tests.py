import pytest
import sys
import os
from subprocess import Popen, PIPE
from text_checker import TextChecker


def test_roman_numerals():
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('I V X L C D M\n')
    assert pipe.stdout.readline() == '1\n'
    assert pipe.stdout.readline() == '5\n'
    assert pipe.stdout.readline() == '10\n'
    assert pipe.stdout.readline() == '50\n'
    assert pipe.stdout.readline() == '100\n'
    assert pipe.stdout.readline() == '500\n'
    assert pipe.stdout.readline() == '1000\n'
    pipe.terminate()


def test_lowercase():
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('abcdefghijklmnopqrstuvwxyz\n')
    assert pipe.stdout.readline() == '0\n'
    pipe.terminate()


def test_non_roman_numerals():
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('ABEFGHJKNOPQRSTUWYZ\n')
    assert pipe.stdout.readline() == '0\n'
    pipe.terminate()


def test_subtraction():
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('IV IX IL IC ID IM XL XC XD XM CD CM\n')
    assert pipe.stdout.readline() == '4\n'
    assert pipe.stdout.readline() == '9\n'
    assert pipe.stdout.readline() == '49\n'
    assert pipe.stdout.readline() == '99\n'
    assert pipe.stdout.readline() == '499\n'
    assert pipe.stdout.readline() == '999\n'
    assert pipe.stdout.readline() == '40\n'
    assert pipe.stdout.readline() == '90\n'
    assert pipe.stdout.readline() == '490\n'
    assert pipe.stdout.readline() == '990\n'
    assert pipe.stdout.readline() == '400\n'
    assert pipe.stdout.readline() == '900\n'
    pipe.terminate()


def test_non_standard_roman_numerals():  # These are not standard Roman numerals
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('IVI CLDI VXLC\n')
    assert pipe.stdout.readline() == '5\n'
    assert pipe.stdout.readline() == '551\n'
    assert pipe.stdout.readline() == '35\n'
    pipe.terminate()


def test_non_roman_numeral_word():  # The converter incorrectly states these are Roman numerals
    pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
    pipe.stdin.write('Idea DEMAND\n')
    assert pipe.stdout.readline() == '1\n'
    assert pipe.stdout.readline() == '2000\n'
    pipe.terminate()


def test_TextChecker_output():
    text_to_check = "http://www.gutenberg.org/files/54610/54610-0.txt"
    text_checker = TextChecker(text_to_check, './RomanConvertor')
    roman_numeral_locations = text_checker.get_locations_of_roman_numerals()
    assert roman_numeral_locations['4'] == ['Line 116, word 1', 'Line 1113, word 1', 'Line 3951, word 6']
    assert roman_numeral_locations['12'] == ['Line 133, word 1', 'Line 2299, word 1']
