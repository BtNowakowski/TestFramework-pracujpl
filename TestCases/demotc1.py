import time

import pytest

from Pages.pracujpl_launch_page import LaunchPage
from Pages.results_page import ResultPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_job(self):
        lp = LaunchPage(self.driver, self.wait)
        lp.select_location("Zabrze", "Bytom", "Katowice")
        lp.select_position("Tester Oprogramowania", "QA")
        lp.click_submit()
        rp = ResultPage(self.driver, self.wait)
        rp.check_title("tester oprogramowania", "Zabrze")

        time.sleep(4)