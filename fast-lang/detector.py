from fastText import FastText
from urllib.request import urlretrieve
from os import path
import re

__all__ = [
    'MODEL_FILE',
    'FastLangDetect'
]

# default model location
MODEL_FILE = path.join(path.dirname(__file__), 'model', 'model.ftz')

class FastLangDetect(object):
    """Text needs to be UTF-8 encoded.
    """

    def __init__(self, model=MODEL_FILE):
        self.model = FastText.load_model(model)

    def detect(self, item, *args, **kwargs):
        """Predict languge using string or list
        of strings.

        Parameters:
        -----------

        item: str or list
            input string or list of strings.

        k: int, default 1
            Controls number of returned labels

        threshold: float, default 0.0
            filters the returned labels by a threshold on probability.
            A choice of 0.5 will return labels with at least 0.5 probability.

        on_unicode_error: str, default 'strict'

        Returns:
        --------

        dict with language labels and probabilities or
        list of dicts.
        """

        if isinstance(item, str):
            text = self._preprocess(item)
            res = self.model.predict(text, *args, **kwargs)

            key = [self._clean_label(x) for x in res[0]]
            val = res[1].tolist()
            return dict( zip(key,val) )
        else:
            text = [self._preprocess(x) for x in item]
            res = self.model.predict(text, *args, **kwargs)

            ret = []
            keys = res[0]
            vals = res[1]

            for row_key, row_val in zip(keys, vals):
                key = [self._clean_label(x) for x in row_key]
                val = row_val.tolist()

                ret.append( dict(zip(key,val)) )

            return ret

    def get_labels(self, *args, **kwargs):
        """Return all labels of the trained model.

        Parameters:
        -----------

        include_freq: bool, default False
            Return dictionary of labels with associated frequencies

        on_unicode_error: str, default 'strict'
        """

        res = self.model.get_labels(*args, **kwargs)

        if isinstance(res, tuple):
            key = [self._clean_label(x) for x in res[0]]
            val = res[1].tolist()

            return dict( zip(key,val) )
        else:
            return [self._clean_label(x) for x in res]

    def download_model(self, url):
        print('Attempting to download model file from: %s' % url)
        urlretrieve(url, MODEL_FILE)
        print('Model save in %s' % MODEL_FILE)

    def _preprocess(self, text):
        # remove numbers, interpunction
        pre = re.sub(r'[^\s\w]', ' ', text)
        # remove whitespace
        pre = re.sub(r'\s+', ' ', pre)

        return pre

    def _clean_label(self, label):
        return label.replace('__label__', '')

if __name__ == '__main__':

    lang = FastLangDetect()

    print( lang.detect('komputery del xps 150 za pół ceny', k=5) )
    print( lang.detect(['Ala ma kota', 'Your mother gay'], k=3))
    print( lang.get_labels(include_freq=False) )
