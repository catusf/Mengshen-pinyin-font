Todo list

[X] Design input, output for easier adding new typeface
[ ] Add bottom option
[ ] Add rotated options
[ ] Add Source Han Sans/Serif, probably the most comprehensive and opensource Han fonts, now build has errors (circular reference)
[X] Copy all glyphs from fonts
[X] Adjust width for long pinyins
[X] Fix Vietnamese char wrong in Micro Hei: ơ o7

Step to fix Micro Hei  issues:
- Delete None-Unicode glyphs (14000+)
- Fix deleted referenced glyphs: 'uniFA0C', 'uniFA0D'
