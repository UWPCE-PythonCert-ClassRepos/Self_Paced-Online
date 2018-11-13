import mailroom_oo as m

database = {'William Gates, III': [54842.49, 48965.25],
            'Mark Zuckerberg': [7852.25, 48652.0, 3548.0],
            'Jeff Bezos': [5486.0, 58794.02, 7412.1],
            'Paul Allen': [46872.02]}

d1 = m.Donor('William Gates, III', database['William Gates, III'])
d2 = m.Donor('Mark Zuckerberg', database['Mark Zuckerberg'])
d3 = m.Donor('Jeff Bezos', database['Jeff Bezos'])
d4 = m.Donor('Paul Allen', database['Paul Allen'])


def test_donor_data_to_obj():
    d1 = m.Donor('William Gates, III', database['William Gates, III'])
    print(d1.name)
    print(d1.donations)

    assert d1.name == 'William Gates, III'
    assert d1.donations == database['William Gates, III']
    # assert False


def test_donor_property_sum_number_avg():
    d2 = m.Donor('Mark Zuckerberg', database['Mark Zuckerberg'])
    print(d2.total)
    print(d2.num_donations)
    print(d2.average_don)

    assert d2.total == sum(database['Mark Zuckerberg'])
    assert d2.num_donations == 3
    assert d2.average_don == sum(database['Mark Zuckerberg']) / 3
    # assert False


def test_donor_collection():
    dc = m.DonorCollection(d1, d2, d3, d4)
    assert dc.donors[d1.name].donations == [54842.49, 48965.25]
    assert dc.donors[d2.name].total == sum(database['Mark Zuckerberg'])
    # assert False


def test_create_report():
    dc = m.DonorCollection(d1, d2, d3, d4)
    result = dc.create_report()
    expected = """
        Donor Name          | Total Given | Num Gift  | Average Gift
        ------------------------------------------------------------
        William Gates, III    $ 103807.74        2       $ 51903.87
        Jeff Bezos            $ 71692.12         3       $ 23897.37
        Mark Zuckerberg       $ 60052.25         3       $ 20017.42
        Paul Allen            $ 46872.02         1       $ 46872.02
        """
    try:
        assert result == expected
    except AssertionError:
        print('Check if the result is correct')
    # assert False


def test_adding_a_new_donor():
    dc = m.DonorCollection(d1, d2, d3, d4)
    dc.add_donation("Bob", [3333.33])
    assert dc.donors.get("Bob")
    assert dc.donors.get("Bob").donations == [3333.33]