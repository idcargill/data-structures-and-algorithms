import pytest
from code_challenges.hashmap_repeat.hashmap_repeat_word import repeated_word

class Text:
  a = "Once upon a time, there was a brave princess who..."
  b = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
  c = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

@pytest.fixture
def text():
  text = Text()
  return text


@pytest.mark.hr
def test_repeat_word_a(text):
  result = repeated_word(text.a)
  assert result['first duplicate'] == 'a'


@pytest.mark.hr
def test_repeat_word_a(text):
  result = repeated_word(text.b)
  assert result['first duplicate'] == 'it'

@pytest.mark.hr
def test_repeat_word_a(text):
  result = repeated_word(text.c)
  assert result['first duplicate'] == 'summer'


@pytest.mark.hr
def test_repeat_word_all_c(text):
  result = repeated_word(text.c)
  assert result['totals'] == {'it': 1, 'was': 2, 'a': 1, 'queer': 1, 'sultry': 1, 'summer': 2, 'the': 2, 'they': 1, 'electrocuted': 1, 'rosenbergs': 1, 'and': 1, 'i': 2, 'didn': 1, 't': 1, 'know': 1, 'what': 1, 'doing': 1, 'in': 1, 'new': 1, 'york': 1}

@pytest.mark.hr
def test_repeat_word_all_a(text):
  result = repeated_word(text.a)
  assert result['totals']['once'] == 1