from DayPass.check_day_pass import day_pass
from DayPass.navigation_in_day_pass import navigation_in_day_pass


class GetRewards:
    def get(self):
        navigation_in_day_pass.click_to_day_pass()
        self._get_all_events()

    def _get_all_events(self):
        navigation_in_day_pass.going_through_all_events(day_pass.get_all)


get_rewards = GetRewards()


