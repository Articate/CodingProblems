import findmultiples

cases = {
    #    n : answer
        10 : 23,
        15 : 45,
        25 : 143
    }

class TestSumMultiples:
    @staticmethod
    def test_sum_multiples():
        for n, answer in cases.items():
            assert findmultiples.sum_multiples(n) == answer

class TestSumMultiplesOptimized:
    @staticmethod
    def test_optimized():
        for n, answer in cases.items():
            assert findmultiples.sum_mutliples_optimized(n, [3, 5]) == answer