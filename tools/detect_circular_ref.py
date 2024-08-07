from fontTools.ttLib import TTFont

def find_dependent_glyphs(font_path, target_glyph_name):
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()

    dependent_glyphs = []

    for glyph_name in glyph_set.keys():
        glyph = glyph_set[glyph_name]
        if hasattr(glyph, 'components'):
            for component in glyph.components:
                if component.baseGlyph == target_glyph_name:
                    dependent_glyphs.append(glyph_name)
                    break

    return dependent_glyphs

# Example usage
font_path = '/workspaces/Mengshen-pinyin-font/res/fonts/han-serif/NotoSansSC-Regular.ttf'
target_glyph_name = 'uni7023'

dependent_glyphs = find_dependent_glyphs(font_path, target_glyph_name)
print(f"Glyphs dependent on '{target_glyph_name}': {dependent_glyphs}")
