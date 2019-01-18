def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.qq.com" in msg
    assert 0

def test_noop(shuchu):
    msg = shuchu
    print(msg)

