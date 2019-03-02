import mailroom9 as mr

def test_donor():
    
    # Create an empty donor instance
    d1 = mr.Donor("Margo Hayes")
    assert d1.name == "Margo Hayes"
    assert d1.n_donations == 0
    assert d1.sum_donations == 0
    # Add donations to an empty instance
    d1.add_donation(20.16)
    assert d1.n_donations == 1
    assert d1.sum_donations == 20.16
    
    # Creat a donor with an initial donation
    d2 = mr.Donor("Tommy Caldwell", 20.17)
    assert d2.n_donations == 1
    assert d2.sum_donations == 20.17
    d2.add_donation(1.01)
    assert d2.n_donations == 2
    
    