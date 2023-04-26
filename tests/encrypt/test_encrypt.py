from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("cassio", 4) == "oi_ssac"
    assert encrypt_message("cassio", 3) == "sac_ois"
    assert encrypt_message("cassio", 9) == "oissac"
    with pytest.raises(TypeError):
        encrypt_message("retorna_erro", "1")
