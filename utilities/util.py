"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""

import time
import logging
import traceback
import random, string
import utilities.custom_logger as cl


class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """ Put the program to wait for the specified amount of time """
        if info is not None:
            self.log.info(f"Wait:: {sec} seconds for {info}")
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alpha_numeric(self, length, type="letters"):
        """
        Get random string characters
        :param length: Length of string, number of characters string should have
        :param type: Type of characters string should have. Default is letters
        Provide lower/upper/digits for different types
        """
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "digits":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        select_choice = alpha_num.join(random.choice(case) for i in range(length))
        return select_choice

    def get_unique_name(self, charCount=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(charCount, type="lower")

    def get_unique_name_list(self, listsize=5, itemLength=None):
        """
        Get a list of valid emails
        :param
        listsize: number of names. default is 5
        itemLength: It should be a list containing number of items equal to the listSize.
        This determines the length of each item in the list -> [1, 2, 3, 4, 5]
        """
        namelist = []
        for i in range(0, listsize):
            namelist.append(self.get_unique_name(itemLength[i]))
            return namelist

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        self.log.info(f"Actual Text From Application Web UI --> :: {actual_text}")
        self.log.info(f"Expected Text From Application Web UI --> :: {expected_text}")
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verify_text_math(self, actual_text, expected_text):
        self.log.info(f"Actual Text From Application Web UI --> :: {actual_text}")
        self.log.info(f"Expected Text From Application Web UI --> :: {expected_text}")
        if expected_text.lower() == actual_text.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True

