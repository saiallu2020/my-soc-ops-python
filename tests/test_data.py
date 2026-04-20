from app.data import QUESTIONS


def test_tech_life_question_pool_size_and_uniqueness():
    assert len(QUESTIONS) == 24
    assert len(set(QUESTIONS)) == 24


def _count_matches(keywords: set[str]) -> int:
    lowered_questions = [question.lower() for question in QUESTIONS]
    return sum(
        1
        for question in lowered_questions
        if any(keyword in question for keyword in keywords)
    )


def test_questions_include_coding_habits():
    coding_keywords = {"code", "debug", "test", "variable", "print statements"}
    assert _count_matches(coding_keywords) >= 4


def test_questions_include_ide_preferences():
    ide_keywords = {
        "ide",
        "editor",
        "dark mode",
        "theme",
        "font",
        "tabs over spaces",
        "vim keybindings",
    }
    assert _count_matches(ide_keywords) >= 5


def test_questions_include_developer_culture():
    culture_keywords = {
        "works on my machine",
        "standup",
        "version control",
        "pair program",
        "commit",
        "docs",
    }
    assert _count_matches(culture_keywords) >= 4
