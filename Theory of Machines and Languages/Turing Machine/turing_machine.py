class TuringMachine:
    def __init__(self, tape):
        # Initialize the Turing Machine with the input tape and states
        self.tape = list(tape)  # Main tape containing the input string
        self.head = 0  # Head position on the main tape
        self.state = 'q0'  # Initial state of the machine
        self.a_tape = ['0']  # Second tape to store binary count of 'a'
        self.b_tape = ['0']  # Third tape to store binary count of 'b'
        self.a_head = 0  # Head position on the a_tape
        self.b_head = 0  # Head position on the b_tape

    def move_head(self, direction, tape='main'):
        # Move the head in the specified direction (R: right, L: left) on the specified tape
        if tape == 'main':
            if direction == 'R':
                self.head += 1
                if self.head >= len(self.tape):
                    self.tape.append('_')  # Append a blank if the head moves past the end
            elif direction == 'L':
                self.head -= 1
                if self.head < 0:
                    self.tape.insert(0, '_')  # Insert a blank if the head moves before the start
        elif tape == 'a':
            if direction == 'R':
                self.a_head += 1
                if self.a_head >= len(self.a_tape):
                    self.a_tape.append('0')
            elif direction == 'L':
                self.a_head -= 1
                if self.a_head < 0:
                    self.a_tape.insert(0, '0')
        elif tape == 'b':
            if direction == 'R':
                self.b_head += 1
                if self.b_head >= len(self.b_tape):
                    self.b_tape.append('0')
            elif direction == 'L':
                self.b_head -= 1
                if self.b_head < 0:
                    self.b_tape.insert(0, '0')

    def read(self, tape='main'):
        # Read the current character at the head position on the specified tape
        if tape == 'main':
            return self.tape[self.head]
        elif tape == 'a':
            return self.a_tape[self.a_head]
        elif tape == 'b':
            return self.b_tape[self.b_head]

    def write(self, char, tape='main'):
        # Write the specified character at the head position on the specified tape
        if tape == 'main':
            self.tape[self.head] = char
        elif tape == 'a':
            self.a_tape[self.a_head] = char
        elif tape == 'b':
            self.b_tape[self.b_head] = char

    def increment_tape(self, tape):
        # Increment the binary number on the specified tape by 1
        current_tape = self.a_tape if tape == 'a' else self.b_tape
        head_position = self.a_head if tape == 'a' else self.b_head

        carry = 1
        while carry:
            if head_position >= len(current_tape):
                current_tape.append('0')  # Extend the tape if needed

            if current_tape[head_position] == '0':
                current_tape[head_position] = '1'
                carry = 0
            else:
                current_tape[head_position] = '0'
                head_position += 1

        if tape == 'a':
            self.a_tape = current_tape
        else:
            self.b_tape = current_tape

    def binary_to_decimal(self, tape):
        # Convert the binary number on the specified tape to a decimal integer
        return int("".join(reversed(tape)), 2)

    def run(self):
        # Execute the Turing Machine based on its states and transitions
        while self.state != 'halt':

            if self.state == 'q0':
                # In state q0, process 'a' and increment its count, or transition to q1 for 'b'
                if self.read() == 'a':
                    self.increment_tape('a')
                    self.move_head('R', 'main')
                elif self.read() == 'b':
                    self.state = 'q1'
                elif self.read() == '_':
                    self.state = 'q_check'
                else:
                    print("Rejected! please consider the shape of a^nb^m | n = m^2, m >= 1, no possibility for the n=m=0 or other alphabet signs.")
                    self.state = 'q_reject'

            elif self.state == 'q1':
                # In state q1, process 'b' and increment its count, or transition to q_check for '_'
                if self.read() == 'b':
                    self.increment_tape('b')
                    self.move_head('R', 'main')
                elif self.read() == '_':
                    self.state = 'q_check'
                else:
                    print("Rejected! please consider the shape of a^nb^m | n = m^2, m >= 1, no possibility for the <a> after b or other alphabets")
                    self.state = 'q_reject'

            elif self.state == 'q_check':
                # In state q_check, verify if n = m^2 using the squared binary tape
                square_tape = square_binary_tape(self.b_tape)
                if self.a_tape == square_tape:
                    print("Accepted! a_count =", self.binary_to_decimal(self.a_tape), "b_count =", self.binary_to_decimal(self.b_tape),"squared turing machine output count= ",self.binary_to_decimal(square_tape))
                    self.state = 'q_accept'                    
                else:
                    print("Rejected! a_count =", self.binary_to_decimal(self.a_tape), "b_count =", self.binary_to_decimal(self.b_tape),"squared turing machine output count= ",self.binary_to_decimal(square_tape))
                    self.state = 'q_reject'

            elif self.state == 'q_accept':
                break

            elif self.state == 'q_reject':
                break

        return ''.join(self.tape).strip('_')


