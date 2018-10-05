from mailroom4 import create_report, add_new_donor, create_letters, quit, donors, create_thank_you

def test_add_new_donor():
    add_new_donor("todd schultz", 123)
    assert "todd schultz" in donors[-1]
    assert 123 in donors[-1]

def test_create_letters():
    assert "3368" in open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session06/letters/baby huey.txt').read()

def test_quit():
    assert quit() is "exit_menu"

def test_create_thank_you():
	assert "baby huey" in donors[0]

def test_make_donors_list():
    assert "3368" in open('/Users/toddschultz/Projects/UW/Self_Paced-Online/Students/toddschultz/session06/letters/baby huey.txt').read()




