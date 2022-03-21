# Program to generate the 48 possible permutations of a 12 tone row

# Get P0, or the initial tone row, from the user in pitch class notation
def get_tone_row():
    p0 = input("Please enter the row in set notation, C = 0, C#/Db = 1, " 
               "... Bb = t, B = e: ")
    return p0

# Handle the conversions of string to int for calculations
def convert_pitch_string_to_int(pitch):
    if pitch == 't':
        return 10
    elif pitch == 'e':
        return 11
    else:
        return int(pitch)

# Handle the conversions of int to string for storage
def convert_pitch_int_to_string(pitch):
    if pitch == 10:
        return 't'
    elif pitch == 11:
        return 'e'
    else:
        return str(pitch)

# Modulus for note pitch addition
def musical_addition(pitch_1, pitch_2):
    return (convert_pitch_string_to_int(pitch_1) + 
           convert_pitch_string_to_int(pitch_2)) % 12

# Find the inversion of P0 to generate the starting pitches of the other rows
def find_inversion(tone_row):
    inversion = tone_row[0]
    for pitch in tone_row:
        if pitch == tone_row[0]:
            continue
        else:
            note = 12 - convert_pitch_string_to_int(pitch)
            inversion += convert_pitch_int_to_string(note)
    return inversion

# Generate each of the additional rows based on their relation to P0
def generate_table(tone_row, inversion_column):
    table = [''] * len(tone_row)

    row_count = 0
    while row_count < len(tone_row):
        if inversion_column[row_count] == tone_row[0]:
            table[0] = tone_row
            row_count += 1
        else:
            difference = musical_addition(tone_row[0], inversion_column[row_count])
            row_string = '' + inversion_column[row_count]
            position = 1
            while position < len(tone_row):
                row_string += convert_pitch_int_to_string(
                              musical_addition(tone_row[position],
                              convert_pitch_int_to_string(difference)))
                position += 1
            table[row_count] = row_string
            row_count += 1
    return table

# Display the completed permutation table to the user with note name 
# notation
def display_table(tone_row_permutations, start):

    # print inversion labels
    output = '   '
    for note in tone_row_permutations[0]:
        output += f' I{note} '
    print (output)

    # Convert the pitch class notation into letter notation
    for row in tone_row_permutations:
        newrow = ''
        for note in row:
            letter = convert_pitch_int_to_string(musical_addition(note, start))
            if letter == '0':
                newrow += 'C'
            elif letter == '1':
                newrow += 'D\u266D'
            elif letter == '2':
                newrow += 'D'
            elif letter == '3':
                newrow += 'E\u266D'
            elif letter == '4':
                newrow += 'E'
            elif letter == '5':
                newrow += 'F'
            elif letter == '6':
                newrow += 'G\u266D'
            elif letter == '7':
                newrow += 'G'
            elif letter == '8':
                newrow += 'A\u266D'
            elif letter == '9':
                newrow += 'A'
            elif letter == 't':
                newrow += 'B\u266D'
            else:
                newrow += 'B'
        
        # Pair the flats with the appropriate letters
        output = ''
        count = 0
        while count < len(newrow):
            if count == 0:
                output += f'P{row[0]}  '
            if (count + 1) < len(newrow):
                if newrow[count+1] == '\u266D':
                    output += newrow[count:count+2] + '  '
                    count += 2 
                    if count == len(newrow):
                        output += f'R{row[0]}'
                else:
                    output += newrow[count] + '   '
                    count += 1
            else:
                output += newrow[count] + f'   R{row[0]}'
                count += 1
        print (output)

    # print retrograde inversion labels
    output = '   '
    for note in tone_row_permutations[0]:
        output += f'RI{note} '
    print (output)

def main():
    tone_row = get_tone_row()
    inversion_column = find_inversion(tone_row)
    tone_row_permutations = generate_table(tone_row, inversion_column)
    display_table(tone_row_permutations, input("What is the pitch class of the starting pitch? "))

if __name__ == "__main__":
    main()