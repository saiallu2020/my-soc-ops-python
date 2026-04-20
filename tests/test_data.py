from app.data import QUESTIONS


def test_tech_life_question_pool_size_and_uniqueness():
    assert len(QUESTIONS) == 24
    assert len(set(QUESTIONS)) == 24


def test_questions_include_coding_habits():
    assert any("codes" in question for question in QUESTIONS)
    assert any("debugs" in question for question in QUESTIONS)
    assert any("tests" in question for question in QUESTIONS)


def test_questions_include_ide_preferences():
    assert any("dark mode" in question for question in QUESTIONS)
    assert any("ide" in question for question in QUESTIONS)
    assert any("tabs over spaces" in question for question in QUESTIONS)


def test_questions_include_developer_culture():
    assert any("works on my machine" in question for question in QUESTIONS)
    assert any("standup" in question for question in QUESTIONS)
    assert any("version control" in question for question in QUESTIONS)
