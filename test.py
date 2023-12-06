def create_complex(real, imag):
    return {'real': real, 'imag': imag}


def obtain_real(imaginary):
    return imaginary['real']


def obtain_imag(imaginary):
    return imaginary['imag']


# Create a function to transform complex into a readable string that takes into consideration being positive or negative
def complex_to_string(complex):
    if complex['imag'] < 0:
        return str(complex['real']) + " - " + str(abs(complex['imag'])) + "i"
    else:
        return str(complex['real']) + " + " + str(abs(complex['imag'])) + "i"


def sum_complex(complex1, complex2):
    return create_complex(complex1['real'] + complex2['real'], complex1['imag'] + complex2['imag'])


def sub_complex(complex1, complex2):
    return create_complex(complex1['real'] - complex2['real'], complex1['imag'] - complex2['imag'])


def multiply_complex(complex1, complex2):
    return create_complex(
        complex1['real'] * complex2['real'] - complex1['imag'] * complex2['imag'],
        complex1['real'] * complex2['imag'] + complex1['imag'] * complex2['real'],
    )


def divide_complex(complex1, complex2):
    return create_complex(
        (complex1['real'] * complex2['real'] + complex1['imag'] * complex2['imag']) / (
                complex2['real'] ** 2 + complex2['imag'] ** 2),
        (complex1['imag'] * complex2['real'] - complex1['real'] * complex2['imag']) / (
                complex2['real'] ** 2 + complex2['imag'] ** 2),
    )


def main():
    complex1 = create_complex(5, 2)
    complex2 = create_complex(4, -7)

    print(complex_to_string(complex1))
    print(complex_to_string(complex2))

    complex3 = sum_complex(complex1, complex2)
    print(complex_to_string(complex3))

main()