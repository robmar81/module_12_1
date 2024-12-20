import runner
import unittest


class RunerTest(unittest.TestCase):
    def test_walk(self):
        wlk = runner.Runner('гуляка')
        for i in range(10):
            wlk.walk()
        self.assertEqual(wlk.distance, 50)


    def test_run(self):
        rnr = runner.Runner('беглец')
        for i in range(10):
            rnr.run()
        self.assertEqual(rnr.distance, 100)


    def test_challenge(self):
        wlk = runner.Runner('гуляка')
        rnr = runner.Runner('беглец')
        for i in range(10):
            wlk.walk()
            rnr.run()
        self.assertNotEqual(wlk.distance, rnr.distance)


if __name__ == "__main__":
    unittest.main()
