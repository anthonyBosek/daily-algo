"""
    726. Number of Atoms
    https://leetcode.com/problems/number-of-atoms/

    Given a string formula representing a chemical formula, return the count of each atom.

    The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

    One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
        - For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.

    Two formulas are concatenated together to produce another formula.
        - For example, "H2O2He3Mg4" is also a formula.

    A formula placed in parentheses, and a count (optionally added) is also a formula.
        - For example, "(H2O2)" and "(H2O2)3" are formulas.

    Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count
    (if that count is more than 1), followed by the second name (in sorted order), followed by its count
    (if that count is more than 1), and so on.

    The test cases are generated so that all the values in the output fit in a 32-bit integer.

"""

from collections import defaultdict


#! Approach 1: Recursion (option 1)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Length of the formula
        n = len(formula)

        # Current index. It should be global as needs
        # to be updated in the recursive function
        self.index = 0

        # Recursively parse the formula
        def parse_formula():
            # Local variable
            curr_map = defaultdict(int)
            curr_atom = ""
            curr_count = ""

            # Iterate until the end of the formula
            while self.index < n:
                # UPPERCASE LETTER
                if formula[self.index].isupper():
                    # Save the previous atom and count
                    if curr_atom:
                        if curr_count == "":
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)

                    curr_atom = formula[self.index]
                    curr_count = ""
                    self.index += 1

                # lowercase letter
                elif formula[self.index].islower():
                    curr_atom += formula[self.index]
                    self.index += 1

                # Digit. Concatenate the count
                elif formula[self.index].isdigit():
                    curr_count += formula[self.index]
                    self.index += 1

                # Left Parenthesis
                elif formula[self.index] == "(":
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        curr_map[atom] += nested_map[atom]

                # Right Parenthesis
                elif formula[self.index] == ")":
                    # Save the last atom and count of nested formula
                    if curr_atom:
                        if curr_count == "":
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)

                    self.index += 1
                    multiplier = ""
                    while self.index < n and formula[self.index].isdigit():
                        multiplier += formula[self.index]
                        self.index += 1
                    if multiplier:
                        multiplier = int(multiplier)
                        for atom in curr_map:
                            curr_map[atom] *= multiplier

                    return curr_map

            # Save the last atom and count
            if curr_atom:
                if curr_count == "":
                    curr_map[curr_atom] += 1
                else:
                    curr_map[curr_atom] += int(curr_count)

            return curr_map

        # Parse the formula
        final_map = parse_formula()

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans


#! Approach 1: Recursion (option 2)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Length of the formula
        n = len(formula)

        # Current index. It should be global as needs
        # to be updated in the recursive function
        self.index = 0

        # Recursively parse the formula
        def parse_formula():
            # To save the count of atoms in the formula
            curr_map = defaultdict(int)

            # Iterate until the right parenthesis or end of the formula
            while self.index < n and formula[self.index] != ")":
                # If left parenthesis, do recursion
                if formula[self.index] == "(":
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        curr_map[atom] += nested_map[atom]

                # Otherwise, it should be UPPERCASE LETTER
                # Extract the atom and count in one go.
                else:
                    curr_atom = formula[self.index]
                    self.index += 1
                    while self.index < n and formula[self.index].islower():
                        curr_atom += formula[self.index]
                        self.index += 1

                    curr_count = ""
                    while self.index < n and formula[self.index].isdigit():
                        curr_count += formula[self.index]
                        self.index += 1

                    if curr_count == "":
                        curr_map[curr_atom] += 1
                    else:
                        curr_map[curr_atom] += int(curr_count)

            # If the right parenthesis, extract the multiplier
            # and multiply the count of atoms in the curr_map
            self.index += 1
            multiplier = ""
            while self.index < n and formula[self.index].isdigit():
                multiplier += formula[self.index]
                self.index += 1

            if multiplier:
                multiplier = int(multiplier)
                for atom in curr_map:
                    curr_map[atom] *= multiplier

            return curr_map

        # Parse the formula
        final_map = parse_formula()

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans


