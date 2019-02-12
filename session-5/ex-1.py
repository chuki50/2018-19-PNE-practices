def count_a(seq):
    """Counting the number of 'A's in the sequence."""

    # Counter for the 'A's.
    counter_a = 0

    for b in seq:
        if b == 'A':
            counter_a += 1

    # Return the result.
    return counter_a


# Main program
s = str(input("Please, enter the sequence:"))
# Count the number of As, using the function we have seen before
na = count_a(s)
print("The number of As is: {}".format(na))

# Calculate the total sequence length.
tl = len(s)

# These are some exceptions or errors that we have to take into account.
invalid_bases = False
invalid_length = False
for x in s:
    if x not in ['A', 'G', 'C', 'T']:
        invalid_bases = True
        break

if tl == 0:
    invalid_length = True

# Now, we can complete the program.
if invalid_bases:
    print("One or more of your bases is not valid. Check the sequence you entered:", s)
elif invalid_length:
    print("Your sequence is empty. Try entering a new one.")
else:
    # Calculate the percentage of 'A's in the sequence
    percentage_a = round(100.0 * na / tl, 1)

    print("The total length is: {}".format(tl))
    print("The percentage of As is: {}".format(percentage_a))
