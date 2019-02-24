# fast-lang
Language detection tool based on fastText pretrained model.

## Text preprocessing
Numbers, punctuation and repeating whitespaces are removed before feeding into language detector tool.

## Examples
```python
from fastlang import FastLangDetect

detector = FastLangDetect()

detector.detect('Where is my mother?') 
# {'en': 0.996435284614563}

detector.detect('Where is my mother?', k=3)
# {'en': 0.996435284614563, 'th': 0.0005820714286528528, 'bn': 0.0005180443404242396}
```
As the examples demonstrates you can specify how many labels to return with associated probabilities. 
Output can also be controlled by the `threshold` parameter which filters result based on probability value.
```python
detector.detect('Where is my mother?', k=3, threshold=0.5)
# {'en': 0.996435284614563}
```
Labels are ISO 639-1 encoded. If you want to check what is the corresponding language use `iso_codes`
```python
from fastlang import iso_codes

iso_codes['en']
# 'English'
```
Language detector also works with lists of strings.
```python
from fastlang import FastLangDetect

detector = FastLangDetect()

detector.detect(['Where is my mother?', 'pies i kot na drodze.'])
# [{'en': 0.996435284614563}, {'sl': 0.6256219148635864}] 
```
All 176 model lables can be exposed via `get_labels()` method.
```python
detector.get_labels()
```
If you want associated frequencies just pass `include_freq=True` to the `get_labels` method.

## Installation
`pip install .`
