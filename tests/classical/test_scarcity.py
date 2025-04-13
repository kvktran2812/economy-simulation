import pytest
import numpy as np
from src.classical.scarcity import *


@pytest.mark.parametrize(
        "good1, good2, expected_output",
        [
            ([29, 145], [35, 84], np.array([[174., 145.,   0.], [  0.,  35., 119.]])),
            ([29, 145, 35], [84, 133, 143], np.array([[209., 174., 145., 0.], [0., 143., 227., 360.]])),
            ([29], [145], np.array([[29., 0.], [0., 145.]]))
        ]
)
def test_ppc_2goods(good1, good2, expected_output):
    good1 = np.array(good1)
    good2 = np.array(good2)
    ppc = ppc_2goods(good1, good2)
    assert np.allclose(ppc, expected_output)


def test_ppc_2goods_error():
    good1 = np.random.randint(low=20, high=200, size=(2,))
    good2 = np.random.randint(low=20, high=200, size=(3,))

    with pytest.raises(ValueError, match="Size of 2 list of goods is not the same"):
        ppc_2goods(good1, good2)