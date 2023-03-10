![Surfy.Wiki](https://github.com/surfy-one/core.py/blob/main/imgs/cover.wiki.png?raw=true "Surfy.Wiki")

# Wikipedia Python Library

<br/>

## Installation

```
pip3 install surfy
```
<br/>

## Usage
```python

from surfy.wiki import Wiki

wiki = Wiki()

# Or

options = {
	'ua': 'Mozilla/4.0', # User Agent
	'redirect': 1,
	'lang': 'en'
}

wiki = Wiki(options) # options are optional

```
<br/>

### Get Page by Title or Page ID

```python

'''

wiki.page(
	addr=Address # str Title or int PageID,
	lang=Language # Default 'en'
)

'''
page = wiki.page('Eiffel Tower')

page.status_code # Status Code - e.g. 200 it's ok, 404 - not found
page.id # Page ID
page.url # Page URL
page.title # Page Title
page.content # Page Plain Text Content
page.links # All links from the page
page.summary # Plain Text Summary

```
<br/>

### Set global language

```python

wiki.set_lang('fr')

```

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