#! Approach 2: Stack
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Stack to keep track of the atoms and their counts
        stack = [defaultdict(int)]

        # Index to keep track of the current character
        index = 0

        # Parse the formula
        while index < len(formula):
            # If left parenthesis, insert a new hashmap to the stack. It will
            # keep track of the atoms and their counts in the nested formula
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1

            # If right parenthesis, pop the top element from the stack
            # Multiply the count with the multiplicity of the nested formula
            elif formula[index] == ")":
                curr_map = stack.pop()
                index += 1
                multiplier = ""
                while index < len(formula) and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier

                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]

            # Otherwise, it must be a UPPERCASE LETTER. Extract the complete
            # atom with frequency, and update the most recent hashmap
            else:
                curr_atom = formula[index]
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                curr_count = ""
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)

        # Sort the final map
        final_map = dict(sorted(stack[0].items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
    
    #! Approach 3: Regular Expression
    class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Regular expression to extract atom, count, (, ), multiplier
        # Every element of matcher will be a quintuple
        regex = r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)"
        matcher = re.findall(regex, formula)

        # Stack to keep track of the atoms and their counts
        stack = [defaultdict(int)]

        # Parse the formula
        for atom, count, left, right, multiplier in matcher:
            # If atom, add it to the top hashmap
            if atom:
                stack[-1][atom] += int(count) if count else 1

            # If left parenthesis, insert a new hashmap to the stack
            elif left:
                stack.append(defaultdict(int))

            # If right parenthesis, pop the top element from the stack
            # Multiply the count with the attached multiplicity.
            # Add the count to the current formula
            elif right:
                curr_map = stack.pop()
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier
                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]

        # Sort the final map
        final_map = dict(sorted(stack[0].items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
    
    #! Approach 4: Reverse Scanning
    class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # For multipliers
        running_mul = 1
        stack = [1]

        # Map to store the count of atoms
        final_map = defaultdict(int)

        # Strings to take care of current atom and count
        curr_atom = ""
        curr_count = ""

        # Index to traverse the formula in reverse
        index = len(formula) - 1

        # Parse the formula
        while index >= 0:
            # If digit, update the count
            if formula[index].isdigit():
                curr_count = formula[index] + curr_count

            # If lowercase letter, prepend to the curr_atom
            elif formula[index].islower():
                curr_atom = formula[index] + curr_atom

            # If UPPERCASE LETTER, prepend and update the finalMap
            elif formula[index].isupper():
                curr_atom = formula[index] + curr_atom
                if curr_count:
                    final_map[curr_atom] += int(curr_count) * running_mul
                else:
                    final_map[curr_atom] += 1 * running_mul

                curr_atom = ""
                curr_count = ""

            # If the right parenthesis, the curr_count if any
            # will be considered a multiplier
            elif formula[index] == ")":
                curr_multiplier = int(curr_count) if curr_count else 1
                stack.append(curr_multiplier)
                running_mul *= curr_multiplier
                curr_count = ""

            # If left parenthesis, update the running_mul
            elif formula[index] == "(":
                running_mul //= stack.pop()

            index -= 1

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
    
    #! Approach 5: Preprocessing
    class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # For every index, store the valid multiplier
        muls = []
        running_mul = 1

        # Stack to take care of nested formula
        stack = [1]

        # Preprocess the formula and extract all multipliers
        index = len(formula) - 1
        curr_number = ""
        while index >= 0:
            if formula[index].isdigit():
                curr_number += formula[index]

            # If we encountered a letter, then the scanned
            # number was count and not multiplier. Discard it.
            elif formula[index].isalpha():
                curr_number = ""

            # If we encounter a right parenthesis, then the
            # scanned number was a multiplier. Store it.
            elif formula[index] == ")":
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ""

            # If we encounter a left parenthesis, then the
            # most recent multiplier will cease to exist.
            elif formula[index] == "(":
                running_mul //= stack.pop()
                curr_number = ""

            # For every index, store the valid multiplier
            muls.append(running_mul)
            index -= 1

        # Reverse the muls
        muls = muls[::-1]

        # Map to store the count of atoms
        final_map = defaultdict(int)

        # Traverse left to right in the formula
        index = 0
        while index < len(formula):
            # If UPPER CASE LETTER, extract the entire atom
            if formula[index].isupper():
                curr_atom = formula[index]
                curr_count = ""
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                # Extract the count
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                # Update the final map
                if curr_count:
                    final_map[curr_atom] += int(curr_count) * muls[index - 1]
                else:
                    final_map[curr_atom] += 1 * muls[index - 1]

            else:
                index += 1

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
    
#! Approach 6: Reverse Scanning with Regex
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Every element of matcher will be a quintuple
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        matcher.reverse()

        # Map to store the count of atoms
        final_map = defaultdict(int)

        # Stack to keep track of the nested multiplicities
        stack = [1]

        # Current Multiplicity
        running_mul = 1

        # Parse the formula
        for atom, count, left, right, multiplier in matcher:
            # If atom, add it to the final map
            if atom:
                if count:
                    final_map[atom] += int(count) * running_mul
                else:
                    final_map[atom] += 1 * running_mul

            # If the right parenthesis, multiply the running_mul
            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                running_mul *= multiplier
                stack.append(multiplier)

            # If left parenthesis, divide the running_mul
            elif left:
                running_mul //= stack.pop()

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans