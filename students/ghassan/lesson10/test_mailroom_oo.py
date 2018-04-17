from mailroom_oo import Donor, Mailroom


def test_donor():
    e = Donor('Ghassan', [100, 200, 300])
    assert e.total_donations == 100+200+300
    e.add_donation(400)
    assert e.total_donations == 100+200+300+400


def test_mailroom():
    donor1 = Donor('Ghassan', [100, 200, 300])
    donor2 = Donor('Miles', [52, 241, 736])
    donor3 = Donor('Jack', [425, 100, 245])
    mr = Mailroom([donor1, donor2, donor3])
    assert mr.donors == [donor1, donor2, donor3]
    donor4 = Donor('Tony', [55, 342, 765])
    mr.add_donor(donor4)
    assert mr.donors == [donor1, donor2, donor3, donor4]
    assert mr.get_donor('Miles') == donor2
    assert mr.send_thankyou('Ghassan') == 'Thank you {} for your generous donation of {}'.format(
        mr.get_donor('Ghassan').name, mr.get_donor(
            'Ghassan').total_donations
    )
    assert mr.all_donors() == ['Ghassan', 'Miles', 'Jack', 'Tony']
    assert mr.list_donors() == '\n'.join(['Ghassan', 'Miles', 'Jack', 'Tony'])


def test_mailroom_multiplier():
    donor1 = Donor('Ghassan', [100, 200, 300])
    x = donor1.mult_donations_by(2)
    assert sum(x) == (100+200+300)*2


def test_mailroom_min():
    donor1 = Donor('Ghassan', [100, 200, 300])
    x = donor1.mult_donations_by(2, min_donation=150)
    assert sum(x) == (200+300)*2


def test_mailroom_max():
    donor1 = Donor('Ghassan', [100, 200, 300])
    x = donor1.mult_donations_by(2, max_donation=220)
    assert sum(x) == (200+100)*2
