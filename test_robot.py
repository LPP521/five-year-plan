from mock import patch, Mock
import robot as module


@patch.object(module, 'make_plans', return_value=['to be great', 'to be so cool'])
def test_get_a_good_plan_returns_a_plan_from_make_plans(mock_make_plans):
    assert module.get_a_good_plan() in mock_make_plans()


@patch.object(module, 'make_plans', return_value=['our best plan', 'we have thought so too'])
def test_get_a_good_plan_does_not_return_a_plan_with_banned_words(mock_make_plans):
    assert module.get_a_good_plan() == ''


def test_generate_plans_from_text_model_returns_expected_number_of_plans():
    mock_text_model = Mock()
    mock_text_model.make_short_sentence_with_start.side_effect = lambda starting_phrase, _: starting_phrase
    number_of_plans = 5
    assert len(module.generate_plans_from_text_model(mock_text_model, number_of_plans)) == number_of_plans
