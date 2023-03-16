# Surfy° Words Python Library

<br/>

## Installation

```
pip install surfy
```
<br/>

## Usage
```python

from surfy.words import Words

words = Words()

# Or

options = {
	'api_key': 'YOUR_FREE_API_KEY', # https://surfy.one
}

words = Words(options) # options are optional

corpus = 'Surfy is an ecosystem of hardware and software solutions based on artificial intelligence, combining technologies which synthesise basic human senses - vision, hearing and speech, text, geo-positioning, search for new information and intelligence, all of which can be used to increase efficiency and broaden human potential. Surfy is an ecosystem of software. Digity content: 1987, 1ml raw bites, 8,39239, 2937. Redundant Content: Surfy is an ecosystem of software. Surfy is an ecosystem of hardware. Surfy is an ecosystem of hardware. Surfy is an ecosystem of software. Surfy is an ecosystem of hardware.'

```
<br/>

### Get Digitization of the text
Return index between 0 and 1, where 1 means only digits

```python

digity_index = words.digity(corpus)

'''

Returns 0.03296703296703297

'''

```
<br/>

### Get Redundancy of the text
Return index between 0 and 1, where 1 means only redundancy text presents

```python

redundancy_index = words.redundancy(corpus)

'''

Returns 0.18644067796610164

'''

```
<br/>


<br />
<br />

## MIT License

Alexander Yermolenko • [surfy.one](https://surfy.one)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.