def square_binary_tape(binary_tape):
    #Turing machine to compute the square of the binary number
    class SquaringTuringMachine:
        def __init__(self, binary_input):
            self.input_tape = list(binary_input)  # Tape holding the binary input number
            self.result_tape = ['0']  # Tape to store the result (initialized as 0)
            self.temp_tape = ['0']  # Temporary tape for intermediate results
            self.input_head = 0  # Head position on the input tape
            self.result_head = 0  # Head position on the result tape
            self.temp_head = 0  # Head position on the temporary tape

        def reset_temp(self):
            # Reset the temporary tape for new computations
            self.temp_tape = ['0']
            self.temp_head = 0

        def move_head(self, direction, tape):
            # Move the head in the specified direction (R: right, L: left) on the specified tape
            if tape == 'input':
                if direction == 'R':
                    self.input_head += 1
                    if self.input_head >= len(self.input_tape):
                        self.input_tape.append('0')
                elif direction == 'L':
                    self.input_head -= 1
                    if self.input_head < 0:
                        self.input_tape.insert(0, '0')
            elif tape == 'result':
                if direction == 'R':
                    self.result_head += 1
                    if self.result_head >= len(self.result_tape):
                        self.result_tape.append('0')
                elif direction == 'L':
                    self.result_head -= 1
                    if self.result_head < 0:
                        self.result_tape.insert(0, '0')
            elif tape == 'temp':
                if direction == 'R':
                    self.temp_head += 1
                    if self.temp_head >= len(self.temp_tape):
                        self.temp_tape.append('0')
                elif direction == 'L':
                    self.temp_head -= 1
                    if self.temp_head < 0:
                        self.temp_tape.insert(0, '0')

        def add_to_result(self):
            # Add the temporary tape value to the result tape (binary addition)
            self.result_head = 0
            self.temp_head = 0
            carry = 0

            while self.temp_head < len(self.temp_tape) or carry:
                if self.result_head >= len(self.result_tape):
                    self.result_tape.append('0')

                temp_bit = int(self.temp_tape[self.temp_head]) if self.temp_head < len(self.temp_tape) else 0
                result_bit = int(self.result_tape[self.result_head])

                sum_bit = temp_bit + result_bit + carry
                self.result_tape[self.result_head] = str(sum_bit % 2)
                carry = sum_bit // 2

                self.temp_head += 1
                self.result_head += 1

        def compute_square(self):
            # Multiply the input tape by itself (binary multiplication)
            self.reset_temp()
            for i in range(len(self.input_tape)):
                if self.input_tape[i] == '1':
                    # Shift the temporary tape by i and add to the result
                    self.temp_tape = ['0'] * i + self.input_tape
                    self.add_to_result()
            return self.result_tape

    squaring_tm = SquaringTuringMachine(binary_tape)
    return squaring_tm.compute_square()

def test_turing_machine():
    inputs = [
        "aaab", 
        "aaaaaaaaabbb",
        "aaaaaaaaaaaaaaaabbbb",
        "aaaab",
        "aaaabb",
        "bbaaaa",
        "aaaabba",
        " ",
        "landal",
        "aaaabbc",
        "aaaaaaaaaaaaaaaaaaaaaaaaabbbbb"
        ]

    for inp in inputs:
        print("\n------------------------------------------------------------------------------------------")
        print(f"Inputted String: {inp}")
        tm = TuringMachine(inp)
        tm.run()

test_turing_machine()

inputted_string = input('please input your string: ')
print(f"Inputted String: {inputted_string}")
tm = TuringMachine(inputted_string)
tm.run()